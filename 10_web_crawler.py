# A simple web crawler - still under development
# 简单的网络爬虫 - 还在开发中

import urllib2  # for get_page(url)


def crawler(seed):
    to_crawl = [seed]
    crawled = []
    while to_crawl:
        url = to_crawl.pop
        to_crawl = get_links_in_a_page(url, to_crawl, crawled)
        crawled.append(url)


def get_links_in_a_page(url, to_crawl, crawled):
    to_crawl = to_crawl
    page = get_page(url)
    start_index = page.find('<a href=')
    if start_index > -1:
        while start_index > -1:
            page = page[start_index + 1:]
            start_index = page.find('"')
            end_index = page[start_index + 1:].find('"')
            new_url = page[start_index: end_index + 1]
            if check_if_crawled(new_url, crawled):
                to_crawl.append(new_url)
        return to_crawl
    else:
        return to_crawl


def get_page(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    page = response.read()
    return page

def check_if_crawled(new_url, crawled):
    if new_url in crawled:
        return True
    else:
        return False

