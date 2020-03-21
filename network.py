from _thread import *
import socket
import ast

class Network():
	def __init__(self, server):
		self.data = None;
		self.server = server
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock_connect()
		start_new_thread(self.recv_data, ())

	def sock_connect(self):
		self.socket.connect(self.server)

	def recv_data(self):
		while True:
			data = self.socket.recv(2048)
			print("Received:", data.decode("utf-8"))
			reply = ast.literal_eval(data.decode("utf-8"))
			self.data = reply

	def get_data(self):
		data = self.data
		return data

	def send_data(self, data):
		self.socket.send(str.encode(data))