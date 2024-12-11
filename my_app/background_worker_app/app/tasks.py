from my_app.background_worker_app.app.db import get_db_connection
from celery import Celery

app = Celery('background_worker_app', broker='redis://localhost:6379/0')


@app.task
def insert_customer_data(first_name, last_name, phone_number, monthly_salary):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
            INSERT INTO customer_data (first_name, last_name, phone_number, monthly_salary)
            VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query, (first_name, last_name, phone_number, monthly_salary))
            connection.commit()
            cursor.close()
            print(f"Inserted into table1: {first_name} {last_name}")
        except Exception as e:
            print(f"Error inserting data into table1: {e}")
        finally:
            connection.close()


@app.task
def insert_loan_data(loan_amount,tenure,interest_rate,monthly_repayment,emis_paid_on_time,start_date,end_date):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
            INSERT INTO loan_amount(loan_amount,tenure,interest_rate,monthly_repayment,emis_paid_on_time,start_date,end_date)
            VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query, (loan_amount,tenure,interest_rate,monthly_repayment,emis_paid_on_time,start_date,end_date))
            connection.commit()
            cursor.close()
            print(f"Inserted into table2: {loan_amount}")
        except Exception as e:
            print(f"Error inserting data into table2: {e}")
        finally:
            connection.close()

