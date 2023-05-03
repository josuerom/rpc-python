from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('172.19.0.6', 8004), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def rpc_node(sms):
        F7 = sms + "\ntodos los hombres vuelven a ser hermanos\n"
        s = xmlrpc.client.ServerProxy('http://172.19.0.8:8006')
        ans = s.node(F7)
        return ans

    server.register_function(rpc_node, 'node')
    server.serve_forever()
