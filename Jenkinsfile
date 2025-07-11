pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'flask-cicd-demo'
        DOCKER_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = 'flask-app'
        APP_PORT = '5000'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest"
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    sh "docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} python -c 'import app; print(\"App imported successfully\")'"
                }
            }
        }
        
        stage('Stop Old Container') {
            steps {
                echo 'Stopping old container...'
                script {
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                script {
                    sh "docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:5000 ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
        
        stage('Health Check') {
            steps {
                echo 'Performing health check...'
                script {
                    sleep 5
                    sh "curl -f http://localhost:${APP_PORT}/health || exit 1"
                }
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up unused Docker images...'
            sh "docker image prune -f"
        }
        success {
            echo 'Pipeline completed successfully!'
            echo "Application is running at: http://localhost:${APP_PORT}"
        }
        failure {
            echo 'Pipeline failed!'
            sh "docker logs ${CONTAINER_NAME} || true"
        }
    }
}
