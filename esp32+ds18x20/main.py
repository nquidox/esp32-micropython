import socket
from machine import Pin
import onewire
import ds18x20

# назначаем пины для датчика
ds_sensor = ds18x20.DS18X20(onewire.OneWire(Pin(4)))

# определяем серверный сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# делаем привязку к адресу и порту (ip выставлен статическим на роутере)
server_socket.bind(('192.168.1.101', 9000))

# запускаем ожидание подключений
server_socket.listen(1)

while True:
    # принимаем подключение
    client_socket, addr = server_socket.accept()
    client_socket.settimeout(10.0)

    while True:
        request = client_socket.recv(4096)

        if not request:
            # если нет запроса, то прекращаем цикл
            break
        else:
            # если есть запрос, отправляем ответ
            # опрос датчика
            temp = "0"
            roms = ds_sensor.scan()
            ds_sensor.convert_temp()
            for rom in roms:
               temp = ds_sensor.read_temp(rom)
            response = str(temp).encode()
            client_socket.send(response)

