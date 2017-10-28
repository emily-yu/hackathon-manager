from flask import Flask, request
import urllib.request
# from bottle import route, run, template, static_file, get, post, request
import requests
# from secret import getSID, getAuth, getAuthy
import string
import re
import json
import base64
import csv
import pandas
import codecs

array1 = list()
array2 = list()
array3 = list()
array4 = list()

app = Flask(__name__)

@app.route("/")
#Each row is a user
def hello():
	with open('data.csv', newline='') as myFile1:  
		reader1 = csv.reader(myFile1)
		for row in reader1:
			print(row)
	with open('hardware.csv', newline='') as myFile2:
		reader2 = csv.reader(myFile2)
		for row in reader2:
			print(row)
	with open('sponsors.csv', newline='') as myFile3:
		reader3 = csv.reader(myFile3)
		for row in reader3:
			print(row)
	with open('judges.csv', newline='') as myFile4:
		reader4 = csv.reader(myFile4)
		for row in reader4:
			print(row)
	return "hey it's me"
# write new user
@app.route("/write")
def newSheet():
	# http://b99de565.ngrok.io/write?input=nam&email=edf&school=asdf
	name = request.args.get("input")
	email = request.args.get("email")
	school = request.args.get("school")
	row = [name, email, school]
	with open('data.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([name, " "]), ''.join([email, " "]), ''.join([school, " "])])
		array1.append(row)
	return "Users"

@app.route("/hardware")
def newSheet2():
	deviceName = request.args.get("deviceName")
	loanee = request.args.get("loanee")
	cost = request.args.get("cost")
	row = [deviceName, loanee, cost]
	with open('hardware.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([deviceName, " "]), ''.join([loanee, " "]), ''.join([cost, " "])])
		array2.append(row)
	return "Hardware"

@app.route("/sponsors")
def newSheet3():
	companyName = request.args.get("companyName")
	status = request.args.get("status")
	proposal = request.args.get("proposal")
	notes  = request.args.get("notes")
	row = [companyName, status, proposal, notes]
	with open('sponsors.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([companyName, " "]), ''.join([status, " "]), ''.join([proposal, " "]), ''.join([notes, " "])])
		array3.append(row)
	return "Sponsors"

@app.route("/judges")
def newSheet4():
	judgeName = request.args.get("judgeName")
	projectName = request.args.get("projectName")
	c1Grade = request.args.get("c1Grade")
	c1Notes = request.args.get("c1Notes")
	c2Grade = request.args.get("c2Grade")
	c2Notes = request.args.get("c2Notes")
	c3Grade = request.args.get("c3Grade")
	c3Notes = request.args.get("c3Notes")
	c4Grade = request.args.get("c4Grade")
	c4Notes = request.args.get("c4Notes")
	c5Grade = request.args.get("c5Grade")
	c5Notes = request.args.get("c5Notes")
	row = [judgeName, projectName, c1Grade, c1Notes, c2Grade, c2Notes, c3Grade, c3Notes, c4Grade, c4Notes, c5Grade, c5Notes]
	with open('judges.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([judgeName, " "]), ''.join([projectName, " "]), ''.join([c1Grade, " "]), ''.join([c1Notes, " "]), ''.join([c2Grade, " "]), ''.join([c2Notes, " "]), ''.join([c3Grade, " "]), ''.join([c3Notes, " "]), ''.join([c4Grade, " "]), ''.join([c4Notes, " "]), ''.join([c5Grade, " "]), ''.join([c5Notes, " "])])
		array4.append(row)
	return "judges"

@app.route("/output1")
def output1():
	return array1
@app.route("/output2")	
def output2():
	return array2
@app.route("/output3")
def output3():
	return array3
@app.route("/output4")
def output4():
	return array4

@app.route("/sendEmail")
def send_simple_message():
	# http://b99de565.ngrok.io/sendEmail?name=bob&email=eyudeveloper@gmail.com&subject=same&text=hahahahahasmaeaseas
	name = request.args.get("name")
	email = request.args.get("email")
	subject = request.args.get("subject")
	textLine = request.args.get("text")
	return requests.post(
		"https://api.mailgun.net/v3/sandboxc5380f848a684d4aa86069c1308d4884.mailgun.org/messages",
		auth=("api", "key-ef2d27e2ebe2754a5335866944846055"),
		data={"from": "PalyHacks <info@palyhacks.io>",
		# "to": "HM <eyudeveloper@gmail.com>",
		"to" : name + " <" + email + ">",
		# "subject": "Hello HM",
		"subject" : subject,
		# "text": "Congratulations HM, you just sent an email with Mailgun!  You are truly awesome!"
		"text" : textLine,
		})

if __name__ == '__main__':
        app.run()
