#!/usr/bin/env groovy
podTemplate(label: 'docs',
  containers: [
    containerTemplate(name: 'build', image: "gcr.io/plaidcloud-build/tools/python-build:latest", ttyEnabled: true, command: 'cat', alwaysPullImage: true, workingDir: '/home/jenkins/agent')
  ],
  serviceAccount: 'jenkins',
  imagePullSecrets: ['gcr-key']
)
{
  node(label: 'docs') {
    properties([
      [$class: 'JiraProjectProperty'], buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '10', daysToKeepStr: '', numToKeepStr: '50')),
      parameters([
        booleanParam(name: 'no_cache', defaultValue: true, description: 'Adds --no-cache flag to docker build command(s).'),
        booleanParam(name: 'skip_lint', defaultValue: false, description: 'Do not lint.'),
        booleanParam(name: 'full_lint', defaultValue: false, description: 'Lint all files.'),
        stringParam(name: 'image_name', defaultValue: 'gcr.io/plaidcloud-build/docs', description: 'Fully-qualified image name for GCR upload.'),
        stringParam(name: 'chart_app', defaultValue: 'docs', description: 'Name of application in plaidcloud helm chart.'),
        stringParam(name: 'argo_app', defaultValue: 'io-plaid', description: 'Name of argo application used to deploy/manage this project.'),
        stringParam(name: 'target_lint_dir', defaultValue: 'docs', description: 'Name of directory to run linter against.')
      ])
    ])
    container('build') {
      scm_map = checkout([
        $class: 'GitSCM',
        branches: scm.branches,
        doGenerateSubmoduleConfigurations: false,
        extensions: [[$class: 'SubmoduleOption', disableSubmodules: false, parentCredentials: true, recursiveSubmodules: true, reference: '', trackingSubmodules: true]],
        submoduleCfg: [],
        userRemoteConfigs: scm.userRemoteConfigs
      ])

      branch = env.CHANGE_BRANCH ?: scm_map.GIT_BRANCH.minus(~/^origin\//)

      stage("Run Checks") {
        if (!params.skip_lint) {
          sh """
            export BRANCH=$branch
            export TARGET_LINT_DIR=$target_lint_dir

            # Lint python files (this script uses env vars above):
            lint
          """

          if (branch == 'master') {
            recordIssues tool: pyLint(pattern: 'pylint.log')
          } else {
            recordIssues tool: pyLint(pattern: 'pylint.log'), qualityGates: [[threshold: 1, type: 'TOTAL_HIGH', unstable: true]]
          }

          // Check licenses on all python packages.
          license_errors = sh (
            returnStatus: true,
            script: '''
              set +x 
              cat license-report.txt | grep "UNAUTHORIZED" > /dev/null
            '''
          ) == 0
          if (license_errors) {
              output = sh returnStdout: true, script: '''
                set +x 
                cat license-report.txt | grep "UNAUTHORIZED"
              '''
              echo "\nThe following python package licenses are unauthorized:\n\n$output"
              currentBuild.result = 'UNSTABLE'
          } else {
            echo "No licensing issues found."
          }
        }
      }

      if( currentBuild.result != 'Unstable') {
        stage("Build Image") {
          withCredentials([string(credentialsId: 'docker-server-ip', variable: 'host')]) {
            docker.withServer("$host", "docker-server") {
              withCredentials([dockerCert(credentialsId: 'docker-server', variable: "DOCKER_CERT_PATH")]) {
                docker.withRegistry('https://gcr.io', 'gcr:plaidcloud-build') {

                  // Params are always strings. Convert to the type we want.
                  image_label = "${scm_map.GIT_COMMIT.substring(0, 7)}-${BUILD_NUMBER}"

                  build_args = [
                    PLAID_BUILD_TAG: image_label
                  ]
                  
                  // TODO: parameterize this so invidivual builds can be given custom build args.
                  // Concatenate build args to docker command.
                  docker_args = ""
                  build_args.each { entry -> docker_args += " --build-arg $entry.key=$entry.value" }
                  
                  if (params.no_cache) {
                    docker_args += ' --no-cache'
                  }

                  image = docker.build("${image_name}:latest", "--pull ${docker_args} .")

                  if (branch == 'master') {
                    image.push()
                    image.push(image_label)
                  }
                }
              }
            }
          }
        }

        if (branch == 'master') {
          stage("Deploy to Kubernetes") {
            withCredentials([usernamePassword(credentialsId: 'plaid-machine-user', usernameVariable: 'user', passwordVariable: 'pass')]) {
              withCredentials([string(credentialsId: 'argocd-token', variable: 'ARGOCD_AUTH_TOKEN')]) {
                sh """
                  export ARGOCD_SERVER=deploy.plaidcloud.io
                  argocd app set $params.argo_app -p ${params.chart_app}.image="$params.image_name:$image_label"
                """
              }
            }
          }
        }
      }
    }
  }
}
