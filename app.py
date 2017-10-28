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

app = Flask(__name__)

@app.route("/")
def hello():
	with open('data.csv', newline='') as myFile:  
		reader = csv.reader(myFile)
		for row in reader:
			# each row is a user
			print(row)
	with open('hardware.csv', newline='') as myFile2:
		reader2 = csv.reader(myFile2)
		for row in reader2:
			print(row)
	with open('sponsors.csv', newline='') as myFile3:
		reader3 = csv.reader(myFile3)
		for row in reader3:
			print(row)
	return "hey it's me"


# write new user
@app.route("/write")
def newSheet():
	# http://b99de565.ngrok.io/write?input=nam&email=edf&school=asdf
	names = request.args.get("input")
	print(names)
	email = request.args.get("email")
	print(email)
	school = request.args.get("school")
	print(school)
	row = [names, email, school]
	with open('data.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([names, " "]), ''.join([email, " "]), ''.join([school, " "])])
	return "same"

@app.route("/hardware")
def newSheet2():
	deviceName = request.args.get("deviceName")
	print(deviceName)
	loanee = request.args.get("loanee")
	print(loanee)
	cost = request.args.get("cost")
	print(cost)
	row = [deviceName, loanee, cost]
	with open('hardware.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([deviceName, " "]), ''.join([loanee, " "]), ''.join([cost, " "])])
	return "same lmao"

@app.route("/sponsors")
def newSheet3():
	companyName = request.args.get("companyName")
	print(companyName)
	status = request.args.get("status")
	print(status)
	proposal = request.args.get("proposal")
	print(proposal)
	notes  = request.args.get("notes")
	print(notes)
	row = [companyName, status, proposal, notes]
	with open('sponsors.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([companyName, " "]), ''.join([status, " "]), ''.join([proposal, " "]), ''.join([notes, " "])])
	return "big shaq"



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
