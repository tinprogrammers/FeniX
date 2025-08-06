# FeniX

> **🔥 FeniX — No fluff. No clutter. Just simple, fast, and ready to deploy.**


FeniX is a blazing fast and ultra-minimal Python full-stack web framework.

## Features
- Minimal routing system
- Single HTML template file for all views
- Variable replacement like `{{ name }}`
- Only 2 user files needed (`app.py` and `templates.html`)

## Folder Tree
```bash
myApp/
├── app.py
└── templates.html
````
## Quick Start

```bash
pip install fenix
```
## Example
```python
from fenix import App

app = App()

@app.route("/")
def home():
    return app.render("home", name="Azeem")

app.run()
```
## templates.html
```html
{% template "home" %}
<html><body>Hello {{ name }}</body></html>
```
## License
MIT License


---
