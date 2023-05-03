from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('172.19.0.9', 8007), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def rpc_node(sms):
        F6 = sms + "\nlo que la acerba costumbre había separado;"
        s = xmlrpc.client.ServerProxy('http://172.19.0.6:8004')
        ans = s.node(F6)
        return ans

    server.register_function(rpc_node, 'node')
    server.serve_forever()
