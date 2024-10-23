import socket
import threading

# Функция для получения сообщений с сервера
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # Если соединение разорвано
            print("Соединение с сервером потеряно.")
            client_socket.close()
            break

# Настройка клиента
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))  # Адрес сервера

    # Запуск потока для получения сообщений
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        # Отправка сообщений на сервер
        message = input("")
        client.send(message.encode('utf-8'))


start_client()