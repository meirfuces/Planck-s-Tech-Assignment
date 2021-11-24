from flask import Flask, jsonify
import controller

app = Flask(__name__)


@app.route('/drinks')
def get_all_drinks():
    return jsonify(controller.get_drinks())

@app.route('/drink/<id>')
def get_drink_by_id(id):
    return jsonify(controller.get_drink(id))

@app.route('/pizza/<id>')
def get_pizza_by_id(id):
    return jsonify(controller.get_pizza(id))


@app.route('/pizzas')
def get_all_pi():
    return jsonify(controller.get_pizzas())


@app.route('/dessert/<id>')
def get_dessert_by_id(id):
    return jsonify(controller.get_desert(id))


@app.route('/desserts')
def get_all_desserts():
    print('hey')
    return jsonify(controller.get_desserts())