from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' # super secret
socketio = SocketIO(app)

# Return index.html
@app.route("/")
def index():
    """Return HTML"""
    return render_template('index.html')
    #pass

# Reserved event: Connect
@socketio.on('connect')
def test_connect():
    """Gets fired on any client-server connection"""
    print("SocketIO: Connected:", request.sid)

# Reserved event: Disconnect
@socketio.on('disconnect')
def test_disconnect():
    """Gets fired on any client-server disconnect"""
    print('SocketIO: Disconnected:', request.sid)

# Custom event: Any message from client
@socketio.on('message_from_client') #  Event name is crucial.
def handle_my_custom_event(json_data):
    """Use this function to receive events from the client.
       A JSON is always sent along and it hold all necessary data."""
    print("SocketIO: Received a message and forwarding to MessageHandler.")

# Emit events to one client as response
def emit_event(event_name, json_data):
    """Use this function to emit events to the client which sent data.
       A JSON is always sent along and it hold all necessary data.
       This is not a broadcasting to all clients!"""
    print("SocketIO: Sending to one client as response: ",event_name)

# Emit events to all clients as broadcast
def emit_event_to_all_clients(event_name, json_data):
    """Use this function to emit events to all clients as broadcast.
       A JSON is always sent along and it hold all necessary data."""
    print("SocketIO: Sending to all clients: ",event_name)

# ALL EVENTS ARE PROCESSED HERE --------------------------------
def process_message(session_id, json_data):
    """Processes each message type defined in "type" in JSON."""
    print("PROCESSING: Event Type:", json.loads(json_data)["type"])

    data = json.loads(json_data)

    if data["type"] == "echo":
        pass
    elif data["type"] == "":
        pass
#----------------------------------------------------------------

# Boilerplate starts SocketIO instead of standard flask.
if __name__ == '__main__':
    socketio.run(app)
    # socketio.run(app, host="192.168.178.23", port="5001")


"""
Notes:
send() and emit() is used in client context for answering.
socketio.send() and socketio.emit() is used when server starts communication.

json.loads() --> string to json
json.dumps() --> json to string

request.sid --> unique session ID for each client connection
"""
