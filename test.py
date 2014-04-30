from google.appengine.ext import ndb
from pagination import return_query_page

class Note(ndb.Model):
    text = ndb.StringProperty()
    published = ndb.BooleanProperty()
    creation_date = ndb.DateTimeProperty(auto_now_add=True)
  

def test:
    n = []
    n.append(Note("test1", True))
    n.append(Note("test2", True))
    n.append(Note("test3", False))
    n.append(Note("test4", True))
    n.append(Note("test5", True))

    n.put_multi(n)
    
    # usually this function is included as a class method inside a Model so cls is always the class calling
    results, prev_b, next_b = return_query_page(Note, 1, None, None, {'published': True}, {'creation_date': '-'})
    assert results[0].text == "test1'
    
    #calling next page
    results, prev_b, next_b = return_query_page(Note, 1, next_b, None, {'published': True}, {'creation_date': '-'})
    assert results[0].text == "test2'
    
    #calling next page
    results, prev_b, next_b = return_query_page(Note, 1, next_b, None, {'published': True}, {'creation_date': '-'})
    assert results[0].text == "test4'
    
    #calling prev page
    results, prev_b, next_b = return_query_page(Note, 1, prev_b, True, {'published': True}, {'creation_date': '-'})
    assert results[0].text == "test2'
    
    #calling prev page
    results, prev_b, next_b = return_query_page(Note, 1, prev_b, True, {'published': True}, {'creation_date': '-'})
    assert results[0].text == "test1'
