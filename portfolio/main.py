import webapp2
import os
import logging
# import jinja2 here
import jinja2
# import regular expression
import re

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# the single handler for all the pages except login.html and successlogin.html 
class IndexHandler(webapp2.RequestHandler):
    def get(self):
# using self.request.path here to get the url from the users and direct them to the page they request
        try:
            title = re.findall('/(\S*).html', self.request.path)
            title = title[0].upper()
            template = JINJA_ENVIRONMENT.get_template('templates%s'%self.request.path)
            self.response.write(template.render({'title': title}))
# if the users fail to enter a proper url, they will go to the homepage instead
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/portfolio.html')
            self.response.write(template.render({'title' : 'portfolio'}))
# handler that handles user inputs and provide feedback
# class LoginHandler(webapp2.RequestHandler):
#     def get(self):
#         template = JINJA_ENVIRONMENT.get_template('templates/login.html')
#         self.response.write(template.render({'title' : 'LOG IN'}))
#     def post(self):
#         username = self.request.get('name')
#         password = self.request.get('pw')
#         if username != 'Colleen' or password != 'pass':
# # wrong inputs are logged here
#             logging.info('User error combination: '+ username + ',' + password)
#             msg = 'Bad credentials. Try again.'
#             template = JINJA_ENVIRONMENT.get_template('templates/login.html')
#             self.response.write(template.render({'message': msg}))
#         else:
#             template = JINJA_ENVIRONMENT.get_template('templates/successlogin.html')
#             self.response.write(template.render({'title': 'Logged In...'}))
# list of url and corresponding handlers
app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/portfolio.html', IndexHandler),
    ('/contactme.html', IndexHandler),
    ('/design.html', IndexHandler),
    ('/research.html', IndexHandler),
    ('/aboutme.html', IndexHandler),
    ('/resume.html', IndexHandler)
], debug=True)
