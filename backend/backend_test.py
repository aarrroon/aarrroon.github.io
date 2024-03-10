import requests
import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS


DATABASE_URL = "https://dates-fd71bc03469b.herokuapp.com/"
POSTGRES_URL = "postgres://uf8be187h4nlk3:pd6b97fef32d82edc18a09f693e71b14979a777a6f3f47ca6db2c25015d698c4c@ceu9lmqblp8t3q.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dt64j7nmchagp"

app = Flask(__name__)
CORS(app)


# Functions
def test_backend(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        print('Backend test successful!')
    else:
        print('Backend test failed. Status code:', response.status_code)

# Establish Data Connection
def connect_postgres(url):
    try:
        connection = psycopg2.connect(POSTGRES_URL)
        cursor = connection.cursor()
        print('Postgres connection successful!')
        return connection, cursor
    except Exception as e:
        print('Postgres connection failed:', e)

@app.route('/test_data')
def get_test_data():
    # Connect to the database
    # Execute SQL query to select test data
    cursor.execute("SELECT * FROM POI")

    # Fetch all rows
    rows = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    connection.close()

    result = [{'id': row[0], 'name': row[1]} for row in rows]
    print(result)
    # Return JSON response
    return jsonify(result)



if __name__ == '__main__':
    # test_backend(DATABASE_URL)
    connection, cursor = connect_postgres(POSTGRES_URL)

    app.run()
