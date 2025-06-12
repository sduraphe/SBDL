pipeline {
    agent any

    environment {
        SSH_KEY = '/home/ec2-user/.ssh/oregon-pk.pem'  // Replace if needed
        SSH_USER = 'ec2-user'
        TARGET_IP = '35.87.63.53'
        PIPENV = '/usr/local/bin/pipenv'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '${PIPENV} install --ignore-pipfile'
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
                    scp -i ${SSH_KEY} -o 'StrictHostKeyChecking no' \
                    sbdl.zip log4j2.properties sbdl_main.py sbdl_submit.sh conf \
                    ${SSH_USER}@${TARGET_IP}:/home/${SSH_USER}/sbdl-qa
                """
            }
        }

        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                sh """
                    scp -i ${SSH_KEY} -o 'StrictHostKeyChecking no' \
                    sbdl.zip log4j2.properties sbdl_main.py sbdl_submit.sh conf \
                    ${SSH_USER}@${TARGET_IP}:/home/${SSH_USER}/sbdl-prod
                """
            }
        }
    }
}
