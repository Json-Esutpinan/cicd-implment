
pipeline {
    agent any

    environment {
        AZURE_RESOURCE_GROUP = 'SWII-CICD'
        AZURE_APP_NAME = 'productosjson'
        AZURE_REGION = 'Canada Central'
        VENV_DIR = 'venv' 
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                git branch: 'main',url: 'https://github.com/Json-Esutpinan/cicd-implment.git'
            }
        }

        stage('Setup Virtual Environment and Install Dependencies') {
            steps {
                script {
                    // 1. Crear el entorno virtual
                    sh "python3 -m venv ${VENV_DIR}"
                    echo "Virtual environment created at ${VENV_DIR}"

                    // 2. Activar el entorno virtual y actualizar pip
                    // Usamos 'source' para activar el venv en el shell actual
                    // y luego ejecutamos los comandos de pip
                    sh """
                        bash -c "
                            source ${VENV_DIR}/bin/activate && \\
                            pip install --upgrade pip && \\
                            pip install -r requirements.txt
                        "
                    """
                    echo "Dependencies installed into virtual environment."
                }
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
}

    post {
        always {
            cleanWs()
            echo "Process Finalized"// Limpia el espacio de trabajo después de cada ejecución
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
