from flask import Flask, request, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from application.config import Config
app = Flask(__name__)
app.config.from_object(Config)

from application import routes


# bootstrap = Bootstrap(app)
#Bootstrap(app)
bootstrap = Bootstrap(app)