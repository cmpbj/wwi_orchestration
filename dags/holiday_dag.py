from airflow import DAG
from airflow.decorators import task, dag
from airflow.models import Variable
from datetime import datetime
from dags.src.utils import holiday_func

# Define DAG properties
default_args = {
    "start_date": datetime(2025, 3, 28),
    "schedule": "@yearly",  # Schedule it to run once a year
    "catchup": False,
}

# Variable to track if the backfill has already been executed
BACKFILL_VAR_KEY = "holiday_ingestion_backfill_done"

@dag(**default_args)
def holiday_ingestion_dag():
    @task
    def holiday_ingestion():
        """Handles both the initial backfill and yearly updates."""
        current_year = datetime.now().year
        backfill_done = Variable.get(BACKFILL_VAR_KEY, default_var="false") == "true"

        if not backfill_done:
            # Backfill last 20 years
            for year in range(current_year - 19, current_year + 1):
                holiday_func(date=year)
            Variable.set(BACKFILL_VAR_KEY, "true")  # Mark backfill as done
        else:
            # Only process the new year
            holiday_func(date=current_year)

    holiday_ingestion()

dag_instance = holiday_ingestion_dag()
