from datetime import timedelta, datetime

from airflow import DAG

from airflow.operators.python import PythonOperator

# Un diccionario que despues será pasado como parámetro en la creación del DAG

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def limpieza():
    with open('../scripts/Limpieza.py', 'r') as f:
        exec(f.read())

def carga():
    with open('../scripts/Carga.py', 'r') as f:
        exec(f.read())

with DAG(
    'ETL',
    default_args = default_args,
    description = 'Extrae los datos, los limpia y los carga a la DB',
    schedule_interval = timedelta(weeks=4),
    start_date = datetime(2023, 2, 25, 15, 50),
    tags = ['ETL','Limpieza','Carga'],
) as dag:
    limpieza_task = PythonOperator(task_id="limpieza", python_callable=limpieza)
    carga_task = PythonOperator(task_id="carga", python_callable=carga)

    limpieza_task >> carga_task