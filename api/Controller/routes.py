from .routesfunc import *

def setuproute(app, call):
    @app.route('/test/',        ['OPTIONS', 'POST', 'GET'], lambda x = None: call([])                     )
    @app.route('/call/',    	['OPTIONS', 'POST'],        lambda x = None: call([check_method, call_sec])   )
    def base():
        return
