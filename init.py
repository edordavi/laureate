import webapp2
import urllib2
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'webpage/index.html') 
        self.response.out.write(template.render(path, {}))

class getYouTube(webapp2.RequestHandler):
    
    def get(self):
        qry = self.request.get("q",default_value="")
        
        url='https://www.googleapis.com/youtube/v3/search?part=id,snippet&channelId=UCvS6-K6Ydmb4gH-kim3AmjA&key=AIzaSyB_bNlNDEGBs5spVySYQuWpb6g1CIGSnbo&q=' + qry
        youtube = urllib2.urlopen(url)
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(youtube.read())

application = webapp2.WSGIApplication([('/', MainPage),('/test', getYouTube),], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
