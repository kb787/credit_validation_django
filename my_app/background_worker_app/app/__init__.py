from celery import Celery


app = Celery('excel_to_db_ingestion', broker='redis://localhost:6379/0')
app.config_from_object('celeryconfig')
