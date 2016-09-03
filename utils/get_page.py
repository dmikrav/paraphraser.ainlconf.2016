import urllib2
response = urllib2.urlopen('https://ru.wiktionary.org/wiki/%D1%80%D0%B0%D0%B7%D0%BB%D1%83%D0%BA%D0%B0')
html = response.read()
print html
