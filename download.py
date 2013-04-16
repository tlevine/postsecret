#!/usr/bin/env python2
from os.path import join as path
from lxml.html import fromstring
from cache import get

def main(datestamp):
    'Download given a datestamp.'
    # Set the directories.
    index_dir = path('downloads', 'index', datestamp)
    image_dir = path('downloads', 'images')

    # Download the index.
    index = get('http://www.postsecret.com/', cachedir = index_dir)

    # Download the new images.
    html = fromstring(index.read())
    srcs = html.xpath('//img/@src')
    for src in srcs:
        get(src, cachedir = image_dir)

if __name__ == '__main__':
    import datetime
    main(datetime.date.today().isoformat())
