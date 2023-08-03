pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/Brandonawan/ansible-manage-keys.git'
        GIT_CREDENTIALS = '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' // Jenkins credential ID for GitHub access token
    }

    stages {
        stage('Clone Git Repository') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: GIT_REPO_URL, credentialsId: GIT_CREDENTIALS]]])
            }
        }

        stage('Run Ansible Playbook') {
            environment {
                PRIVATE_KEY = credentials('JENKINS_PRIVATE_KEY')
            }
            steps {
                sh "ansible-playbook -i hosts.ini --private-key=${PRIVATE_KEY} manage_ssh_keys.yml"
            }
        }
    }
}
