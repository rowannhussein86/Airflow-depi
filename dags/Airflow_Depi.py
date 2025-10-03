from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random

def print_welcome():
    print("Welcome! My name is Rowan Hussein")

def generate_random():
    number = random.randint(1, 100)
    with open("/tmp/random.txt", "w") as f:
        f.write(str(number))
    print(f"Random number {number} saved to /opt/airflow/random.txt")


with DAG(
    dag_id="Airflow_Depi",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,   
    catchup=False,
    tags=["Depi"],
) as dag:

    task1 = BashOperator(
        task_id="print_date",
        bash_command="date"
    )

    task2 = PythonOperator(
        task_id="print_welcome",
        python_callable=print_welcome
    )
    
    task3 = PythonOperator(
        task_id="generate_random",
        python_callable=generate_random
    )

task1 >> task2 >> task3  