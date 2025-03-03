pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'cd to-do'
                sh 'sudo pip install poetry'
                sh 'poetry run python3 -m build'
                stash(name: 'compiled-results', includes: 'to-do/*.py*')
            }
        }
        stage('Test') {
            steps {
                sh 'cd to-do'
                sh 'poetry run pytest --junit-xml test-reports/results.xml test ./to-do'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }

        }

    }
}
