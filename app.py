from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

URL = "https://soco.seoul.go.kr/youth/bbs/BMSR00015/list.do?menuNo=400008"

def get_latest_posts():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    posts = []
    for post in soup.find_all("td", class_="subject")[:5]:  # 최신 5개 게시글
        title = post.get_text(strip=True)
        link = "https://soco.seoul.go.kr" + post.find("a")["href"]
        posts.append({"title": title, "link": link})

    return posts

@app.route("/")
def home():
    posts = get_latest_posts()
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
