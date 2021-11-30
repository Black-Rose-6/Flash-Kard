# Local Setup

- Clone the project
- Run `pip install -r requirements.txt` to install all dependencies


# Local Development Run

- To run the application run the following command in the terminal 
- `python3 main.py` It will start the flask app in `development`. Suited for local development.


# Replit run

- Go to shell and run
  `pip install --upgrade poetry`
- Click on `main.py` and click button run
- The web app will be availabe at https://replit.com/@Blac-rose-6/Flash-Cards#main.py


# Folder Structure

- `Flashcard` is the main folder.
- `main.py` is the python file which imports all the data from files and deploy the application.
- `/flashkard` is the folder which consist of the main code for our application.
- `/flashkard/static` - consists of the default `static` files for application.
- `/flashkard/templates` - consist of all the templates that are needed for the application.
- `/flashkard/__init.py__`,`/flashkard/api.py`,`/flashkard/models.py`,`/flashkard/views.py` -are the main code files for the application

```
Flashcard/
├── main.py
├── flashkard/
│   ├──static/
│   │   ├──css
│   │   │   ├──langind.css
│   │   │   ├──login.css
│   │   │   ├──register.css
│   │   │   └──review.css
│   │   └──js
│   │       └──reviewscript.js
│   ├──templates
│   │   ├──dashboard.html
│   │   ├──index.html
│   │   ├──landing.html
│   │   ├──login.html
│   │   ├──register.html
│   │   ├──review.html
│   │   └──temp.html
│   ├──__init__.py
│   ├──api.py
│   ├──models.py
│   ├──project.sqlite3
│   └──views.py
└──
```
