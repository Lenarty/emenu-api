from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import hashlib
import math
import smtplib, ssl
from email.mime.text import MIMEText


app = Flask(__name__)

# Configure DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'emenu'

mysql = MySQL(app)


@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM restaurant")
    row_headers = [x[0] for x in cur.description]
    details = cur.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/requests', methods=['GET'])
def get_requests():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM request")
    row_headers = [x[0] for x in cur.description]
    details = cur.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/restaurants/<id>', methods=['GET'])
def get_restaurants_id(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM restaurant WHERE restaurant.id = %s", [id])
    row_headers = [x[0] for x in cur.description]
    details = cur.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/restaurant', methods=['PUT'])
def update_restaurant():
    update = request.get_json()
    cur10 = mysql.connection.cursor()
    _id = update['id']
    _name = update['name']
    _location = update['location']
    cur10.execute("UPDATE restaurant SET name = %s, location = %s WHERE id = %s", (_name, _location, _id))
    mysql.connection.commit()
    cur10.close()
    return 'Success'


@app.route('/order', methods=['PUT'])
def update_order():
    update = request.get_json()
    cur10 = mysql.connection.cursor()
    _id = update['id']
    _meal_id = update['meal_id']
    _active_order = update['active_order']
    cur10.execute("UPDATE orders SET meal_id = %s, active_order = %s WHERE id = %s", (_meal_id, _active_order, _id))
    mysql.connection.commit()
    cur10.close()
    return 'Success'


@app.route('/clientorder', methods=['PUT'])
def update_clientorder():
    update = request.get_json()
    cur10 = mysql.connection.cursor()
    _id = update['id']
    _payment_done = update['payment_done']
    cur10.execute("UPDATE clientorders SET payment_done = %s WHERE id = %s", (_payment_done, _id))
    mysql.connection.commit()
    cur10.close()
    return 'Success'


@app.route('/meal', methods=['PUT'])
def update_meal():
    update = request.get_json()
    cur10 = mysql.connection.cursor()
    _id = update['id']
    _name = update['name']
    _type = update['type']
    _descripton = update['description']
    _price = update['price']
    _prep_time = update['prep_time']
    cur10.execute("UPDATE meal SET name = %s, type = %s, description = %s, price = %s, prep_time = %s WHERE id = %s",
                  (_name, _type, _descripton, _price, _prep_time, _id))
    mysql.connection.commit()
    cur10.close()
    return 'Success'


@app.route('/user', methods=['PUT'])
def update_user():
    update = request.get_json()
    cur10 = mysql.connection.cursor()
    _phone_number = update['phone_number']
    _name = update['name']
    _lastname = update['lastname']
    _password = update['password']
    _user_type = update['user_type']
    _restaurant_name = update['restaurant_name']
    _email = update['email']
    _epassword = hashlib.md5(str.encode(_password)).hexdigest()
    cur10.execute("UPDATE users SET name = %s, lastname = %s, email = %s, password = %s, user_type = %s, restaurant_name = %s WHERE phone_number = %s",
                  (_name, _lastname, _email, _epassword, _user_type, _restaurant_name, _phone_number))
    mysql.connection.commit()
    cur10.close()
    return 'Success'


@app.route('/meals', methods=['GET'])
def get_meals():
    cur1 = mysql.connection.cursor()
    cur1.execute(
        "SELECT meal.*,restaurant.name AS restaurant_name,restaurant.location AS restaurant_location FROM `meal` INNER JOIN restaurant ON meal.restaurant_id = restaurant.id")
    row_headers = [x[0] for x in cur1.description]
    details = cur1.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/meals/<id>', methods=['GET'])
def get_meals_id(id):
    cur1 = mysql.connection.cursor()
    cur1.execute(
        "SELECT meal.*,restaurant.name AS restaurant_name,restaurant.location AS restaurant_location FROM `meal` INNER JOIN restaurant ON meal.restaurant_id = restaurant.id WHERE meal.id = %s",
        [id])
    row_headers = [x[0] for x in cur1.description]
    details = cur1.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/users', methods=['GET'])
def get_users():
    cur2 = mysql.connection.cursor()
    cur2.execute("SELECT * FROM users")
    row_headers = [x[0] for x in cur2.description]
    details = cur2.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/users/<phonenumber>', methods=['GET'])
def get_users_phone_number(phonenumber):
    cur2 = mysql.connection.cursor()
    cur2.execute("SELECT * FROM users WHERE users.phone_number = %s", [phonenumber])
    row_headers = [x[0] for x in cur2.description]
    details = cur2.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/orders', methods=['GET'])
def get_orders():
    cur4 = mysql.connection.cursor()
    cur4.execute(
        "SELECT orders.* ,meal.price AS meal_price, meal.name AS meal_name, meal.type AS meal_type, meal.description AS meal_description, meal.prep_time AS meal_prep_time FROM orders INNER JOIN meal ON orders.meal_id = meal.id")
    row_headers = [x[0] for x in cur4.description]
    details = cur4.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/orders/<id>', methods=['GET'])
def get_orders_id(id):
    cur4 = mysql.connection.cursor()
    cur4.execute(
        "SELECT orders.* ,meal.price AS meal_price, meal.name AS meal_name, meal.type AS meal_type, meal.description AS meal_description, meal.prep_time AS meal_prep_time FROM orders INNER JOIN meal ON orders.meal_id = meal.id WHERE orders.phone_number =%s",
        [id])
    row_headers = [x[0] for x in cur4.description]
    details = cur4.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/clientorders', methods=['GET'])
def get_clientorders():
    cur5 = mysql.connection.cursor()
    cur5.execute(
        "SELECT clientorders.*,neworders.quantity AS quantity, neworders.meal_name AS meal_name, neworders.meal_type AS meal_type, neworders.meal_price AS meal_price, users.phone_number AS phone_number, users.name AS user_name, users.lastname AS user_lastname FROM clientorders INNER JOIN users ON clientorders.phone_number = users.phone_number INNER JOIN (SELECT orders.* , meal.name AS meal_name, meal.type AS meal_type, meal.description AS meal_description, meal.prep_time AS meal_prep_time, meal.price AS meal_price FROM orders INNER JOIN meal ON orders.meal_id = meal.id) AS neworders ON clientorders.order_id = neworders.id ")
    row_headers = [x[0] for x in cur5.description]
    details = cur5.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/clientorders/<id>', methods=['GET'])
def get_clientorders_id(id):
    cur5 = mysql.connection.cursor()
    cur5.execute(
        "SELECT clientorders.*, neworders.meal_name AS meal_name, neworders.meal_type AS meal_type, neworders.meal_price AS meal_price users.phone_number AS phone_number, users.name AS user_name, users.lastname as user_lastname FROM clientorders INNER JOIN users ON clientorders.phone_number = users.phone_number INNER JOIN (SELECT orders.* , meal.name AS meal_name, meal.type AS meal_type, meal.description AS meal_description, meal.prep_time AS meal_prep_time, meal.price AS meal_price FROM orders INNER JOIN meal ON orders.meal_id = meal.id) AS neworders ON clientorders.order_id = neworders.id WHERE clientorders.id = %s",
        [id])
    row_headers = [x[0] for x in cur5.description]
    details = cur5.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/kitchenorders', methods=['GET'])
def get_kitchenorders():
    cur4 = mysql.connection.cursor()
    cur4.execute(
        "SELECT kitchenorders.*,neworders.table_number AS table_number, neworders.quantity AS quantity ,neworders.meal_description AS meal_description, neworders.meal_name AS meal_name, neworders.meal_type AS meal_type, neworders.meal_prep_time AS meal_prep_time FROM kitchenorders INNER JOIN orders ON kitchenorders.order_id = orders.id INNER JOIN (SELECT orders.* , meal.name AS meal_name, meal.type AS meal_type, meal.description AS meal_description, meal.prep_time AS meal_prep_time FROM orders INNER JOIN meal ON orders.meal_id = meal.id) AS neworders ON kitchenorders.order_id = neworders.id")
    row_headers = [x[0] for x in cur4.description]
    details = cur4.fetchall()
    json_data = []
    for detail in details:
        json_data.append(dict(zip(row_headers, detail)))
    return jsonify(json_data)


@app.route('/restaurant', methods=['POST'])
def post_restaurant():
    restaurantDetails = request.get_json()
    _name = restaurantDetails['name']
    _location = restaurantDetails['location']
    cur6 = mysql.connection.cursor()
    cur6.execute("INSERT INTO restaurant(name, location) VALUES(%s, %s)", (_name, _location))
    mysql.connection.commit()
    cur6.close()
    return 'Succeess'


@app.route('/request', methods=['POST'])
def post_request():
    requestDetails = request.get_json()
    _description = requestDetails['description']
    _time = requestDetails['time']
    _restaurant = requestDetails['restaurant']
    cur6 = mysql.connection.cursor()
    cur6.execute("INSERT INTO request(description, time, restaurant) VALUES(%s, %s, %s)", (_description, _time, _restaurant))
    mysql.connection.commit()
    cur6.close()
    return 'Succeess'


@app.route('/user', methods=['POST'])
def post_user():
    userDetails = request.get_json()
    _lastname = userDetails['lastname']
    _name = userDetails['name']
    _password = userDetails['password']
    _phone_number = userDetails['phone_number']
    _userType = userDetails['user_type']
    _restaurant_name = userDetails['restaurant_name']
    _email = userDetails['email']
    _epassword = hashlib.md5(str.encode(_password)).hexdigest()
    cur3 = mysql.connection.cursor()
    cur3.execute("INSERT INTO users(phone_number, name, lastname, email, password, user_type, restaurant_name) VALUES(%s, %s, %s, %s, %s, %s, %s)",
                 (_phone_number, _name, _lastname, _email, _epassword, _userType,_restaurant_name))
    mysql.connection.commit()
    cur3.close()
    return 'Succeess'


@app.route('/meal', methods=['POST'])
def post_meal():
    mealDetails = request.get_json()
    _restaurantID = mealDetails['restaurant_id']
    _name = mealDetails['name']
    _type = mealDetails['type']
    _description = mealDetails['description']
    _price = mealDetails['price']
    _prepTime = mealDetails['prep_time']
    cur7 = mysql.connection.cursor()
    cur7.execute(
        "INSERT INTO meal(restaurant_id, name, type, description, price, prep_time) VALUES(%s, %s, %s, %s, %s, %s)",
        (_restaurantID, _name, _type, _description, _price, _prepTime))
    mysql.connection.commit()
    cur7.close()
    return 'Succeess'


@app.route('/order', methods=['POST'])
def post_orders():
    orderDetails = request.get_json()
    _mealId = orderDetails['meal_id']
    _active = orderDetails['active_order']
    _phone_number = orderDetails['phone_number']
    _quantity = orderDetails['quantity']
    _table_number = orderDetails['table_number']
    cur8 = mysql.connection.cursor()
    cur8.execute("INSERT INTO orders(meal_id, active_order, phone_number, quantity, table_number) VALUES(%s, %s, %s, %s, %s)",
                 [_mealId, _active, _phone_number, _quantity, _table_number])
    mysql.connection.commit()
    cur8.close()
    return 'Succeess'


@app.route('/clientorder', methods=['POST'])
def post_clientorders():
    clientorderDetails = request.get_json()
    _orderId = clientorderDetails['order_id']
    _phoneNumber = clientorderDetails['phone_number']
    cur9 = mysql.connection.cursor()
    cur9.execute("INSERT INTO clientorders(order_id, phone_number) VALUES(%s, %s)", (_orderId, _phoneNumber))
    mysql.connection.commit()
    cur9.close()
    return 'Succeess'


@app.route('/kitchenorder', methods=['POST'])
def post_kitchenorders():
    clientorderDetails = request.get_json()
    _orderId = clientorderDetails['order_id']
    cur9 = mysql.connection.cursor()
    cur9.execute("INSERT INTO kitchenorders(order_id) VALUES(%s)", [_orderId])
    mysql.connection.commit()
    cur9.close()
    return 'Succeess'


@app.route('/restaurant', methods=['DELETE'])
def delete_restaurant():
    details = request.get_json()
    _id = details['id']
    cur12 = mysql.connection.cursor()
    cur12.execute("DELETE FROM restaurant WHERE id = %s", [_id])
    mysql.connection.commit()
    cur12.close()
    return "Deleted row successfully"


@app.route('/meal', methods=['DELETE'])
def delete_meal():
    details = request.get_json()
    _id = details['id']
    cur12 = mysql.connection.cursor()
    cur12.execute("DELETE FROM meal WHERE id = %s", [_id])
    mysql.connection.commit()
    cur12.close()
    return "Deleted row successfully"


@app.route('/order', methods=['DELETE'])
def delete_order():
    details = request.get_json()
    _id = details['id']
    cur12 = mysql.connection.cursor()
    cur12.execute("DELETE FROM orders WHERE id = %s", [_id])
    mysql.connection.commit()
    cur12.close()
    return "Deleted row successfully"


@app.route('/user', methods=['DELETE'])
def delete_user():
    details = request.get_json()
    _id = details['phone_number']
    cur12 = mysql.connection.cursor()
    cur12.execute("DELETE FROM users WHERE phone_number = %s", [_id])
    mysql.connection.commit()
    cur12.close()
    return "Deleted row successfully"


@app.route('/request', methods=['DELETE'])
def delete_request():
    details = request.get_json()
    _id = details['id']
    cur12 = mysql.connection.cursor()
    cur12.execute("DELETE FROM request WHERE id = %s", [_id])
    mysql.connection.commit()
    cur12.close()
    return "Deleted row successfully"


@app.route('/clientorder', methods=['DELETE'])
def delete_clientorder():
    details = request.get_json()
    _id = details['id']
    cur12 = mysql.connection.cursor()
    cur12.execute("DELETE FROM clientorders WHERE id = %s", [_id])
    mysql.connection.commit()
    cur12.close()
    return "Deleted row successfully"


@app.route('/kitchenorder', methods=['DELETE'])
def delete_kitchenorder():
    details = request.get_json()
    _id = details['id']
    cur12 = mysql.connection.cursor()
    cur12.execute("DELETE FROM kitchenorders WHERE id = %s", [_id])
    mysql.connection.commit()
    cur12.close()
    return "Deleted row successfully"


@app.route('/timer/<phone_number>', methods=['GET'])
def timer(phone_number):
    cur1 = mysql.connection.cursor()
    cur2 = mysql.connection.cursor()
    cur3 = mysql.connection.cursor()
    cur3.execute("SELECT COUNT(*) FROM kitchenorders")
    cur2.execute("SELECT COUNT(*) FROM orders WHERE phone_number = %s", [phone_number])
    cur1.execute("SELECT MAX(meal.prep_time) FROM orders INNER JOIN meal ON orders.meal_id = meal.id WHERE orders.phone_number = %s", [phone_number])
    data1 = cur1.fetchone()
    data2 = cur2.fetchone()
    data3 = cur3.fetchone()
    max1 = int(data1[0])
    numberOfKitchenOrders = int(data3[0])
    numberOfOrders = int(data2[0])
    number = numberOfKitchenOrders + numberOfOrders

    if numberOfKitchenOrders == 0:
        return str(max1)
    else:
        return str(round(number * max1 - math.sqrt(number * max1) * 2))


@app.route("/email", methods=['GET'])
def email():
    cur2 = mysql.connection.cursor()
    cur2.execute("SELECT email FROM users WHERE user_type = 'Client'")
    result = cur2.fetchall()
    emails = list(sum(result, ()))
    while '' in emails:
        emails.remove('')

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "emenu.noreply@gmail.com"  # Enter your address
    receiver_email = emails  # Enter receiver address
    password = "emenu123"
    meal_name = request.args.get('name')
    meal_description = request.args.get('description')
    meal_price = request.args.get('price')

    for email in receiver_email:
        message = MIMEText("Our new food is stuffed " + meal_description + ". The price is " + meal_price)
        message['Subject'] = 'Check out the new ' + meal_name
        message['From'] = sender_email
        message['To'] = email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, email, message.as_string())
    return "Success"


if __name__ == '__main__':
    app.run()
