from debug import *
from zoodb import *
import rpclib

def login(username, password):
    ## Fill in code here.
    with rpclib.client_connect('/authsvc/sock') as c:
        kwargs = {'username':username,'password':password}
        ret = c.call('login',**kwargs)
	#ret = c.call('login', username=username, password=password)
        return ret

def register(username, password):
    ## Fill in code here.
    with rpclib.client_connect('/authsvc/sock') as c:
        kwargs = {'username':username,'password':password}
        print "register kwargs=%s" % kwargs
        ret = c.call('register',**kwargs)
	#ret = c.call('register', username=username, password=password)
        return ret

def check_token(username, token):
    ## Fill in code here.
    with rpclib.client_connect('/authsvc/sock') as c:
        kwargs = {'username':username,'token':token}
        ret = c.call('check_token',**kwargs)
	#ret = c.call('check_token', username=username, token=token)
        return ret
