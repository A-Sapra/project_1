pipeline {
    agent any
    environment {
        NEXUS_LOGIN=credentials('NEXUS_LOGIN')
    }
    stages {
        stage('build') {
            steps {
                sh "sudo docker build -t localhost:8083/pythonapp:newest ."
                sh "sudo docker image ls"
            }   
        }
        stage('push')
            steps{
                sh "sudo docker login -u $(NEXUS_LOGIN_USR) -p ${NEXUS_LOGIN_PSW)"
            }
        }
    }
}
