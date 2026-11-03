import socket

#1 параметры подключения
ip = '127.0.0.1'
port = 9001
end_point = (ip, port) # точка подключения


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # соединение с сервером
    client.connect(end_point)
    while True:
        # отправка
        client_message = input('Сообщение для сервера: ')
        client.send(client_message.encode(encoding='utf-8'))
        if client_message == 'stop_server':
            break
        # прием сообщения
        sever_message = client.recv(1024).decode(encoding='utf-8')
        print(f'Ответ сервера: [{sever_message}]')
        allow_continue = input('Продолжаем (y/n)?: ')
        if allow_continue == 'n':
            break

except BaseException as e:
    print(e)
finally:
    client.close()
    print('Сервер остановлен')