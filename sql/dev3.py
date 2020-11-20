import mysql.connector
import  csv
mydb = mysql.connector.connect(
# mydb = mysql.connect(
    host = 'localhost',
    user = "root",
    password="",
    database = 'customers',
)
with open('customer.csv') as csv_file:
    customer_file = csv.reader(csv_file,delimiter = ',')
    all_value = []
    for row in customer_file:
        value =(row[0] , row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
        all_value.append(value)

sql = "Insert into data_customer (customerid,firstname,lastname,companyname,billingaddress1,billingaddress2,city,state,postalcode,country,phonenumber,emailaddress,createddate) Value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cur = mydb.cursor()
cur.executemany(sql,all_value)
mydb.commit()