import re
import mechanicalsoup
import urllib.request
from inscriptis import get_text
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

blue = '\033[94m'
cyan = '\033[96m'
green = '\033[92m'
end = '\033[0m'

while True:

  x = input(f"{blue}moai search - {end}")
  if x == "search":
    searchres = input(" what do you wanna search for? - ")
    cls()

    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://www.google.com/")

    browser.select_form('form[action="/search"]')
    browser["q"] = searchres

    browser.submit_selected(btnName="btnG")

    for link in browser.links():
        target = link.attrs['href']
        if (target.startswith('/url?') and not
                target.startswith("/url?q=http://webcache.googleusercontent.com")):
            target = re.sub(r"^/url\?q=([^&]*)&.*", r"\1", target)
            print(target)
  elif x == "open":
    res = input(f"{green} type the url - https://{end}")
    cls()
    url = "https://" + res
    html = urllib.request.urlopen(url).read().decode('utf-8')

    text = get_text(html)
    print(text)
  elif x == "help":
    print(" open - type in the url to go to the page \n search - type in keywords to find most relevant url's")
  else:
      print(" invalid command, type 'help'")
