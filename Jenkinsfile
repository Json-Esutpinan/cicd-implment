pipeline {
    agent any

    environment {
        AZURE_RESOURCE_GROUP = 'SWII-CICD'
        AZURE_APP_SERVICE_NAME = 'productosjson'
        AZURE_REGION = 'Canada Central'
        AZURE_CREDENTIALS_ID = 'TU_ID_CREDENCIALES_AZURE'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Json-Esutpinan/cicd-implment.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'pytest'
            }
        }
        stage('Run Flask App') {
            steps {
                sh '''
                    pkill -f "flask run" || true
                    export FLASK_APP=app.py
                    nohup flask run --host=0.0.0.0 --port=5000 > flask.log 2>&1 &
                '''
            }
        }
        stage('Deploy to Azure App Service') {
            steps {
                azureWebAppPublish azureCredentialsId: "${AZURE_CREDENTIALS_ID}",
                                   appName: "${AZURE_APP_SERVICE_NAME}",
                                   resourceGroup: "${AZURE_RESOURCE_GROUP}",
                                   sourceDirectory: '.'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
