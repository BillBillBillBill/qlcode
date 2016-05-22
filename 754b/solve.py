import urllib2


if __name__ == '__main__':
    r = urllib2.Request("http://www.qlcoder.com/download/hugefile")
    r.add_header("Range", "bytes=12345678901-12345678999")
    ret = urllib2.urlopen(r)
    print ret.read()
