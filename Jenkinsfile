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
        // Checkout source
        scm_map = checkout([
            $class: 'GitSCM',
            branches: scm.branches,
            doGenerateSubmoduleConfigurations: false,
            extensions: [[$class: 'SubmoduleOption', disableSubmodules: false, parentCredentials: true, recursiveSubmodules: false, reference: '', trackingSubmodules: false]],
            submoduleCfg: [],
            userRemoteConfigs: scm.userRemoteConfigs
        ])

        // When building from a PR event, we want to read the branch name from the CHANGE_BRANCH binding. This binding does not exist on branch events.
        CHANGE_BRANCH = env.CHANGE_BRANCH ?: scm_map.GIT_BRANCH.minus(~/^origin\//)

        stage('Build Image') {

          dir('docs') {
            image = docker.build("${image_name}:latest", "--pull -f docs/Dockerfile .")
          }

          dir('src') {
            git url: 'https://github.com/PlaidCloud/plaid.git', credentialsId: 'plaid-machine-user'
          }          
        }

        // No need to publish dev branches, we can change this later.
        if (CHANGE_BRANCH == 'master') {

          stage('Publish to DockerHub') 
              image.push()

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
