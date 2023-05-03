from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('172.19.0.5', 8003), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def rpc_node(sms):
        F5 = sms + "\nTu hechizo une de nuevo"
        s = xmlrpc.client.ServerProxy('http://172.19.0.9:8007')
        ans = s.node(F5)
        return ans

    server.register_function(rpc_node, 'node')
    server.serve_forever()
