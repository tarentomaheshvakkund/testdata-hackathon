"""Web templates with XSS vulnerability."""
from flask import Flask, request
from jinja2 import Template

app = Flask(__name__)

@app.route('/user')
def user_profile():
    name = request.args.get('name', '')
    template = Template(f"<h1>Welcome {name}</h1>")
    return template.render()
