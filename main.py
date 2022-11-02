from flask import Flask,request, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your secret key'


@app.route('/')
def hello():
    return jsonify("Hello")

@app.route('/init')
def init():
    mydb = mysql.connector.connect( host="${DB_HOST}", user="${DB_USERNAME}", password="${DB_PASSWORD}") #change the host to hostname that you gave in database container as conatiner_name
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE cr")
    return jsonify("DB Created")

@app.route('/table')
def table():
    mydb = mysql.connector.connect( host="${DB_HOST}", user="${DB_USERNAME}", password="${DB_PASSWORD}", database="${DB_NAME}")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE temp(name VARCHAR(255), rarity VARCHAR(255))")
    return jsonify("Table Created")

@app.route('/list')
def list():
    mydb = mysql.connector.connect( host="${DB_HOST}", user="${DB_USERNAME}", password="${DB_PASSWORD}", database="${DB_NAME}")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM temp")
    output = mycursor.fetchall()
    return jsonify(output)

@app.route('/post',methods=['POST'])
def post():
    mydb = mysql.connector.connect( host="${DB_HOST}", user="${DB_USERNAME}", password="${DB_PASSWORD}", database="${DB_NAME}")
    mycursor = mydb.cursor()
    new_name = request.form["name"]
    new_rarity = request.form["rarity"]
    sql = "INSERT INTO temp (name, rarity) VALUES (%s, %s)"
    mycursor.execute(sql, (new_name, new_rarity))
    mydb.commit()
    return jsonify("Record Added")

if __name__ == "__main__":
    app.run(debug=1)
