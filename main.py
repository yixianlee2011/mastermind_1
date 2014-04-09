"""`main` is the top level module for your Bottle application.

Loads the Bottle framework and adds a custom error
handler.
"""

# import the Bottle framework
from bottle import Bottle
from google.appengine.api import users
from bottle import route, request, run, redirect
import json
import urllib
from google.appengine.api import urlfetch
from google.appengine.ext import ndb

def verify_service(requestJSON, url):
      params = urllib.urlencode({'jsonrequest': requestJSON})
      print params
      deadline = 120
    
      result = urlfetch.fetch(url=url,
                                payload=params,
                                method=urlfetch.POST,
                                deadline=deadline,
                                headers={'Content-Type': 'application/x-www-form-urlencoded'})
      return result.content


# Run the Bottle wsgi application. We don't need to call run() since our
# application is embedded within an App Engine WSGI application server.
bottle = Bottle()

'''
@bottle.route('/api/get_bots')
def use_verify_service():
  return "I return this"
  
  bots = Bot.query().fetch(100)
  result = []
  for bot in bots:
    result.append(bot.to_dict())
  return json.dumps(result) 
'''
@bottle.error(404)
def error_404(error):
  """Return a custom 404 error."""
  return 'Sorry, Nothing at this URL.'

@bottle.post('/api/verify_service_m')
def verify_service_m():
  bots_code_m = request.forms.get("bots_code")
  #syntax testing
  bots_code_m+="function aguess(a,b,c,d){ return [1,1] }";
  tests_m = request.forms.get("tests");
  d = {"tests":tests_m, "solution":bots_code_m}
  url = "http://162.222.183.53/js"
  requestJSON = json.dumps(d)
  result = verify_service(requestJSON,url)
  print result 
  return result