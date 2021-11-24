import flask
from flask import Flask, jsonify, request, render_template
import controller,GetDb
import threading


# def job():
#     print ("I'm working...")
#     return
#
#
# schedule.every().minute.at(":17").do(job)
# schedule.every().day.at("01:00").do(job,'It is 01:00')
#
# while True:
#     schedule.run_pending()
#     time.sleep(60) # wait one minute

t1 = threading.Thread(target=GetDb.update_data(), args=(10,))
t1.run()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Plank Task </h1>" \
           "<p>meir fuchs </p>"


# GET /drinks - Returns the id, name, description and price of all drinks
@app.route('/drinks')
def get_all_drinks():
    return jsonify(controller.get_drinks())


# GET /drink/<id> - Returns id, name, description and price of a drink
@app.route('/drink/<id>')
def get_drink_by_id(id):
    return jsonify(controller.get_drink(id))


# GET /pizzas - Returns the id, name, description and price of all pizzas
@app.route('/pizzas')
def get_all_pi():
    return jsonify(controller.get_pizzas())


# GET /pizza/<id> - Returns id, name, description and price of a pizza
@app.route('/pizza/<id>')
def get_pizza_by_id(id):
    return jsonify(controller.get_pizza(id))


# GET /desserts - Returns the id, name, description and price of all desserts
@app.route('/desserts')
def get_all_desserts():
    return jsonify(controller.get_desserts())


# GET /dessert/<id> - Returns id, name, description and price of a dessert
@app.route('/dessert/<id>')
def get_dessert_by_id(id):
    return jsonify(controller.get_desert(id))


# POST /order - receives an order and returns its total price.
@app.route('/order', methods = ['POST'])
def order():
    if flask.request.method == 'POST':
        data = request.get_json()

        return jsonify(controller.price(data))
    else:
        return "<p>order </p>"
    # print(request.form)


if __name__ == '__main__':
    app.run()