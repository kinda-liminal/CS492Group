# Pacific Coast Book Store

CS492 group project: a Flask web app for a rare bookstore, with a SQLite database.

## Requirements

- Python 3.12 or newer. On Windows, select "Add python.exe to PATH" in the installer.
- Git
- A GitHub account with access to this repository

## Setup

Do these steps one time, after you get access to the repository.

1. Clone the repository, and go into its folder:
   ```
   git clone https://github.com/kinda-liminal/CS492Group.git
   cd CS492Group
   ```
2. Create a virtual environment. It keeps this project's libraries separate from the rest of your computer:
   - Windows: `python -m venv .venv`
   - macOS or Linux: `python3 -m venv .venv`
3. Activate the virtual environment. Do this every time you open a new terminal for this project:
   - Windows: `.venv\Scripts\activate`
   - macOS or Linux: `source .venv/bin/activate`

   Your prompt starts with `(.venv)` when it is active. If PowerShell blocks the script, run
   `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` one time, then try again.
4. Install the dependencies: `pip install -r requirements.txt`
5. Create your local database: `flask db upgrade`

## Run

```
flask run
```

Then open http://127.0.0.1:5000. Press Ctrl+C to stop the server.

## Test

```
pytest
```

All tests must pass before you open a pull request. To run one test file, give its path, for example `pytest tests/test_setup.py`.

## After you pull new changes

Teammates may add libraries or database changes. After each `git pull`, run:

```
pip install -r requirements.txt
flask db upgrade
```

## Database

- The database is the file `instance/bookstore.db`. Each person has their own copy, and Git ignores it.
- To start over with an empty database, delete `instance/bookstore.db`, then run `flask db upgrade`.
- To change a table, change its model in `bookstore/models/`, then run:
  ```
  flask db migrate -m "describe the change"
  flask db upgrade
  ```
  Commit the new file in `migrations/versions/` with your code.

## Project layout

| Folder | What it holds |
| --- | --- |
| `bookstore/` | The app code |
| `bookstore/models/` | The database tables |
| `bookstore/templates/` | The HTML pages |
| `migrations/` | The database changes |
| `tests/` | The tests |
