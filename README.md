# hackathon-manager
Procurator is a web application meant to assist evnet organizers while organizing a hackathon, or any other event. It does so by providing a clear representation of all the necessary tasks, in order of date, that the organizing team needs.

### Installation
	git clone https://github.com/emily-yu/hackathon-manager.git
	cd init
	sh generate.sh
	
### Usage
	./ngrok http 5000
	python app.py
	
Copy paste the ngrok link into `global.js`'s variable named ngrok, then open `index.html`

### Improvements
* port CSV data storage to a more collaborative data storage