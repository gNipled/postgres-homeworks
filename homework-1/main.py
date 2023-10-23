import csv
import os
import psycopg2

employee_data_path = os.path.join('north_data', 'employees_data.csv')
customers_data_path = os.path.join('north_data', 'customers_data.csv')
orders_data_path = os.path.join('north_data', 'orders_data.csv')

"""Скрипт для заполнения данными таблиц в БД Postgres."""

employee_data = []
with open(employee_data_path, 'r', newline='') as file:
    for row in csv.DictReader(file):
        employee_data.append(
            (row['employee_id'],
             row['first_name'],
             row['last_name'],
             row['title'],
             row['birth_date'],
             row['notes']
             ))

customers_data = []
with open(customers_data_path, 'r', newline='') as file:
    for row in csv.DictReader(file):
        customers_data.append(
            (row['customer_id'],
             row['company_name'],
             row['contact_name']
             ))

orders_data = []
with open(orders_data_path, 'r', newline='') as file:
    for row in csv.DictReader(file):
        orders_data.append(
            (row['order_id'],
             row['customer_id'],
             row['employee_id'],
             row['order_date'],
             row['ship_city']
             ))

with psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='1963'
) as conn:

    with conn.cursor() as cursor:
        cursor.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',  employee_data)
        cursor.executemany('INSERT INTO customers VALUES (%s, %s, %s)', customers_data)
        cursor.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', orders_data)

conn.close()
