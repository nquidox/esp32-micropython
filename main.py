import socket
from machine import Pin
from machine import I2C
import bme280

# назначаем пины для датчика
i2c = I2C(scl = Pin(22), sda = Pin(21), freq = 10000)

# определяем серверный сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# разрешаем повторного его использовать
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# делаем привязку к адресу и порту (ip выставлен статическим на роутере)
addr = socket.getaddrinfo('192.168.1.100', 9000)[0][-1]
server_socket.bind(addr)

# запускаем ожидание подключений
server_socket.listen(1)


while True:
    # принимаем подключение
    client_socket, addr = server_socket.accept()
    print("Connection from: ", addr)

    while True:
        request = client_socket.recv(4096)

        if not request:
            # если нет запроса, то прекращаем цикл
            break
        else:
            # если есть запрос, отправляем ответ
            #опрос датчика
            bme = bme280.BME280(i2c = i2c)
            temp = bme.temperature
            humi = bme.humidity
            pres = bme.pressure

            response = ("Temperature: " + temp + "\n" + "Humidity: " + humi + "\n" + "Pressure: " + pres).encode()
            client_socket.send(response)
