import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='Wolfer3779', db='searchtest')
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute("""SELECT url FROM search""")
newpages=cur.fetchall()
#newpages={'http://uppit.us/'}
siteString = ', '.join(d['url'] for d in newpages)
sitesList = siteString.split(', ')
def indexed(url):
	if(url in sitesList):
		return True
	else:
		return False
def crawl(pages, depth=1):
	try:
		requesteddesc, requestedkeys, title, text, tag = "", "", "", "", ""
		for i in range(depth):
			
			for page in pages:
				try:
					c=urllib.request.urlopen(page)
				except:
					print("Couldnt open " + str(page))
					continue
				soup=BeautifulSoup(c.read())
				links=soup('a')
				for link in links:
					if('href' in dict(link.attrs)):
						url=urljoin(page, link['href'])
						if url.find("'")!=-1: continue
						url=url.split('#')[0]
						url=url.replace('"', '\"')
						url=url.replace("'", "\'")
						if(indexed(url)==False):
							text=" "+soup.get_text()
							text=text.replace('"', '\"')
							text=text.replace("'", "\'")
							text=text.replace("\n", " ")
							title=soup.title.string
							title=title.replace('"', '\"')
							title=title.replace("'", "\'")
							title=title.replace("\n", " ")
							sitesList.append(url)
							tag = soup.find_all('meta')
							for metag in range(len(tag)):
								try:
									metag_name = tag[metag]['name']
									if(metag_name == 'keywords'):
										requestedkeys = tag[metag]['content']
										requestedkeys = requestedkeys.replace(",", "")
										requestedkeys=requestedkeys.replace('"', '\"')
										requestedkeys=requestedkeys.replace("'", "\'")
										requestedkeys=requestedkeys.replace("\n", " ")
									if(metag_name == 'description'):
										requesteddesc = tag[metag]['content']
										requesteddesc=requesteddesc.replace('"', '\"')
										requesteddesc=requesteddesc.replace("'", "\'")
										requesteddesc=requesteddesc.replace("\n", " ")
								except:
									continue
							print("Url Found")
							command = '''INSERT INTO search (title, description, url, keywords) VALUES ("''' + title + '''","''' + requesteddesc + '''","''' + url + '''","''' + requestedkeys + " " + url + " " + title + " " + requesteddesc + '''")'''
							try:
								if(cur.execute(command)):
									print(url)
							except:
								print("Could parse Url")
							#print(command)
							requesteddesc, requestedkeys, title, text, tag = "", "", "", "", ""
	except:
		pass
						

crawl(sitesList)
'''

tag = soup.find_all('meta')
for metag in range(len(tag)):
	metag_name = tag[metag]['name']
	if(metag_name == 'keywords'):
		requestedkeys = tag[metag]['content']
	elif(metag_name == 'description'):
		requesteddesc = tag[metag]['content']


>>> conn = pymysql.connect(host='localhost', user='root', passwd='Wolfer3779', db='searchengine')
>>> cur = conn.cursor()
>>> cur.execute("""SELECT url FROM search""")
4
>>> newpages=cur.fetchall()
>>> #newpages={'http://uppit.us/'}
... 
>>> siteString = ', '.join(d['url'] for d in sites)
>>> sitesList = siteString.split(', ')
>>> sitesLists = [', '.join(sitesList[n:]) for n in range(len(sitesList))]
>>> sitesLists
['http://socialno.de, http://[fc3a:956e:4b69:1c1e:5ebc:11a5:3e71:3e7e], http://[fcb4:bcb2:1630:bfe3:b4c4:f99b:98b:eca4]/cgi/ansearch.py , http://urlcloud.net', 'http://[fc3a:956e:4b69:1c1e:5ebc:11a5:3e71:3e7e], http://[fcb4:bcb2:1630:bfe3:b4c4:f99b:98b:eca4]/cgi/ansearch.py , http://urlcloud.net', 'http://[fcb4:bcb2:1630:bfe3:b4c4:f99b:98b:eca4]/cgi/ansearch.py , http://urlcloud.net', 'http://urlcloud.net']
>>> sitesList
['http://socialno.de', 'http://[fc3a:956e:4b69:1c1e:5ebc:11a5:3e71:3e7e]', 'http://[fcb4:bcb2:1630:bfe3:b4c4:f99b:98b:eca4]/cgi/ansearch.py ', 'http://urlcloud.net']


# A list of words that every site has. Why bother saveing space for them?
ignorewords=set(['the','of','to','and','a','in','is','it', 'be', 'beeing', 'been', 'had', 'has', 'will', 'hyperboria'])
def crawl(self,pages,depth=2):

  for i in range(depth):

    newpages=set( )

    for page in pages:

      try:

        c=urllib.urlopen(page)

      except:

        print("Could not open %s" % page)

        continue

      soup=BeautifulSoup(c.read( ))

      self.addtoindex(page,soup)



      links=soup('a')

      for link in links:

        if ('href' in dict(link.attrs)):

          url=urljoin(page,link['href'])

          if url.find("'")!=-1: continue

          url=url.split('#')[0] # remove location portion

          if url[0:4]=='http' and not self.isindexed(url):

            newpages.add(url)

          linkText=self.gettextonly(link)

          self.addlinkref(page,url,linkText)



        self.dbcommit( )



        pages=newpages
pagelist=['http://kiwitobes.com/wiki/Perl.html']
crawl(['http://google.com'])
'''