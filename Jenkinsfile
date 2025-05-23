pipeline {
    agent any

    environment {
        AZURE_RESOURCE_GROUP = 'SWII-CICD'
        AZURE_APP_SERVICE_NAME = 'productosjson'
        // AZURE_REGION = 'Canada Central' // La región no es necesaria para el comando de despliegue
        AZURE_CREDENTIALS_ID = 'azure-service-principal' // ID de la credencial de Jenkins
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
                rm -rf venv
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        /* stage('Run Unit Tests') {
            steps {
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$PYTHONPATH:$(pwd)
                pytest
                '''
            }
        } */
        // La etapa 'Run Flask App' no suele ser necesaria para el despliegue a App Service
        // ya que Azure se encarga de iniciar la aplicación.
        /*
        stage('Run Flask App') {
            steps {
                sh '''
                pkill -f "flask run" || true
                . venv/bin/activate
                export FLASK_APP=app.py
                nohup flask run --host=0.0.0.0 --port=5000 > flask.log 2>&1 &
                '''
            }
        }
        */
        stage('Deploy to Azure App Service') {
            steps {
                // withCredentials inyecta las variables de entorno de tu Service Principal
                // (AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID)
                withCredentials([azureServicePrincipal(AZURE_CREDENTIALS_ID)]) {
                    sh '''
                        # Autenticarse con el Service Principal usando Azure CLI
                        az login --service-principal -u "$AZURE_CLIENT_ID" -p "$AZURE_CLIENT_SECRET" --tenant "$AZURE_TENANT_ID" --allow-no-subscription

                        # Desplegar la aplicación web al App Service
                        # El --src-path . indica que se despliega el contenido del directorio actual
                        az webapp deploy --resource-group "$AZURE_RESOURCE_GROUP" --name "$AZURE_APP_SERVICE_NAME" --src-path .

                        # Opcional: Cerrar sesión de Azure CLI después del despliegue
                        az logout
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}