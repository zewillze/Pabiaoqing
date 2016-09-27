# -*- coding:utf-8 -*-
import urllib2
import lxml.html
import web
import json

from config import baseURL, bqDict


render = web.template.render("templates/")

# router
urls = (
    '/jgz/(.+)', 'jgzManager',
    '/sbd/(.+)', 'sbdManager'
)


class bqbManager:
    currentType = 'default'
    def GET(self, page):
        bq = bqDict[self.currentType]

        assert bq != ''

        if int(page) >= 2:
            mid = bq.bid + "_{0}".format(page)
        else:
            mid = bq.bid

        url = baseURL + mid + ".html"
        print url
        picUrls = readHTML(url, bq.xpath)
        def componentURL(uri):
            return "http://qq.yh31.com" + uri

        picUrls = map(componentURL, picUrls)
        # print(picUrls)
        # web.header('Content-Type', 'application/json')
        # return json.dumps(picUrls)
        return render.bq(pics=picUrls)



#金馆长
class jgzManager(bqbManager):
    currentType = "jgz"


#斯巴达
class sbdManager(bqbManager):
    currentType = "sbd"




def parseHTML(rs):
	try:
		return lxml.html.fromstring(rs)
	except Exception, e:
		raise e


def readHTML(url, htmlXpath):
	rq = urllib2.urlopen(url)
	rs = rq.read()

	return parseHTML(rs).xpath(htmlXpath)



if __name__ == '__main__':
	# readHTML(path["jgz"])
    app = web.application(urls, globals())
    app.run()
