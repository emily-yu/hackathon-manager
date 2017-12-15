from flask import Flask, request, render_template, send_file
import urllib.request
import requests
import string
import re
import json
import base64
import csv
import codecs
import os, errno
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def hello():
	with open(os.getcwd() + '/application/data.csv', newline='') as myFile1:  
		reader1 = csv.reader(myFile1)
		for row in reader1:
			print(row)
	with open(os.getcwd() + '/application/hardware.csv', newline='') as myFile2:
		reader2 = csv.reader(myFile2)
		for row in reader2:
			print(row)
	with open(os.getcwd() + '/application/sponsors.csv', newline='') as myFile3:
		reader3 = csv.reader(myFile3)
		for row in reader3:
			print(row)
	with open(os.getcwd() + '/application/judges.csv', newline='') as myFile4:
		reader4 = csv.reader(myFile4)
		for row in reader4:
			print(row)
	with open(os.getcwd() + '/application/goals.csv', newline='') as myFile5:
		reader5 = csv.reader(myFile5)
		for row in reader5:
			print(row)

	return "hey it's me"

@app.route("/users")
def newSheet():
	name = request.args.get("name")
	email = request.args.get("email")
	school = request.args.get("school")
	row = [name, email, school]
	with open(os.getcwd() + '/application/data.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([name, " "]), ''.join([email, " "]), ''.join([school, " ,,"])])
		#array1.append(''.join([name, " "]) + ''.join([email, " "]) + ''.join([school, " "]))
	return "Users"

@app.route("/hardware")
def newSheet2():
	deviceName = request.args.get("deviceName")
	loanee = request.args.get("loanee")
	cost = request.args.get("cost")
	row = [deviceName, loanee, cost]
	with open(os.getcwd() + '/application/hardware.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([deviceName, " "]), ''.join([loanee, " "]), ''.join([cost, " ,,"])])
		#array2.append(''.join([deviceName, " "]) + ''.join([loanee, " "]) + ''.join([cost, " "]))
	return "Hardware"

@app.route("/sponsors")
def newSheet3():
	companyName = request.args.get("companyName")
	status = request.args.get("status")
	proposal = request.args.get("proposal")
	notes  = request.args.get("notes")
	row = [companyName, status, proposal, notes]
	with open(os.getcwd() + '/application/sponsors.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([companyName, " "]), ''.join([status, " "]), ''.join([proposal, " "]), ''.join([notes, " ,,"])])
		#array3.append(''.join([companyName, " "]) + ''.join([status, " "]) + ''.join([proposal, " "]) + ''.join([notes, " "]))
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
	with open(os.getcwd() + '/application/judges.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([judgeName, " "]), ''.join([projectName, " "]), ''.join([c1Grade, " "]), ''.join([c1Notes, " "]), ''.join([c2Grade, " "]), ''.join([c2Notes, " "]), ''.join([c3Grade, " "]), ''.join([c3Notes, " "]), ''.join([c4Grade, " "]), ''.join([c4Notes, " "]), ''.join([c5Grade, " "]), ''.join([c5Notes, " ,,"])])
		#array4.append(''.join([judgeName, " "]) + ''.join([projectName, " "]) + ''.join([c1Grade, " "]) + ''.join([c1Notes, " "]) + ''.join([c2Grade, " "]) + ''.join([c2Notes, " "]) + ''.join([c3Grade, " "]) + ''.join([c3Notes, " "]) + ''.join([c4Grade, " "]) + ''.join([c4Notes, " "]) + ''.join([c5Grade, " "]) + ''.join([c5Notes, " "]))
	return "judges"

@app.route("/goals")
def newSheet5():
	goals = request.args.get("date")
	emailList = request.args.get("milestone")
	row = [goals, emailList]
	with open(os.getcwd() + '/application/goals.csv', "a") as f:
		writer = csv.writer(f)
		writer.writerow([''.join([goals, " "]), ''.join([emailList, " "]), ''.join(["N/A ,,"])])
		#array5.append([''.join([goals, " "]), ''.join([emailList, " "])])
	return "goals"

@app.route("/output1")
def output1():
	with open(os.getcwd() + '/application/data.csv') as f:
		s1 = f.read() + '\n' # add trailing new line character
	return(s1)

@app.route("/output2")
def output2():
	# asdf
	with open(os.getcwd() + '/application/hardware.csv') as f:
		s2 = f.read() + '\n' # add trailing new line character
	return(s2)

@app.route("/output3")	
def output3():
	with open(os.getcwd() + '/application/sponsors.csv') as f:
		s3 = f.read() + '\n' # add trailing new line character
	return(s3)

@app.route("/output4")
def output4():
	with open(os.getcwd() + '/application/judges.csv') as f:
		s4 = f.read() + '\n' # add trailing new line character
	return(s4)

@app.route("/output5")
def output5():
	with open(os.getcwd() + '/application/goals.csv') as f:
		s5 = f.read() + '\n' # add trailing new line character
	return(s5)
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		new_rows = []
		f = request.files['file']
		directory = os.getcwd() + '/application/invoices/' + request.values['row']+ '/'
		print(directory)
		if (os.path.exists(directory)):
			print("exists")
		else:
			os.makedirs(directory)

		f.save(os.path.join(directory, secure_filename(f.filename)))

		with open(os.getcwd() + '/application/sponsors.csv') as f:
			reader = csv.reader(f)
			# print(reader)
			for row in reader:
				new_rows.append(row)
				# print(row)

		print(new_rows[int(request.values['row'])][4])
		new_rows[int(request.values['row'])][4] = 'loading...'
		print(new_rows[int(request.values['row'])][4])
		with open(os.getcwd() + '/application/sponsors.csv', 'w') as f:
			writer = csv.writer(f)
			writer.writerows(new_rows)

		return "file uploaded"

@app.route('/get_files')
def get_files():
	folder = request.args.get('folder')
	directory = os.getcwd() + '/application/invoices/' + folder
	print(directory)
	img_files = ''
	for file in os.listdir(directory):
		print(file)
		if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
			print("YES")
			img_files += ',' + file
		else:
			print("NO")

	print(os.listdir(directory))
	return img_files

@app.route('/change_milestone_status')
def change_milestone_status():
	new_rows = []
	row = request.args.get('row')
	status = request.args.get('status')

	with open(os.getcwd() + '/application/goals.csv') as f:
		reader = csv.reader(f)
		# print(reader)
		for row in reader:
			new_rows.append(row)
			# print(row)

	print(new_rows[int(request.values['row'])][2])
	new_rows[int(request.values['row'])][2] = status
	print(new_rows[int(request.values['row'])][2])
	with open(os.getcwd() + '/application/goals.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows(new_rows)

	return "changed"

@app.route("/sendEmail")
def send_simple_message():
	name = request.args.get("name")
	email = request.args.get("email")
	subject = request.args.get("subject")
	textLine = request.args.get("text")
	return requests.post(
		"https://api.mailgun.net/v3/sandboxc5380f848a684d4aa86069c1308d4884.mailgun.org/messages",
		auth=("api", "key-ef2d27e2ebe2754a5335866944846055"),
		data={"from": "PalyHacks <info@palyhacks.io>",
		"to" : name + " <" + email + ">",
		"subject" : subject,
		"text" : textLine,
		})

if __name__ == '__main__':
        app.run()
