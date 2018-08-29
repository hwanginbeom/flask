# -*- coding : utf-8 -*-
#flask run --port 8080 --host 0.0.0.0
from flask import Flask ,render_template,request
from bs4 import BeautifulSoup
import datetime
import random
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")
    
#variable routing
@app.route("/inbeom/<string:name>")
def hellobeom(name):
    return render_template("hello.html",n=name)

#/cube/숫자
@app.route("/cube/<int:value>")
def cube(value):
    return render_template("cube.html", value=value*value)
    

#/cube/숫자
@app.route("/cube2/<int:value>")
def cube2(value):
    return render_template("cube2.html", value=value*value)
    
@app.route("/lunch")
def lunch():
    lunch_box = ["20층", "김밥카페","양자강","바스버거","시골집"]
    lunch=random.choice(lunch_box)
    return render_template("lunch.html",lunch=lunch , box = lunch_box)
    
@app.route('/google')
def google():
    return render_template("google.html")
    
@app.route('/opgg')
def opgg():
    return render_template("opgg.html")
    
@app.route('/opggresult')
def opggresult():
    name = request.args.get('q') # name에 썻던걸 쓴다.
    res = requests.get('http://www.op.gg/summoner/userName={}'.format(name))
    soup = BeautifulSoup(res.content, 'html.parser')
    solotierRank=soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierRank > span')[0].text
    teamtierRank=soup.select(' div.TierRank > div.TierRank')[0].text
    win= soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')[0].text
    lose = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')[0].text
    win=win.text
    lose=lose.text
    solotierRank=solotierRank.text
    teamtierRank=teamtierRank.text
    
    return render_template("opggresult.html", name = name, win=win , lose=lose ,solotierRank=solotierRank, teamtierRank=teamtierRank)    
    
@app.route("/identity")
def identity():
    identity_list = ["왕족", "브라만","크샤트리아","바이샤","수드라","불가축천민","리동훈"]
    identity=random.choice(identity_list)
    return render_template("identity.html",identity=identity , identity_list = identity_list)

    
@app.route("/christams")
def christams():
    now = datetime.datetime.now()
    christams =""
    if (now.month == 12 and now.day == 25):
        christams =" 맞아 ! "
    else :
        christams="아니야!"
    return render_template("christams.html",christams=christams)
    
if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0')