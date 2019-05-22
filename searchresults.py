#use idle 3.4.4
import webbrowser, bs4, requests, re, time
import urllib
import urllib.request




class handle:
    def __init__(self, searchquery):
        self.searchquery = str(searchquery)
        self.res = requests.get('http://www.google.com/search?q='+self.searchquery)
        self.res.raise_for_status()
        self.soup = bs4.BeautifulSoup(self.res.text, "html.parser")
        self.linkElem = self.soup.select('.r a')

    def execu(self):
        return min(5, len(self.linkElem))



class manageurl:
    def __init__(self):
        
        self.t = []
        self.pas = []
        self.us = []
        self.newurl = []
        self.finalurl = []
    
        
    def sepurl(self):
        for x in self.us:    
            t = (x.replace(str('/url?q='), ""))
            self.newurl.append(t)
    
    
        first = self.newurl[1]

        self.newurl.remove(first)

        for x in self.newurl:
            self.pas.append(x)

        
        for x in self.pas:
            spli = x.split('&')
            self.t.append(spli[0])


    def __str__(self):
        return '{}'.format(self.t)




def main():
    #make input string
    hacker = ('mikeyPPPP')#enter search here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    manage = manageurl()
    hand = handle(hacker)
    numOpen = hand.execu()
    
    for i in range(numOpen):
        #opens the browser
        
        #webbrowser.open('http://www.google.com' + hand.linkElem[i].get('href'))
        #time.sleep(1)

        manage.us.append(hand.linkElem[i].get('href'))
    manage.sepurl()
    for x in manage.t:
        print(x)
    

        
        

if __name__=="__main__":
    main()

#by mikeyPPPP
