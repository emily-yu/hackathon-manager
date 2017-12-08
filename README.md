# hackathon-manager
Procurator is a web application meant to assist event organizers while organizing a hackathon, or any other event. It does so by providing a clear representation of all the necessary tasks, in order of date, that the organizing team needs.

### Installation

Clone the repository and run the application generation scripts.

	git clone https://github.com/emily-yu/hackathon-manager.git
	cd init
	sh generate.sh

Make sure you have a [Heroku](https://signup.heroku.com/) account and deploy your own app using the following button or run the heroku.sh script in the init folder by `sh heroku.sh`.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/emily-yu/hackathon-manager)

Open `global.js` and replace the variable ngrok with your Heroku app name, which can be found when you run the generate script. 

	var ngrok = <YOUR-HEROKU-APP-URL>
	
### Usage
Run the installation instructions, then open `index.html`
