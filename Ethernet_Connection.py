import socket

HOST = '169.254.190.208'
PORT = 12345


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print('Подключено к:', HOST)

            while True:
                data = input('Введите число: ')
                s.sendall(data.encode())

                response = s.recv(1024)

                print('Ответ от Raspberry Pi:', response.decode())

        except ConnectionRefusedError:
            print('Не удалось подключиться к', HOST)

        finally:
            s.close()