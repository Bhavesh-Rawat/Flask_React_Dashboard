from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import sqlite3

app = Flask(__name__)
socketio = SocketIO(app)

def get_db_connection():
    conn = sqlite3.connect('dishes.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/dishes', methods=['GET'])
def get_dishes():
    conn = get_db_connection()
    dishes = conn.execute('SELECT * FROM dishes').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in dishes])

@app.route('/api/dishes/<int:dish_id>/toggle', methods=['POST'])
def toggle_is_published(dish_id):
    conn = get_db_connection()
    dish = conn.execute('SELECT * FROM dishes WHERE dishId = ?', (dish_id,)).fetchone()
    
    if dish is None:
        return jsonify({'error': 'Dish not found'}), 404
    
    new_status = not dish['isPublished']
    conn.execute('UPDATE dishes SET isPublished = ? WHERE dishId = ?', (new_status, dish_id))
    conn.commit()
    conn.close()
    
    # Emit the change to all connected clients
    socketio.emit('update', {'dishId': dish_id, 'isPublished': new_status})

    return jsonify({'message': 'Status updated', 'isPublished': new_status})

if __name__ == '__main__':
    print(app.url_map)
    socketio.run(app, debug=True)
