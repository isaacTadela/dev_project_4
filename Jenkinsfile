pipeline {
agent any
stages {
    stage('pull from git') {
        steps {
            bat 'git.exe clean -ffdx'
            bat 'git clone https://github.com/isaacTadela/dev_project_3b'
        }
    }
    stage('rest app') {
        steps {
			dir("dev_project_3b"){
			  bat 'start /min python rest_app.py'
			}
        }
    }
    stage('testing backend') {
        steps {
			dir("dev_project_3b"){
			  bat 'python backend_testing.py'
          }
		}
    }
    stage('clean environment') {
        steps {
			dir("dev_project_3b"){
              bat 'python clean_environment.py'
          }
		}
    }
    stage('build image') {
        steps {
			dir("dev_project_3b"){
              bat 'docker build -t iitzhakk/dev_proj_4b .'
          }
		}
    }
    stage('push image') {
        steps {
			dir("dev_project_3b"){
			  bat "echo IMAGE_TAG=${env.BUILD_NUMBER}>.env"
			  bat "more .env"
              bat 'docker push -q iitzhakk/dev_proj_3b:{env.BUILD_NUMBER}'
          }
		}
    }
    stage('docker-compose up') {
        steps {
			dir("dev_project_3b"){
			  bat 'docker-compose up -d'
          }
		}
    }
    stage('testing docker-compose') {
        steps {
			dir("dev_project_3b"){
              bat 'python docker_backend_testing.py'
          }
		}
    }
    stage('clean docker environment') {
        steps {
			dir("dev_project_3b"){
              bat 'docker-compose down -v --rmi all'
          }
		}
    }
 }
 post {
        always {
            echo 'One way or another, I have finished'
			bat 'git.exe clean -ffdx' /* clean up our workspace */
        }
        success {
            echo 'I succeeded!'
        }
        failure {
            echo 'I failed :('
        }
    }
}