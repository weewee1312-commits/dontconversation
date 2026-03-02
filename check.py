import requests
from bs4 import BeautifulSoup
import os

URL = "https://ice.dongguk.edu/article/notice/list"
WEBHOOK = https://discord.com/api/webhooks/1477952168429617203/qMQamCKC9Gzu2kWLwrrCaqXUpEMSNElWKh9TKlv7wzXbETj2so4Y_TKQi4HcucPEms4D

def get_title():
html = requests.get(URL).text
soup = BeautifulSoup(html,"html.parser")
return soup.select_one("table tbody tr td a").text.strip()

last=None
if os.path.exists("last.txt"):
last=open("last.txt").read()

now=get_title()

if last!=now:
requests.post(WEBHOOK,json={"content":f"새 공지: {now}"})
open("last.txt","w").write(now)
