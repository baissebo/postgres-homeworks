"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os

import psycopg2
import csv


def main():
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='basadannih')
    try:
        with conn:
            with conn.cursor() as cur:
                folder_path = "north_data"
                files = [
                    os.path.join(folder_path, "employees_data.csv"),
                    os.path.join(folder_path, "customers_data.csv"),
                    os.path.join(folder_path, "orders_data.csv")]

                for file in files:
                    with open(file, 'r') as csv_file:
                        next(csv_file)

                        if "employees_data.csv" in file:
                            for row in csv.reader(csv_file):
                                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
                        elif "customers_data.csv" in file:
                            for row in csv.reader(csv_file):
                                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
                        elif "orders_data.csv" in file:
                            for row in csv.reader(csv_file):
                                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)
    except psycopg2.Error as e:
        print("Ошибка выполнения операции", e)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
