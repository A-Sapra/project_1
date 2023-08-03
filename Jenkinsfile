pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh "cd project_1"
                sh "sudo docker build -t localhost:8083/pythonapp:newest ./project_1/"
                sh "sudo docker image ls"
            }
            
        }
        
    }
}
