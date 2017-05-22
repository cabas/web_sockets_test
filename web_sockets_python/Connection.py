# -*- coding: utf-8 -*-
import json
from websocket import create_connection
from Utils import Object
class Connection(object):
	def __init__(self, host):
		self.host = host

	def connect(self):
		print("Connecting to host", self.host)
		self.connection = create_connection(self.host)
	
	def disconnect(self):
		print("···connection closed···")
		self.connection.close() 

	def subscribe(self, channel):
		print("Connecting to channel", channel)
		self.channel = channel
		self.connection.send(self.__build_subscription_message())
		print("Server says: ", self.__parse_message(self.connection.recv()))

	def send_message(self, message):
		print("Sending message to server")
		self.connection.send(self.__build_message(message));
		print("Server says: ", self.__parse_message(self.connection.recv()))

	def __build_subscription_message(self):
		c = Object()
		d = Object()
		c.command = "subscribe"
		d.channel = self.channel
		c.identifier = json.dumps(d, default=lambda o: o.__dict__)
		return json.dumps(c, default=lambda o: o.__dict__)

	def __parse_message(self, message):
		parsed = json.loads(message)
		if (parsed is not None):
			return parsed["type"];
		else:
			return "error";


	def __build_message(self, message):
		c = Object()
		d = Object()
		c.channel = self.channel
		d.command = "message"
		d.identifier = json.dumps(c, default=lambda o: o.__dict__)
		d.data = message
		return json.dumps(d, default=lambda o: o.__dict__)



