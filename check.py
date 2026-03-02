import os
import requests
from bs4 import BeautifulSoup

URL = "https://ice.dongguk.edu/article/notice/list"
WEBHOOK = os.environ.get("DISCORD_WEBHOOK", "").strip()

def get_title():
    headers = {"User-Agent": "Mozilla/5.0"}
    html = requests.get(URL, headers=headers, timeout=20).text
    soup = BeautifulSoup(html, "html.parser")
    a = soup.select_one("table tbody tr td a")
    if not a:
        raise RuntimeError("공지 목록을 찾지 못했어요.")
    return a.get_text(strip=True)

def send_discord(msg):
    if not WEBHOOK:
        raise RuntimeError("DISCORD_WEBHOOK secret이 없음.")
    r = requests.post(WEBHOOK, json={"content": msg}, timeout=20)
    r.raise_for_status()

def main():
    now = get_title()

    last = None
    if os.path.exists("last.txt"):
        with open("last.txt", "r", encoding="utf-8") as f:
            last = f.read().strip()

    if last != now:
        send_discord(f"📢 동국대 ICE 새 공지: {now}\n{URL}")
        with open("last.txt", "w", encoding="utf-8") as f:
            f.write(now)

if __name__ == "__main__":
    main()
