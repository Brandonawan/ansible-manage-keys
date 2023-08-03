pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/Brandonawan/ansible-manage-keys.git'
        GIT_CREDENTIALS = 'github_pat_11ARUZ4WI0uKc7xuJ9Ta' // Jenkins credential ID for GitHub access token
        PRIVATE_KEY_PATH = '/var/lib/jenkins/.ssh/id_rsa'
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
            steps {
                sh "ansible-playbook -i hosts.ini --private-key=${env.PRIVATE_KEY_PATH} manage_ssh_keys.yml"
            }
        }
    }
}
