from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from datetime import datetime, timedelta

dfeault_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "forex_data_pipeline",
    start_date=datetime(2021, 1, 1),
    schedule_interval="@daily",
    dfeault_args=dfeault_args,
    catchup=False,
) as dag:
    
    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available",
        http_conn_id="forex_api",
        endpoint="https://gist.github.com/marclamberti/f45f872dea4dfd3eaa015a4a1af4b39b"
    )
