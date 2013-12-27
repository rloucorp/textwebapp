from werkzeug.wrappers import Request, Response
from werkzeug.debug import DebuggedApplication

@Request.application
def app(request):
	print request.path
   	print request.headers
   	return Response("hello, world!")



from werkzeug.serving import run_simple
run_simple("localhost", 4001, app)
