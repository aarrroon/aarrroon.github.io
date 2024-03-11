from flask import Flask
import os
from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

DATABASE_URL = "https://dates-fd71bc03469b.herokuapp.com/"
POSTGRES_URL = "postgres://uf8be187h4nlk3:pd6b97fef32d82edc18a09f693e71b14979a777a6f3f47ca6db2c25015d698c4c@ceu9lmqblp8t3q.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dt64j7nmchagp"

app = Flask(__name__)
CORS(app)

# Establish Data Connection
def connect_postgres(url):
    """
    Connects to a PostgreSQL database using the provided URL.

    Args:
        url (str): The URL of the PostgreSQL database.

    Returns:
        tuple: A tuple containing the connection and cursor objects.

    Raises:
        Exception: If the connection to the PostgreSQL database fails.

    """
    try:
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        print('Postgres connection successful!')
        return connection, cursor
    except Exception as e:
        print('Postgres connection failed:', e)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get_poi')
def get_poi():
    # Connect to the database
    # Execute SQL query to select test data
    connection, cursor = connect_postgres(POSTGRES_URL)

    cursor.execute("""
                    SELECT
                        poi_id,
                        poi_name,
                        poi_price,
                        poi_lat,
                        poi_long,
                        poi_address,
                        poi_suburb,
                        poi_type_name
                    FROM POI NATURAL JOIN POI_TYPE;
                   """)

    # Fetch all rows
    rows = cursor.fetchall()
    # Close cursor and connection
    cursor.close()
    connection.close()
    result = [{'id': row[0], 
                'name': row[1],
                'price': row[2], 
                'latitude': row[3], 
                'longitude': row[4], 
                'address': row[5], 
                'suburb': row[6],
                'activity_type': row[7],
                } for row in rows]
    # Return JSON response
    return jsonify(result)



app.run()
if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    print(port)
    app.run(host="0.0.0.0", port=port)

    # app.run()
    connection, cursor = connect_postgres(POSTGRES_URL)