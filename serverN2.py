from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('172.19.0.4', 8002), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def rpc_node():
        F1 = "¡Alegría, hermoso destello de los dioses"
        s = xmlrpc.client.ServerProxy('http://172.19.0.2:8000')
        ans = s.node(F1)
        return ans

    server.register_function(rpc_node, 'node')
    server.serve_forever()
