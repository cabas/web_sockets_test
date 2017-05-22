# from actioncable.connection import Connection
# from actioncable.subscription import Subscription
# from actioncable.message import Message


# connection = Connection(url='ws://localhost:3000/cable', origin='http://0.0.0.0:3000')
# connection.connect()

# print (connection.connected)

# subscription = Subscription(connection, channel_name='TestChannel', identifier={'additional': 'params'})  # You don't have to provide the channel name in the identifier param.
# message = Message(action='update_something', data={'something': 'important'})

# subscription.send(message)

import json
import datetime
from Connection import Connection
from websocket import create_connection
from Utils import Object

def build_attendance_message(username):
	data = Object()
	data.action = "register_attendance"
	data.username = 'Esteban'
	data.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	return json.dumps(data, default=lambda o: o.__dict__)



# Definition for subscription



connection = Connection("ws://localhost:3000/cable")
connection.connect()
connection.subscribe("SomethingChannel")
connection.send_message(build_attendance_message('esteban@papinotas.com'))
connection.disconnect();


