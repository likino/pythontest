# -*-coding: utf-8 -*-
import urllib2
import urllib
content urllib2.urlopen('http://www.verycd.com/').read()
postdata = urllib.urlencode({
	'username':'xxxx',
	'password':'xxxx',
	'continue':'http://www.verycd.com/',
	'fk':fk,
	'login submit':'登录'
})

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
}

req = urllib2.Request(
	url = 'http://secure.verycd.com/signin?error_code=emptyInput&continue=http://www.verycd.com/',
	data = postdata
	headers = headers
)
result = urllib2.urlopen(req).read()

