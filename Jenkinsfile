pipeline {
environment {
	registry = "iitzhakk/dev_proj_4b"
	registryCredential = 'docker hub credentials'
	dockerImage = ''
	}
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
			  sleep(5)
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
    stage('Deploy image') {
        steps {
			dir("dev_project_3b"){
			  bat "echo IMAGE_TAG=${env.BUILD_NUMBER}>.env"
			  bat "more .env"
              bat "docker build -t dev_proj_4b:${env.BUILD_NUMBER} ."
			  bat "docker tag dev_proj_4b:${env.BUILD_NUMBER} iitzhakk/dev_proj_4b:${env.BUILD_NUMBER}"
              bat "docker push iitzhakk/dev_proj_4b:${env.BUILD_NUMBER}"
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
	stage('Deploy HELM') {
        steps {
			bat "minikube start"
			bat "helm install --set image.version=iitzhakk/dev_proj_4b:${env.BUILD_NUMBER} isaac ./isaac"
			bat "start /B minikube service isaac > k8s_url.txt"
			bat "more k8s_url.txt"
		  }
    }
	stage('clean HELM') {
        steps {
			bat 'minikube delete'
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