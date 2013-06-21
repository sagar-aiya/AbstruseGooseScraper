import urllib2
from BeautifulSoup import BeautifulSoup

def saveim(url,filename):
    try:
        pic = urllib2.urlopen(url).read()
        print('Saving file: '+filename)
        out = open(filename,"wb")
        out.write(pic)
        out.close()
    except:
        print("Could not save file: "+filename);


imageNo = 120
end = False
notfoundcount = 0;
while not end:
    url = 'http://abstrusegoose.com/'+str(imageNo)
    try:
        data = urllib2.urlopen(url).read()
        if data != 'Page does not exist':
            soup = BeautifulSoup(urllib2.urlopen(url).read())
            image = soup.find("section").find("img")
            imageurl = image["src"]
            try:
                name = image["alt"]
            except KeyError:
                try:
                    name = image["title"]
                except:
                    name = " "
        
            filename = "AG-"+str(imageNo)+" "+name+str(imageurl[-4:])
            saveim(imageurl,filename)
            imageNo += 1
            notfoundcount = 0
        else:
            notfoundcount+=1
            if notfoundcount > 3:
                end = True
            else:
                imageNo += 1
    except:
        notfoundcount += 1
        imageNo += 1
