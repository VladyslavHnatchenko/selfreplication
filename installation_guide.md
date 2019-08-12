SelfReplication app
____________________________________________________________________________________________________

Step 1:
Visit the following link to register a new OAuth application:
https://github.com/settings/applications/new
* Application name - you can fill this field with any app name you want.
* Homepage URL - when you use application locally you fill this field with the
    following link - http://127.0.0.1:5000. In production, you use another link:
    https://APPNAME.herokuapp.com.
    E.g. for our application the APPNAME is selfreplication, https://selfreplication.herokuapp.com.
* Authorization callback URL - when you use application locally you fill this field with
    the following link - http://127.0.0.1:5000/login/github/authorized.
    In production, you use another link: https://APPNAME.herokuapp.com/login/github/authorized.
* Register your application.
____________________________________________________________________________________________________

Step 2:
Run the following commands on your computer(bash shell):
- git clone https://github.com/VladyslavHnatchenko/selfreplication.git
- cd selfreplication
- virtualenv -p /usr/bin/python3.7 venv
- source venv/bin/activate
- pip install -r requirements.txt
____________________________________________________________________________________________________

Step 3:
Run the following commands on your computer(bash shell):
- Login to heroku in your terminal with the following command.
- heroku login
- git init
- heroku create your-first-heroku-app* --buildpack heroku/python
- heroku git:remote -a your-first-heroku-app*

*change to your credentials
____________________________________________________________________________________________________

Step 4:
Configuration and Config Vars for GitHub and Heroku.
Run the following commands on your computer(bash shell):
- heroku config:set GITHUB_OAUTH_CLIENT_ID=*
- heroku config:set GITHUB_OAUTH_CLIENT_SECRET=*
- heroku config:set OAUTHLIB_INSECURE_TRANSPORT=true
- heroku config:set FLASK_SECRET_KEY=*
- heroku config:set GITHUB_USERNAME=VladyslavHnatchenko
- heroku config:set REPOSITORY_NAME=selfreplication
- pip install -r requirements.txt
- git add .
- git commit -m "Heroku first commit"
- git push heroku master
- heroku open

*change to your credentials
____________________________________________________________________________________________________