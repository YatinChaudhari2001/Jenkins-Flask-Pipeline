pipeline {
    agent any
    stages {
        stage ('SCM Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YatinChaudhari2001/Jenkins-Flask-Pipeline.git'
            }
        }
        
        stage ('docker image build') {
            steps {
              sh '/usr/bin/docker image build -t yatinchaudhari/myflaskpipeline .'   
            }
        }
        
        
        stage ('docker auth login') {
            steps {
                sh '/usr/bin/docker login -u yatinchaudhari --password-stdin | echo dckr_pat_cPpi3Ns_D1U4NsiPqUatb5TSr_w '
            }
        }
        
        
        stage ('push image') {
            steps {
                sh '/usr/bin/docker image push yatinchaudhari/myflaskpipeline'
            }
        }
        
        stage ('get the confirmation from user') {
            steps {
                input 'Do you want to deploy this application ?'
            }   
        }
 

        stage ('remove existing service') {
            steps {
                sh '/usr/bin/docker service rm flask-service'
            }
        }
        
        stage ('creation of new service if not') {
            steps {
                    sh '/usr/bin/docker service create --name flask-service -p 4000:4000 --replicas 2 yatinchaudhari/myflaskpipeline'
            }
        }
    }
}    
