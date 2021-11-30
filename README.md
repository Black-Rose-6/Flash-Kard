# About 

- This project aims to create a flash-card application that allows users to create,login into his/her account, create decks i.e. collection of cards. 
- A card consists of front and back which can be designed to store information as per the usage of the deck as per user. 
- The cards are scored into 5 categories EasyPeasy(10) , Easy(8) , Medium(6) , Hard(4) , Enigma(2) according to which deck is overall scored. 
- APIs are based on CRUD in the application , build/deplot with by flask-restful and are still underdevelopment. Hence it would be better if user restrain from putting too many request at a time

# Local Setup

- Clone the project
- Run `pip install -r requirements.txt` to install all dependencies


# Local Development Run

- To run the application run the following command in the terminal 
- `python3 main.py` It will start the flask app in `development`. Suited for local development.


# Replit run

- Clone the project to form your own repl for the project.
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
