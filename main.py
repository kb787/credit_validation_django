# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from my_app.background_worker_app.scripts.parse_excel import parse_excel_and_enqueue


def main():
    # Parse and enqueue tasks for the files and tables
    print("Starting data ingestion process...")
    parse_excel_and_enqueue("./my_app/background_worker_app/data/customer_data.xlsx", "insert_customer_data")
    parse_excel_and_enqueue("./my_app/background_worker_app/data/loan_data.xlsx", "insert_loan_data")
    print("Data ingestion process completed.")


if __name__ == "__main__":
    main()

