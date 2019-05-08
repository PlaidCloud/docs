#!/usr/bin/env groovy

image_name = "plaidcloud/docs"

podTemplate(label: 'io',
  containers: [
    containerTemplate(name: 'docker', image: 'docker:18.09.5', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'kubectl', image: "lachlanevenson/k8s-kubectl:v1.13.5", ttyEnabled: true, command: 'cat')
  ],
  volumes: [
    hostPathVolume(hostPath: '/var/run/docker.sock', mountPath: '/var/run/docker.sock')
  ],
  serviceAccount: 'jenkins'
)
{
  node(label: 'io') {
    properties([
      parameters([
        booleanParam(name: 'no_cache', defaultValue: false, description: 'Adds --no-cache flag to docker build command(s).')
      ])
    ])
    container('docker') {
      docker.withRegistry('', 'plaid-docker') {
        dir('docs') {
          scm_map = checkout scm
        }

        // When building from a PR event, we want to read the branch name from the CHANGE_BRANCH binding. This binding does not exist on branch events.
        CHANGE_BRANCH = env.CHANGE_BRANCH ?: scm_map.GIT_BRANCH.minus(~/^origin\//)

        docker_args = ''

        // Add any extra docker build arguments here.
        if (params.no_cache) {
          docker_args += '--no-cache'
        }

        stage('Build Image') {
          dir('src') {
            git url: 'https://github.com/PlaidCloud/plaid.git', credentialsId: 'plaid-machine-user'
          }
          
          image = docker.build("${image_name}:latest", "--pull ${docker_args} -f docs/Dockerfile .")
        }

        // No need to publish dev branches.
        if (CHANGE_BRANCH == 'master') {

          stage('Publish to DockerHub') {
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
              sh "kubectl -n plaid set image deployment/docs docs=plaidcloud/${image_name}:${image_label} --record"
            }
          } 
        }
      }
    }
  }
}
