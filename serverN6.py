from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('172.19.0.8', 8006), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def rpc_node(sms):
        return sms + "allí donde tu suave ala se posa."

    server.register_function(rpc_node, 'node')
    server.serve_forever()
