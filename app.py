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

# names = ['101', '102', '36', '40']
# school = ['NUC_A', 'NUC_B', 'CATDOG', 'HYDRO_A']
# email = [.99, 1.02, 1.01, 1.00]

@app.route("/")
def hello():
	with open('data.csv', newline='') as myFile:  
		reader = csv.reader(myFile)
		for row in reader:
			# each row is a user
			print(row)
	return "hey its me"


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
	with open('data.csv', "w") as f:
		writer = csv.writer(f)
		writer.writerow([names, email, school])
	return "same"


if __name__ == '__main__':
        app.run()
