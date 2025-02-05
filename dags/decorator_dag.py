from datetime import datetime, timedelta
from airflow.decorators import dag, task

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG using the @dag decorator
@dag(
    dag_id='python_operator_dag',
    default_args=default_args,
    description='A simple DAG using PythonOperator',
    start_date=datetime(2025, 1, 28),
    schedule_interval=timedelta(minutes=1),
    catchup=False,
)
def hello_world_etl():
    @task()
    def get_name():
        return "Nataraj"

    @task()
    def get_age():
        return "29"

    @task()
    def greet(fname, age):
        print(f"Hello world! My name is {fname} and I am {age} years old.")

    # Set up the task dependencies
    name = get_name()
    age = get_age()
    greet(name, age)

# Instantiate the DAG
dag = hello_world_etl()
