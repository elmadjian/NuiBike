import socket, time, re

server_ip   = "192.168.1.242"
server_port = 5999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((server_ip, server_port))
text_so_far = "time\t x\t y\t z\n"
prog = re.compile(r"x:(.+)\ y:(.+)\ z:(.+)")
print("waiting...")

init = time.time()
while True:
    data, addr = sock.recvfrom(1024)
    data = data.decode("utf-8")
    m = prog.match(data)
    data = m.group(1) + "\t" + m.group(2) + "\t" + m.group(3)
    print(data)
    elapsed = time.time() - init
    text_so_far += str(elapsed) + "\t" + data + "\n"
    if elapsed > 10.0:
        break

with open("log.txt", "w") as log:
    log.write(text_so_far)
