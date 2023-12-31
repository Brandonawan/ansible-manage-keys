pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/Brandonawan/ansible-manage-keys.git'
        GIT_CREDENTIALS = credentials('git-token') // Jenkins credential ID for GitHub access token
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
                withCredentials([sshUserPrivateKey(credentialsId: 'JENKINS_PRIVATE_KEY', keyFileVariable: 'PRIVATE_KEY')]) {
                    sh "ansible-playbook -i hosts.ini --private-key=${PRIVATE_KEY} manage_ssh_keys.yml"
                }
            }
        }
    }
}
