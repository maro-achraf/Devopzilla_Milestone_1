from threading import active_count
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/maro_achraf/Documents/Devopzilla_Milestone_1/ItemsAndOrders.db'

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    cost = db.Column(db.Integer)
    avq = db.Column(db.Integer)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer)
    cart_id = db.Column(db.String(50))
    req = db.Column(db.Integer)
    total = db.Column(db.Integer)

db.create_all()

@app.route('/item/<public_id>', methods=['GET'])
def get_item(current_item, public_id):

    item = Item.query.filter_by(id=public_id).first()
    order = Order.query.filter_by(id=public_id, item_id=current_item.id).first()
    if not Item:
        return jsonify({'message' : 'No item found!'})

    item_data = {}
    item_data['id'] = Item.id
    item_data['name'] = Item.name
    item_data['cost'] = Item.cost
    item_data['avq'] = Item.avq

    return jsonify({'item' : item_data})

@app.route('/item', methods=['POST'])
def create_user(current_item):
    data = request.get_json()
    new_item = Item(public_id=data['publec_id'], name=data['name'], cost=data['cost'], avq=['avq'])
    db.session.add(new_item)
    db.session.commit()

    return jsonify({'message' : 'New user created!'})

@app.route('/item/<public_id>', methods=['DELETE'])
def delete_user(current_item, public_id):
    item = Item.query.filter_by(public_id=public_id).first()

    if not item:
        return jsonify({'message' : 'No item found!'})

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message' : 'The user has been deleted!'})


    todos = Todo.query.filter_by(user_id=current_user.id).all()

    output = []

    for todo in todos:
        todo_data = {}
        todo_data['id'] = todo.id
        todo_data['text'] = todo.text
        todo_data['complete'] = todo.complete
        output.append(todo_data)

    return jsonify({'todos' : output})

@app.route('/order/<order_id>', methods=['GET'])
def get_order(current_item, order_id):
    order = Order.query.filter_by(id=order_id, item_id=current_item.id).first()

    if not order:
        return jsonify({'message' : 'No order found!'})

    order_data = {}
    order_data['id'] = order.id
    order_data['cart_id'] = order.cart_id
    order_data['req'] = order.req
    order_data['total'] = order.total

    return jsonify(order_data)

@app.route('/order', methods=['POST'])
def create_order(current_item):
    data = request.get_json()
    new_order = Order(cart_id=data['cart_id'],item_id=current_item.id,req =data['req'],total= data['total'])
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message' : "Order created!"})

@app.route('/order/<order_id>', methods=['DELETE'])
def delete_todo(current_item, order_id):
    order = Order.query.filter_by(id=order_id, item_id=current_item.id).first()

    if not order:
        return jsonify({'message' : 'No order found!'})

    db.session.delete(order)
    db.session.commit()

    return jsonify({'message' : 'Todo item deleted!'})

if __name__ == '__main__':
    app.run(debug=True)