from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('172.19.0.3', 8001), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def rpc_node(sms):
        F4 = sms + "\ndiosa celestial, en tu santuario.\n"
        s = xmlrpc.client.ServerProxy('http://172.19.0.5:8003')
        ans = s.node(F4)
        return ans

    server.register_function(rpc_node, 'node')
    server.serve_forever()
