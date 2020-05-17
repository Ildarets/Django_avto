import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def hello(context):
    return 'Hello'


def world(context):
    return 'World'


def save_to_file():
    with open('save_hello.txt', 'w') as f:
        f.write('Hello_world')


default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2020, 5, 5, 10, 00, 00),
    'concurrency': 1,
    'retries': 0
}

with DAG('my_first_dag',
         default_args=default_args,
         schedule_interval='*/1 * * * * ',
         ) as dag:
    opr_respond = PythonOperator(task_id='save_to_file',
                                 python_callable=save_to_file)

    opr_respond = PythonOperator(task_id='hello',
                                 python_callable=hello)

    opr_respond = PythonOperator(task_id='world',
                                 python_callable=world)

    world >> hello >> save_to_file