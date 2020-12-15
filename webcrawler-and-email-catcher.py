import requests
import re

domain = raw_input('Domain: ')
to_crawl = [domain]
crawled = set()
emails_found = set()

interval = input('Enter the maximum url search range: ')


header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}


for i in range(interval):
    url = to_crawl[0]
    try:
        req = requests.get(url, headers=header)
    except:
        to_crawl.remove(url)
        crawled.add(url)
        continue

    html = req.text
    links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
    print 'Crawling:', url

    emails = re.findall(r'[\w\._-]+@[\w_-]+\.[\w\._-]+\w', html)

    to_crawl.remove(url)
    crawled.add(url)

    for link in links:
        if link not in crawled and link not in to_crawl:
            to_crawl.append(link)

    for email in emails:
        emails_found.add(email)

print emails_found