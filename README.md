
#Iniciando o projeto

python3 -m venv venv

source venv/bin/activate

export AIRFLOW_HOME=$(pwd)/airflow

AIRFLOW_VERSION=2.5.0
PYTHON_VERSION=3.9

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"


pip install "apache-airflow[postgres,celery,redis]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

airflow db init


airflow users create \
    --username admin \
    --firstname Guilherme \
    --lastname Correa \
    --role Admin \
    --email guilherme@admin.com.br
    

informe a senha

airflow webserver


airflow scheduler


