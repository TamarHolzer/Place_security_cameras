from flask import Flask, request, jsonify
import pyodbc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Database connection string
conn_str = r'DRIVER={SQL Server};SERVER=LAPTOP-QF9SMRIF\SQLEXPRESS;DATABASE=project;Trusted_Connection=yes;'


@app.route('/Registration', methods=['POST'])
def CreatCostumer():
    try:
        data = request.json
        NameC = data['name']
        ID = data['postalCode']
        PasswordC = data['password']
        Email = data['email']
        User_type = data['userType']

        with pyodbc.connect(conn_str) as connection:
            cursor = connection.cursor()

            # Insert user data into the Users table
            query = """
                INSERT INTO Customer (NameC,ID,PasswordC,Email,User_type) 
                VALUES (?,?,?,?,?)
            """
            cursor.execute(query, (NameC, ID, PasswordC, Email, User_type))#מריץ את הSQL
            connection.commit()#שומר שינויים
            # connection.close()#סוגר את החיבור

        return jsonify({'status': 'success'}), 200


    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
