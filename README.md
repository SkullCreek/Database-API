# Database-API
A python based API for CRUD operations for PostgresSQL and MongoDB.

Clone the files in your local system and download all the dependencies
Flask, Psycopg2, sqlalchemy, pandas, urllib, logging

Run the program:

Go to postman do the following

## PostgreSQL/MongoDB

### Insert
Hit the following url with POST method to insert.
```
http://127.0.0.1:5000/postgresql/insert
http://127.0.0.1:5000/mongodb/insert
```

write the following in the body section in JSON format and send the request to insert.
```json
{
    "user": "postgres",
    "host": "localhost",
    "port": "5432",
    "password": "xyz",
    "dbname": "xyz",
    "dataset": "csv_file",
    "dataset_name": "xyz"
}
```

### Update
Hit the following url with POST method to update.
```
http://127.0.0.1:5000/postgresql/update
http://127.0.0.1:5000/mongodb/update
```

write the following in the body section in JSON format and send the request to update.
```json
{
    "user": "postgres",
    "host": "localhost",
    "port": "5432",
    "password": "xyz",
    "dbname": "xyz",
    "table_name": "xyz",
    "set": "abc = 'xyz'",
    "condition": "Company = 'xyz'"
}
```

### Delete
Hit the following url with POST method to delete.
```
http://127.0.0.1:5000/postgresql/delete
http://127.0.0.1:5000/mongodb/delete
```

write the following in the body section in JSON format and send the request to delete.
```json
{
    "user": "postgres",
    "host": "localhost",
    "port": "5432",
    "password": "xyz",
    "dbname": "xyz",
    "table_name": "xyz",
    "condition": "Company = 'xyz'"
}
```

### Select
Hit the following url with POST method to select.
```
http://127.0.0.1:5000/postgresql/select
http://127.0.0.1:5000/mongodb/select
```

write the following in the body section in JSON format and send the request to select. It will return all the data in json format.
```json
{
    "user": "postgres",
    "host": "localhost",
    "port": "5432",
    "password": "xyz",
    "dbname": "xyz",
    "row": "*",
    "table_name": "xyz",
    "condition": "Company = 'xyz'"
}
```
