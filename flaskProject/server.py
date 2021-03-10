import socket
import time

host = socket.gethostbyname(socket.gethostname()) #выдает наш родной ip, удобнее, чем прописывать при каждой смене
port = 9090 #удобный порт, не требующий прав администратора
escaping = False #выходим из цикла
clients_adress = [] #принимает адреса входящие на сервер
protocols = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #tcp & ip протоколы
protocols.bind((host, port)) #запускаем хост и порт через протоколы tcp/ip
print("[Started]")
while not escaping:
    try:
        data, addr = protocols.recvfrom(1024) #data - сообщения, addr - адрес пользователя, recvfrom - вызов для приняти data/addr с определенным кол-вом байт
        if addr not in clients_adress:
            clients_adress.append(addr) #если адрес не в клиенте, мы эту проблему решаем(нужно для добавления новых клиентов)
        client_time = time.strftime("%Y-%m-%d.%H.%M,%S", time.localtime()) #для временного лога сообщений и входа/выхода клиента
        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + client_time + "]/", end="") #вывод сообщений хоста
        print(data.decode("utf-8")) #декодируем сообщения
        for client in clients_adress:
            if addr != client:
                protocols.sendto(data, client) #проверка для того, чтобы клиент не видел свои сообщения (для проверки работоспособности чата, в дальнейшем можно убрать)
    except:
        print("\n[Stopped]")
        escaping = True
protocols.close()
