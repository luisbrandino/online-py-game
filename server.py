from _thread import *
import socket
import json

host = "0.0.0.0"
port = 4444

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)

def client_thread(obj):
	while True:
		data = obj.recv(2048)

		if not data:
			print("Client disconnected")
			break

		for client in clients:
			if client != obj:
				print("Sending:", data.decode("utf-8"))
				client.sendall(data)

def main():

	while True:
		conn, addr = s.accept()
		print("Connection received from " + addr[0])
		clients.append(conn)

		start_new_thread(client_thread, (conn,))

main()