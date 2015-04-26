import fb, urllib
from config import token

#print token
facebook=fb.graph.api(token)
userNode =facebook.get_object(cat="single", id="me", fields=['friends'] )
#print userNode
count = 0
for f in userNode['friends']['data']:
  name = f['name']
  pid = f['id']
  p_url = "https://graph.facebook.com/"+pid+"/picture"
  print p_url
  count+=1
  img = open('images/'+name+"_"+pid+".jpg", "wb")
  img.write(urllib.urlopen(p_url).read())
  img.close()
  print "Profile pic of " + name + " downloaded "

print count
