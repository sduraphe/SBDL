pipeline {
    agent any

    environment {
        PIPENV = '/var/lib/jenkins/.local/bin/pipenv'
        SSH_KEY = '/home/ec2-user/.ssh/oregon-pk.pem'   // 🔁 Replace with your actual .pem path
        SSH_USER = 'ec2-user'                          // 🔁 Replace if different (e.g., ubuntu)
        TARGET_IP = '35.86.216.16'
    }

    stages {
        stage('Build') {
            steps {
                sh '${PIPENV} --python python3 sync'
            }
        }
        stage('Test') {
            steps {
                sh '${PIPENV} run pytest'
            }
        }
        stage('Package') {
            when {
                anyOf {
                    branch "master"
                    branch "release"
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
