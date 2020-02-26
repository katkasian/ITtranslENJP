### WARNING: as of Feb.26 2020 works only if original article by CNET News

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import argparse
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def validate_jap_article():
    """Reads user input: japanese article link"""
    parser = argparse.ArgumentParser(description="Cnet Eng-Jap IT articles")
    parser.add_argument("article_link", type = str)
    args = parser.parse_args()
    if args.article_link is not None:
        return args.article_link

def get_jap_article(link):
    """Takes link as an input, prints the text of
    the japanese article and outputs the link to the original article"""
    readurl = link
    html = urllib.request.urlopen(readurl, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    print(title)
    text=soup.find_all('div', {'class':["leaf-article-inner block_story"]})
    for item in text:
        print(item.text)
    englink = soup.find('a', {'class':["original_link"]})
    readylink = englink.get('href')
    print('***********************************************')
    print('End of Japanese article')
    print('***********************************************')
    return readylink

def get_orig_article(origlink):
    orightml = urllib.request.urlopen(origlink, context=ctx).read()
    soup = BeautifulSoup(orightml, 'html.parser')
    title = soup.title.string
    print("""\n""")
    print("""\n""")
    print(title)
    text = soup.find_all('script')
    for item in text[:1]:
        myjson = json.loads(item.text)
        origtext = myjson["articleBody"]
        print("""\n""")
        print(origtext)

def main():
    firstlink = validate_jap_article()
    secondlink = get_jap_article(firstlink)
    get_orig_article(secondlink)

if __name__ == "__main__":
    main()
