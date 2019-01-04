# MDChem
* * *
## URLS
* http://mdcchem.ddns.net/ (test server)
* http://chemtutor.hopto.org/ (pythonanywhere test server)
* http://68.183.111.180/ (API testing server)
* * *
## objectives:
* Store user data from a Unity based game using REST.
* Turn that data into useful statistics and trends.
* Manage who has access to the data
* * *
## setup:
* Cd inside project foler
* * **cd /your/dir/here**
* Install dependencies
* * **pip install -r requirements.txt**
* * if pip fails install the deps 1 by 1 with pip install dep_name
* setup database (*perhaps change user and password*)
* * __create database db_example; -- Create the new database__
* * __create user 'springuser'@'%' identified by 'ThePassword'; -- Creates the user__
* * __grant all on db_example.* to 'springuser'@'%'; -- Gives privileges to the new user on the newly created database__
* Initialize the database
* * **python init_db.py**
* Run the main python file
* * **python main.py**
* * note that if on mac/linux you may have to specify python version (python=python2.x, python3=python3.x)
* Open browser and test
* * **localhost:5000 in browser**
* To test on remote
* * **edit main.py app.run() with app.run(host="your host's ip address", port=preferred port number)**
* * **also edit config/config.py and set local to "False"**
* * **edit the templates and static variables to the absolute path of those folders in the MDChem directory** (*might big issues with apache but the local code should work with the embadded flask server*)
* * for your **SQLALCHEMY_DATABASE_URI** enter appropriate database credentials where your **username:password** precedes the database ip address
* * * 
## Tech:
* Python 3
* flask
* flask-cors
* sql-alchemy
* firebase
* mysql
* javascript
* bootstrap
* REST principle
* * * 
## Dependencies:
* requirements.txt 
* * * 
## Todo:
* finish landing page styling with informativve text and video tutorials
* finish contact form, preferably with email support
* design and implement password recovery mechanism
* design data presentation
* design data model
* finish high score API
* refactor API code structure, more unified
* research CORS
* Research security best practices for APIs
* find better solution for config file
* learn more GIT
* design userdata api and admin panel page
* * * 
## Routes:
* /admin (WIP)
* * admin console to view and manipulate all data
* /contact (WIP)
* * email contact form
* /index (WIP)
* * landing page with project information
* /login
* * login page
* /logout
* * logout function
* /recover (WIP)
* * To recover password via recovery passphrase
* /register
* * Register your account
* * * 
## API:
* /admin
* * POST
* * * (Headers = Token) returns a list of all admins
* * * 
* /highscore (WIP)
* * GET
* * * Returns a processes list of with the highest scores from the database via query
* * * 
* /logout
* * POST
* * * (Headers = Token, Email) used for auto logg off
* * * 
* /logs
* * POST
* * * (Headers = Token) used to apache error/access logs
* * * 
* /news
* * GET
* * * returns a list of news items
* * POST
* * * (headers = Token | Body) Saves a news item to database
* * * 
* /save
* * GET
* * * returns a list of all students data objects in database
* * POST 
* * * (Headers = uuid, levelid, score | body = 'json data') Saves a student and level specific data ojbect to the database
* * * 
* /update
* * POST
* * * (Headers = token, email, verifyemail, password. verifypassword) Updates the users password
* * * 
* /updatestudents
* * GET
* * * pings server to run a function that pulls all the users from firebase and makes a local student model with uuid and email
* * * 
* /userdata
* * POST
* * * (Headers = email, token, uuid) returns data for a single student and returns student specific json
* * * 
* /users
* * POST
* * * (Headers = token) returns a list of all current students
* * * 
* 