pipeline {
    agent any

    environment {
        SSH_KEY = '/home/ec2-user/.ssh/oregon-pk.pem'
        SSH_USER = 'ec2-user'
        TARGET_IP = '35.87.63.53'
    }

    stages {
        stage('Build') {
            steps {
                sh '/usr/local/bin/pipenv install --dev'
            }
        }

        stage('Test') {
            steps {
                sh '/usr/local/bin/pipenv run pytest'
            }
        }

        stage('Package') {
            when {
                anyOf {
                    branch 'master'
                    branch 'release'
                }
            }
            steps {
                sh 'zip -r sbdl.zip lib'
            }
        }

        stage('Release') {
            when {
                branch 'release'
            }
            steps {
                sh """
                scp -i ${SSH_KEY} -o 'StrictHostKeyChecking no' -r sbdl.zip log4j2.properties sbdl_main.py sbdl_submit.sh conf ${SSH_USER}@${TARGET_IP}:/home/${SSH_USER}/sbdl-qa
                """
            }
        }

        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                sh """
                scp -i ${SSH_KEY} -o 'StrictHostKeyChecking no' -r sbdl.zip log4j2.properties sbdl_main.py sbdl_submit.sh conf ${SSH_USER}@${TARGET_IP}:/home/${SSH_USER}/sbdl-prod
                """
            }
        }
    }
}
