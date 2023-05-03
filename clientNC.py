import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://172.19.0.4:8002') # Manual connection to node 2
result = s.node()
print("HIMNO A LA ALEGRÍA DE LUDWING VAN BEETHOVEN:\n")
print(str(result))
