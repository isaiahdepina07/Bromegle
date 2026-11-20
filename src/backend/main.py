from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# serve index.html to user
@app.route('/')
def index():
    return render_template('index.html')

# serve a silly little test url
@app.route('/hello')
def helloWorld():
    return "<p>Hello, World! penis</p>"

@socketio.on('chat_message')
def handle_message(data):
    print(f"Python received: {data}")
    # Broadcast that message out to ALL connected browsers
    emit('new_message', data, broadcast=True)

@app.route('/api/ping')
def ping():
    return {"message": "Python received your request!", "status": "online"}

if __name__ == '__main__':
    socketio.run(app, debug=True)
