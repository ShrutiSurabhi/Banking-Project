import mysql.connector
import pandas as pd
from numpy import record


def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(user='str',
                                             password='12345678',
                                             host='127.0.0.1',
                                             port='3306',
                                             database='ticket_event')
    except Exception as error:
        print("Error while connecting to database for job tracker", error)

    return connection

def run_load_third_party(file_path_csv):
    #file_path_csv = 'ticket_sale.csv'
    connection = get_db_connection()
    print("load data ...", end=" ")
    load_third_party(connection, file_path_csv)
    print("done")
    connection.close()

def load_third_party(connection, file_path_csv):
    cursor = connection.cursor()
    df = pd.read_csv(file_path_csv)
    st = ("INSERT INTO ticket_sale "
          "(ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, event_addr, customer_id, price, num_tickets) "
          " VALUES (%(ticket_id)s, %(trans_date)s, %(event_id)s,"
          " %(event_name)s, %(event_date)s, %(event_type)s, %(event_city)s, %(event_addr)s,"
          " %(customer_id)s, %(price)s, %(num_tickets)s)")
    print(st)
    try:
        for i, row in df.iterrows():
            insert_val = {}
            insert_val['ticket_id'] = int(row['ticket_id'])
            insert_val['trans_date'] = int(row['trans_date'])
            insert_val['event_id'] = int(row['event_id'])
            insert_val['event_name'] = row['event_name']
            insert_val['event_date'] = row['event_date']
            insert_val['event_type'] = row['event_type']
            insert_val['event_city'] = row['event_city']
            insert_val['event_addr'] = row['event_addr']
            insert_val['customer_id'] = int(row['customer_id'])
            insert_val['price'] = float(row['price'])
            insert_val['num_tickets'] = int(row['num_tickets'])

            cursor.execute(st, insert_val)
    except Exception as e:
        print(e)
    # [Iterate through the CSV file and execute insert statement]
    connection.commit()
    cursor.close() 
    #csv linked 


