#! python3

import requests, bs4, sys,webbrowser

#opens web pages
print ('Googling...')
res = requests.get('https://www.google.co.in/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()

#finds the elems from the source code
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com'+ linkElems[i].get('href'))