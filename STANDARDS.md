# Code Standards

| # | Rule | Example |
| --- | --- | --- |
| 1 | **Naming.** Use snake_case for functions, variables, and file names. Use PascalCase for classes. Use UPPER_CASE for constants. | `utc_now()`, `staff_id`, `audit_log.py`<br>`class AuditLogEntry`<br>`MIGRATIONS_DIR` |
| 2 | **Imports at the top.** Put every import at the top of the file. Do not import inside a function. | Yes: `from .main import bp as main_bp` at the top of `bookstore/__init__.py`<br>No: the same line inside `create_app()` |
| 3 | **Import order.** Standard library first, then installed libraries, then our own code. Put one blank line between the groups. | `import os`<br>`from pathlib import Path`<br><br>`from flask import Flask`<br><br>`from .extensions import db, migrate` |
| 4 | **No wildcard imports.** Name each thing that you import. | Yes: `from flask import Flask, render_template`<br>No: `from flask import *` |
| 5 | **Indentation.** Use 4 spaces for each level. Do not use tabs. | <code>def index():</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;return render_template("main/index.html")</code> |
| 6 | **Line length.** No line is longer than 120 characters. | Split a longer line:<br><code>app = create_app(</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;{"TESTING": True},</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;instance_path=str(tmp_path / "instance"),</code><br><code>)</code> |
| 7 | **Quotes.** Use double quotes for strings. | Yes: `"create"`<br>No: `'create'` |
| 8 | **Docstrings.** Every file, class, and function starts with a short description. | <code>def utc_now():</code><br><code>&nbsp;&nbsp;&nbsp;&nbsp;"""The current time in UTC."""</code> |
| 9 | **Comments say why, not what.** | Yes: `# The database keeps all times in UTC.`<br>No: `# Get the time.` |
| 10 | **No leftovers.** Merged code has no commented-out code and no stray `print()` calls. | No: `# db.session.commit()`<br>No: `print(entry)` |
| 11 | **Test names.** Test files are `test_<thing>.py`. Test functions are `test_<what it checks>`. | `tests/test_setup.py`<br>`def test_home_page_opens(client):` |
| 12 | **CSS class names.** Use lowercase words joined by hyphens. | Yes: `flash-error`<br>No: `flashError`, `flash_error` |
