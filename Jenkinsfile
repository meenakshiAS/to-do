pipeline {
    agent any
    stages {
        stage('BuildStage') {
            steps {
                sh 'python3 -m build'
                stash(name: 'compiled-results', includes: 'to-do/*.py*')
            }
        }
        stage('Test') {
            steps {
                sh 'pytest --junit-xml test-reports/results.xml test ./to-do'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }

        }

    }
}
