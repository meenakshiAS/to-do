pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'curl -sSL https://install.python-poetry.org | python3;export PATH="$HOME/.local/bin:$PATH";poetry --version;easy_install build;poetry run python3 -m build'
                stash(name: 'compiled-results', includes: 'to-do/*.py*')
            }
        }
        stage('Test') {
            steps {
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
