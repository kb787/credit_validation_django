import pandas as pd
from my_app.background_worker_app.app.tasks import insert_loan_data, insert_customer_data

# Mapping Excel files to tables
FILE_TABLE_MAPPING = {
    "data/loan_data.xlsx": insert_loan_data,
    "data/customer_data.xlsx": insert_customer_data
}


def parse_excel_and_enqueue(file_path, insert_function):
    try:
        # Read Excel file into DataFrame
        df = pd.read_excel(file_path)
        for _, row in df.iterrows():
            if insert_function == insert_customer_data:
                insert_function.delay(
                    row['First Name'],
                    row['Last Name'],
                    row['Phone Number'],
                    float(row['Monthly Salary'])
                )
            elif insert_function == insert_loan_data:
                insert_function.delay(
                    row['Loan Amount'],
                    row['Tenure'],
                    row['Interest Rate'],
                    row['Monthly Repayment'],
                    row['EMIs Paid on Time'],
                    row['Start Date'],
                    row['End Date']
                )
        print(f"All tasks enqueued for file: {file_path}")
    except Exception as e:
        print(f"Error parsing or enqueuing tasks for {file_path}: {e}")


if __name__ == "__main__":
    for file_path, insert_function in FILE_TABLE_MAPPING.items():
        parse_excel_and_enqueue(file_path, insert_function)
