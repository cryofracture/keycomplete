from flask import Flask, request, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
app = Flask(__name__)


from application import routes


bootstrap = Bootstrap(app)