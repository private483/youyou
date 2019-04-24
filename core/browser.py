import time
import random
import cookielib
import mechanize

class Browser(object):
 def __init__(self):
  self.br = None

 def createBrowser(self):
  br = mechanize.Browser()
  br.set_handle_equiv(True)
  br.set_handle_referer(True)
  br.set_handle_robots(False)
  br.set_handle_refresh(False)
  br.set_cookiejar(cookielib.LWPCookieJar())
  br.addheaders=[('User-agent',self.useragent())]
  br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
  self.br = br

 def deleteBrowser(self):
  self.br.close()
  del self.br

 def getIp(self):
  try:
   return self.br.open('http://wtfismyip.com/text',timeout=35.0).read().replace('\n','')
  except KeyboardInterrupt:self.kill()
  except:return

 def watch(self):
  if not self.alive:
   return

  try:
   self.display()
   html = self.br.open(self.url,timeout=35.0)

   sleepTime = random.randint(self.minWatch,self.maxWatch)
   for _ in range(sleepTime):
    if not self.alive:break
    time.sleep(1)

   return html.read()
  except:return

 def useragent(self):
  useragents = [
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
           'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
           'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']
  return random.choice(useragents)
