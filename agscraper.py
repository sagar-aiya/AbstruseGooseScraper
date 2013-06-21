import urllib2
from BeautifulSoup import BeautifulSoup

def saveim(url,filename):
    pic = urllib2.urlopen(url).read()
    print('Saving file: '+filename)
    out = open(filename,"wb")
    out.write(pic)
    out.close()


imageNo = 25
end = False
notfoundcount = 0;
while not end:
    url = 'http://abstrusegoose.com/'+str(imageNo)
    data = urllib2.urlopen(url).read()
    if data != 'Page does not exist':
        soup = BeautifulSoup(urllib2.urlopen(url).read())
        image = soup.find("section").find("img")
        imageurl = image["src"]
        filename = "AG-"+str(imageNo)+" "+image["alt"]+str(imageurl[-4:])
        saveim(imageurl,filename)
        imageNo += 1
        notfoundcount = 0
    else:
        notfoundcount+=1
        if notfoundcount > 3:
            end = True
        else:
            imageNo += 1


        
    




    
    
    
