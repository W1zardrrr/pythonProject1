import socket
import threading

# Список подключенных клиентов
clients = []

# Отправка сообщения всем клиентам
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # В случае ошибки удаляем клиента из списка
                clients.remove(client)

# Обработка подключения клиента
def handle_client(client_socket):
    while True:
        try:
            # Получаем сообщение от клиента
            message = client_socket.recv(1024)
            # Передаем его всем остальным
            broadcast(message, client_socket)
        except:
            # Если что-то пошло не так, удаляем клиента и завершаем поток
            clients.remove(client_socket)
            client_socket.close()
            break


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))  # Хост и порт
    server.listen()

    print("Сервер запущен и ждет подключений...")

    while True:

        client_socket, client_address = server.accept()
        print(f"Подключен клиент: {client_address}")
        clients.append(client_socket)


        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

start_server()