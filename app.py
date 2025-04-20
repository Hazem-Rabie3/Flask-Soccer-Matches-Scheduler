from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
# Get the current date
current_date = datetime.now().strftime("%m/%d/%Y")
partS = current_date.strip().split("/")
currMonth = int(partS[0]) 
currDay = int(partS[1])
currYear = int(partS[2])
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/display", methods=["POST"])
def display():
   date = request.form.get("date")
   parts = date.strip().split("/")
   if not date or len(parts)!=3:
       return render_template("apology.html") 
   month = int(parts[0]) 
   day = int(parts[1])
   year = int(parts[2])
   if not (1 <= month <= 12) or not (1 <= day <= 31) :
       return render_template("apology.html")
   if year > currYear:
       return render_template("apology.html")
   elif year == currYear and month > currMonth:
        return render_template("apology.html")
   elif month == currMonth and day > currDay:
        return render_template("apology.html")

   page = requests.get(f"https://www.yallakora.com/match-center/مركز-المباريات?date={date}")
   src = page.content
   soup = BeautifulSoup(src, "html.parser")
   match_details = []
   champion_names = []
   champions = soup.find_all("div", {'class' : 'matchCard'})
   for champion in champions:
       champion_title = champion.contents[1].find("h2").text.strip()
       champion_names.append(champion_title)
       matches = champion.find_all("div" , {'class' : 'teamsData'})
       for match in matches:
           teamA = match.find("div", {'class':'teamA'}).find("p").text.strip()
           teamB = match.find("div", {'class':'teamB'}).find("p").text.strip()
           scoreAndTime = match.find("div", {'class':'MResult'}).find_all("span")
           score = f"{scoreAndTime[0].text.strip()} - {scoreAndTime[2].text.strip()}"
           time = f"{scoreAndTime[3].text.strip()}"
           match_details.append({"البطولة":champion_title, "الفريق الأول": teamA, "الفريق الثاني":teamB, "النتيجة": score, "الميعاد": time})
   return render_template("display.html",match_details= match_details, date=date, champion_names=champion_names)

@app.route("/save", methods = ["POST"])
def save():
    import json
    match_details = json.loads(request.form.get("match_details"))
    if not match_details:
        return "No match data to save"
    with open("F:\Scarping\data.csv", 'w', newline='', encoding='utf-8-sig') as outputFile:
        keys = match_details[0].keys()
        dict_writer = csv.DictWriter(outputFile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(match_details)
        return render_template("saved.html")




if __name__ == '__main__':
    app.run(debug=True)