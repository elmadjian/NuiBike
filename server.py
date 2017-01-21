import socket, time

server_ip   = "192.168.1.242"
server_port = 5999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((server_ip, server_port))
text_so_far = ""
print("waiting...")

init = time.time()
while True:
    data, addr = sock.recvfrom(1024)
    #print(data)
    text_so_far += str(data) + "\n"
    if time.time() - init > 10.0:
        break

with open("log.txt", "w") as log:
    log.write(text_so_far)
