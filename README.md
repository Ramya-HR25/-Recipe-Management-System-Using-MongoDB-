# Recipe Management System (Flask + MongoDB)

Simple recipe management web app built with Flask and MongoDB. This repository contains a minimal example app for adding, viewing, updating and deleting recipes.

**Project structure**

Below is the repository tree (top-level files and folders):

```
recipe_app_basic/
├─ app.py
├─ interactive_mongo.py
├─ mongo_commands.py
├─ requirements.txt
├─ README.md
├─ .gitignore
├─ .venv/  (optional - created when you make a virtual environment)
├─ templates/
│  └─ index.html
└─ static/
	└─ style.css
```

(The `.venv/` folder is not included in the repo and is shown here as optional.)

**Prerequisites**

- Python 3.8+ installed
- MongoDB running locally on default port (27017). For a quick start, run MongoDB Community Server or use Docker.

**Install dependencies**

Open PowerShell in the project directory and (recommended) create a virtual environment, then install dependencies:

```powershell
python -m venv .venv
; $env:VIRTUAL_ENV = (Resolve-Path .venv).Path
; .\.venv\Scripts\Activate.ps1
; pip install --upgrade pip
; pip install -r requirements.txt
```

If you prefer not to create a venv, run:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

**Run the app**

The app uses `app.run(debug=True)` so you can start it directly with:

```powershell
python app.py
```

Alternatively, run with Flask CLI (PowerShell):

```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
python -m flask run
```

Open http://127.0.0.1:5000 in your browser.

**Troubleshooting**

- Pylance "Import could not be resolved": make sure you're using the same Python interpreter in VS Code that has the dependencies installed (the virtual environment). Select the interpreter with the `.venv` created above.
- MongoDB connection errors: ensure MongoDB is running. If using a remote cluster, update the connection string in `app.py` and `mongo_commands.py`.

**Notes**

- `bson` is provided by `pymongo`, so installing `pymongo` resolves both `pymongo` and `bson.objectid` imports.

**License**

This is a simple example; adapt as needed.
