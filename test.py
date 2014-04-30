from google.appengine.ext import ndb
import pagination

class Note(ndb.Model):
    text = ndb.StringProperty()
    published = ndb.BooleanProperty()
    creation_date = ndb.DateTimeProperty(auto_now_add=True)
  

def test:
    for i in range(3):
        n = Note("test true", True)
        n.put()
    for i in range(3):
        n = Note("test false", False)
        n.put()
    
    
    
