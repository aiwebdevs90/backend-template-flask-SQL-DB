# Backend-Template-Flask-SQL-DB

Backend template using HTML5, CSS3, JavaScript, Flask and connected to a SQL or MySQL database.

* First thing to do is create virtual environment by typing the following command:
  
`python3 -m venv "evnname"` for demo purposes i did `python3 -m venv "myenv"`

* The next file that needs to be created is the .gitignore file, once a file is added to the ignore list it will not be pushed to github. Again can be done by right clicking on the file panel or type into the CLI:

`touch .gitignore`

* Now we need to add the virtual myenv directory to the .gitignore list, to do this open the .gitignore file and type the following:

`myevn/`

* Now we can activate the virtual environment by typing this into the CLI:

`source myenv/bin/activate`

Here you will notice in brackets in the terminal it will say your virtual environment name: `(myenv)`

* To deactivate the virtual environment type this into the CLI:
  
`deactivate`

* Now we need to install Flask, type this command into the CLI:

`pip3 install flask`

* To check and see if flask installed correctly and all its dependencies type this command into the CLI:

`pip3 freeze`

Your terminal should display this at the moment:

```
click==8.0.3
Flask==2.0.2
itsdangerous==2.0.1
Jinja2==3.0.3
MarkupSafe==2.0.1
Werkzeug==2.0.2
```

* Now we need to create a file called app.py, this can be done in h the GUI or CLI:

`touch app.py`

* Inside of the app.py file we need to add the following code below:

```
import os
from flask import Flask, render_template

# Creating a Flask Instance
app = Flask(__name__)


#  Creating a route decorator for homepage
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
```

* Now we need to create the server and this can be done in 2 different ways.

* The first way is using the CLI by typing the following commands in order top to bottom:

```
export FLASK_ENV=development
export FLASK_APP=app.py
```

* To run the server type the following command: `flask run` and to exit the server using the keyboard press: `Ctrl c`

* The second way that this can be done is by creating a env.py to set the default environment variables, this can be done using the GUI or CLI:

`touch env.py`

**Now remember to add this to the .gitignore list, so it does not get pushed to GitHub.**

* At this stage your .gitignore files should look like this:

```
myenv/
env.py
__pycache__/
```

**The pycache directory was created when the server was run, this dir does not need to be pushed to GitHub either.**

* Inside of the env.py file add the following lines of code below:

```
import os

# Setting the default environment variables
os.environ.setdefault("IP", "127.0.0.1")
os.environ.setdefault("PORT", "8000")
```

**The default IP is the local host IP and the port can be any number you like.**

* Now in the app.py file we need to some additional lines of code, it should look something like this:

```
import os
from flask import Flask, render_template

if os.path.exists("env.py"):
    import env

# Creating a Flask Instance
app = Flask(__name__)


#  Creating a route decorator for homepage
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
```

* Once this is done, you can then run the code by typing in the following command in the CLI:

`python3 app.py`

**Personally the second method is longer but gives you more control because as we progress more will be added to the env.py.**

* Now that we know that the page loads we can now create our templates folder and inside of that folder we will create the index.html file and add our own custom html code, this can be done using the GUI or CLI:

```
mkdir templates
touch templates/index.html
```

* Open the index.html file and add the following basic html code:

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flask SQL Test Website</title>
</head>
<body>
  <h1>Hello World!!!</h1>
  <p>This is my first web page paragraph</p>
</body>
</html>
```

* Now go back to the app.py file and change the index def return to this code below:

`return render_template("index.html")`

* Now save all and run the server: `python3 app.py` and you will see that the index page is now showing the index html code.