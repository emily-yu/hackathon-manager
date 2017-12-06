cd ..
git init
git add .
git commit -m "init"

heroku login
heroku create
heroku buildpacks:set heroku/python
git push heroku master