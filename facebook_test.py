import fb, json, urllib2
from config import token
print token
facebook=fb.graph.api(token)
userNode =facebook.get_object(cat="single", id="me", fields=['friends', 'name', 'email', 'likes', 'education'] )
print  userNode


