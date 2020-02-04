#!/usr/bin/env groovy
import groovy.transform.Field

@Field 
def image_name = "plaidcloud/docs"

@Field
def image_label = ""

@Field
def branch = ""

podTemplate(label: 'docs',
  containers: [
    containerTemplate(name: 'docker', image: 'docker:18.09.9', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'kubectl', image: "lachlanevenson/k8s-kubectl:v1.15.9", ttyEnabled: true, command: 'cat')
  ],
  serviceAccount: 'jenkins'
)
{
  node(label: 'docs') {
    properties([
      parameters([
        booleanParam(name: 'no_cache', defaultValue: false, description: 'Adds --no-cache flag to docker build command(s).')
      ])
    ])
    container('docker') {
      withCredentials([string(credentialsId: 'docker-server-ip', variable: 'host')]) {
        docker.withServer("$host", "docker-server") {
          withCredentials([dockerCert(credentialsId: 'docker-server', variable: "DOCKER_CERT_PATH")]) {
            docker.withRegistry("", "plaid-docker") {
              dir('docs') {
                scm_map = checkout scm
              }

              // When building from a PR event, we want to read the branch name from the CHANGE_BRANCH binding. This binding does not exist on branch events.
              branch = env.CHANGE_BRANCH ?: scm_map.GIT_BRANCH.minus(~/^origin\//)

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
              if (branch == 'master') {

                stage('Publish to DockerHub') {
                  image.push()
                }

                stage('Push Git Tag') {
                  // Add additional, unique image tag and push.
                  // https://github.com/jenkinsci/docker-workflow-plugin/blob/50ad50bad2ee14eb73d1ae3ef1058b8ad76c9e5d/src/main/resources/org/jenkinsci/plugins/docker/workflow/Docker.groovy#L176-L179
                  image_label = scm_map.GIT_COMMIT.substring(0, 7)
                  image.push(image_label)
                }
              }
            }
          }
        }
      }
    }
    if (branch == 'master') {
      container('kubectl') {
        stage("Deploy to Kubernetes") {
          sh "kubectl -n plaid set image deployment/docs docs=${image_name}:${image_label} --record"
        }
      }
    }
  }
}
