import csv
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)

"""
templates altijd in template-map !
css-, js- en ico-files altijd in de static-map ! Hiernaar verwijzen in de html-file ! (zie links)

TO-DO in Terminal/cmd:
1. venv/Scripts/activate  ->  Om de virtual environment in de terminal te activeren

2. $env:FLASK_APP = "server.py"   ingeven in Terminal om de Flask-APP te koppelen aan deze server-file.

3. $env:FLASK_ENV = "development"  -> Dit zorgt voor development environment, met debugger ON

4. flask run

http://127.0.0.1:5000/
"""

# Homepage:
@app.route("/")
def my_home():
	return render_template("index.html")



# Andere pagina's (dynamisch opgesteld):
@app.route("/<string:page_name>")
def html_page(page_name):
	return render_template(page_name)

# Contactgegevens (email, onderwerp, tekst) opslaan in file:
def write_to_file(data):
	with open("database.txt", mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

"""
delimiter = komma zorgt voor separation (nieuwe data)
quotechar -> "" er rond of niet?
quoting -> csv.QUOTE_MINIMAL
"""


# Contact:

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
	if request.method == "POST":
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect("/thankyou.html")
		except:
			return "did not save to database"
	else:
		return "Something went wrong, try again."