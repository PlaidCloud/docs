#!/usr/bin/env groovy
import groovy.transform.Field

@Field 
def image_name = "gcr.io/plaidcloud-build/docs"

@Field
def image_label = ""

@Field
def branch = ""

@Field
def chart_name = "docs"

@Field
def argo_app = "docs"

podTemplate(label: 'docs',
  containers: [
    containerTemplate(name: 'docker', image: 'docker:18.09.9-git', ttyEnabled: true, command: 'cat'),
    containerTemplate(name: 'argocd', image: "gcr.io/plaidcloud-build/tools/argocd:latest", ttyEnabled: true, command: 'cat', alwaysPullImage: true, workingDir: '/home/jenkins/agent')
  ],
  serviceAccount: 'jenkins',
  imagePullSecrets: ['gcr-key']
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
            docker.withRegistry('https://gcr.io', 'gcr:plaidcloud-build') {
              
              // Checkout source before doing anything else
              scm_map = checkout([
                  $class: 'GitSCM',
                  branches: scm.branches,
                  doGenerateSubmoduleConfigurations: false,
                  extensions: [[$class: 'SubmoduleOption', disableSubmodules: false, parentCredentials: true, recursiveSubmodules: true, reference: '', trackingSubmodules: true]],
                  submoduleCfg: [],
                  userRemoteConfigs: scm.userRemoteConfigs
              ])

              // When building from a PR event, we want to read the branch name from the CHANGE_BRANCH binding. This binding does not exist on branch events.
              branch = env.CHANGE_BRANCH ?: scm_map.GIT_BRANCH.minus(~/^origin\//)

              docker_args = ''

              // Add any extra docker build arguments here.
              if (params.no_cache) {
                docker_args += '--no-cache'
              }

              stage('Build Image') {
                image = docker.build("${image_name}:latest", "--pull ${docker_args} .")
              }

              // No need to publish dev branches.
              if (branch == 'master') {

                stage('Publish to DockerHub') {
                  image.push()
                }

                stage('Push Git Tag') {
                  // Add additional, unique image tag and push.
                  // https://github.com/jenkinsci/docker-workflow-plugin/blob/50ad50bad2ee14eb73d1ae3ef1058b8ad76c9e5d/src/main/resources/org/jenkinsci/plugins/docker/workflow/Docker.groovy#L176-L179
                  image_label = "${scm_map.GIT_COMMIT.substring(0, 7)}-${BUILD_NUMBER}"
                  image.push(image_label)
                }
              }
            }
          }
        }
      }
    }
    container('argocd') {
      if (branch == 'master') {
        stage("Deploy to Kubernetes") {
          withCredentials([usernamePassword(credentialsId: 'plaid-machine-user', usernameVariable: 'user', passwordVariable: 'pass')]) {
            withCredentials([string(credentialsId: 'argocd-token', variable: 'ARGOCD_AUTH_TOKEN')]) {
              sh """
                export ARGOCD_SERVER=deploy.plaidcloud.io

                # Verify, lint, check versions, package, and push helm chart, along with copying chart changes to k8s repo for argo.
                check_helm_chart --repo-path=$env.WORKSPACE --chart-name=$chart_name
                package_helm_chart --repo-url=https://$user:$pass@github.com/PlaidCloud/k8s.git --chart-name=$chart_name
                
                # Tell argo which image version to use.
                argocd app set $argo_app -p spec.image="$image_name:$image_label"
              """
            }
          }
        }
      } else {
        stage('Process Helm Chart Changes') {
          // This script will lint, check for version increment, and dry-run an install.
          sh "check_helm_chart --repo-path=$env.WORKSPACE --chart-name=$chart_name"
        }
      }
    }
  }
}
