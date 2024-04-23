# from flask import Flask, render_template, request
# from flask_mysqldb import MySQL
# app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Jaatbhai2850@'
# app.config['MYSQL_DB'] = 'dcc_ass'
# mysql = MySQL(app)
# @app.route('/',methods=["GET","POST"])
# def home():
#     if request.method == 'POST':
#         var1 = request.form['Item_1']
#         cur = mysql.connection.cursor()
#         cur.execute("SELECT * FROM comments WHERE id = {}".format(var1))
#         fetchdata = cur.fetchall()
#         cur.close()
#         return render_template('index.html',data = fetchdata)
# if __name__ == '__main__':
#     app.run(debug=True,port=8000)
from flask import Flask, redirect, url_for, request, Response, render_template,jsonify
from flask_mysqldb import MySQL
import matplotlib.pyplot as plt
from io import BytesIO
import base64

plt.switch_backend('Agg')
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Jaatbhai2850@'
app.config['MYSQL_DB'] = 'dcc_ass'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return ('Name: Prateek Takshak,' 
            'Roll Number: 23110256')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['query']
        results_purchase, results_redemption = search_output(search_query)
        return render_template('search_results.html', results_purchase=results_purchase, results_redemption=results_redemption)
def search_output(bond_number):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM csv1 WHERE `Bond Number` = %s OR `Name of the Purchaser` = %s OR `Reference No (URN)` = %s OR `Issue Teller` = %s", (bond_number, bond_number, bond_number, bond_number))
    results_purchase = cursor.fetchall()
    cursor.execute("SELECT * FROM csv2 WHERE `Bond Number` = %s OR `Name of the Political Party` = %s OR `Pay Branch Code` = %s OR `Pay Teller` = %s", (bond_number, bond_number, bond_number, bond_number))
    results_redemption = cursor.fetchall()
    cursor.close()

    return results_purchase, results_redemption

# @app.route('/bar_chart_data', methods=['GET'])
# def bar_chart_data():
#     cursor = mysql.connection.cursor()  
#     cursor.execute("SELECT 'Name of the Political Party',  SUM(CAST(REPLACE('Denominations', ',', '') AS DECIMAL(20, 2))) FROM csv2 GROUP BY 'Name of the Political Party'")

#     results = cursor.fetchall()  
#     labels = [result[0] for result in results] 
#     sizes = [result[1] for result in results]  
#     data = {
#         "labels": labels,
#         "values": sizes
#     }

#     cursor.close() 
#     return jsonify(data) 
if __name__ == '__main__':
    app.run(debug=True)