#!/usr/bin/env groovy

plaid_image = "plaidcloud/docs"

podTemplate(label: 'io',
  containers: [
    containerTemplate(name: 'docker', image: 'docker:17.03.2', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'kubectl', image: "lachlanevenson/k8s-kubectl:v1.11.1", ttyEnabled: true, command: 'cat')
  ],
  volumes: [
    hostPathVolume(hostPath: '/var/run/docker.sock', mountPath: '/var/run/docker.sock')
  ],
  serviceAccount: 'jenkins'
)
{
  node(label: 'io') {

    container('docker') {
      docker.withRegistry('', 'gbates101') {

        stage('Build Image') {
          scm_map = checkout scm
          image = docker.build("${plaid_image}:latest", "--pull -f Dockerfile .")
        }

        // No need to publish dev branches, we can change this later. 
        if (scm_map.GIT_BRANCH == 'master') {

          stage('Publish to DockerHub') {
            stage('Push "latest" Tag') {
              image.push()
            }

            stage('Push Git Tag') {
              // Add additional, unique image tag and push.
              // https://github.com/jenkinsci/docker-workflow-plugin/blob/50ad50bad2ee14eb73d1ae3ef1058b8ad76c9e5d/src/main/resources/org/jenkinsci/plugins/docker/workflow/Docker.groovy#L176-L179
              image_label = scm_map.GIT_COMMIT.substring(0, 7)
              image.push(image_label)
            }

            stage("Deploy to Kubernetes") {
              container('kubectl') {
              sh "kubectl -n plaid set image deployment/docs docs=plaidcloud/docs:${image_label} --record"
              }
            }
          }
        }
      }
    }
  }
}