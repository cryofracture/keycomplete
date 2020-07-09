from application import app
from flask import Flask, request, render_template, redirect, url_for, flash
"""import os


from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField
import psycopg2
from psycopg2.extras import RealDictCursor
#from models import UploadForm
from werkzeug.utils import secure_filename
from pathlib import Path
import discord
from discord import Webhook, RequestsWebhookAdapter, File
from psycopg2 import __version__ as psycopg2_version"""
from dotenv import load_dotenv
load_dotenv
#Bootstrap(app)

#webhook = Webhook.partial(os.environ['WEBHOOK_ID'], os.environ['WEBHOOK_TOKEN'], adapter=RequestsWebhookAdapter())

#webhook.send(post)
#webhook.send(file=discord.File('img.jpg'))

@app.route('/index', methods = ['GET'])
@app.route('/', methods = ['GET'])
def index():
    return render_template('main.html')
#     user = {'username': 'Taylor'}
#     return f"""
# <html>
#     <head>
#         <title>Home Page - Completed Keys</title>
#     </head>
#     <body>
#         <h1>Hello, {user['username']}!</h1>
#     </body>
# </html>
#     """

# @app.route('/completed_key_review', methods = ['POST', 'GET'])
# def review():
#     advertiser  = request.form.get('advertiser')
#     tank        = request.form.get('tank')
#     healer      = request.form.get('healer')
#     first_dps   = request.form.get('dps1')
#     second_dps  = request.form.get('dps2')
#     keyholder   = request.form.get('keyholder')
#     discount    = request.form.get('discount')


#     return render_template('review.html', advertiser=advertiser, tank=tank, healer=healer, first_dps=first_dps, second_dps=second_dps, keyholder=keyholder, discount=discount)



# @app.route('/submitted', methods = ['POST', 'GET'])
# def submitted():
#     advertiser  = request.form.get('advertiser')
#     tank        = request.form.get('tank')
#     healer      = request.form.get('healer')
#     first_dps   = request.form.get('dps1')
#     second_dps  = request.form.get('dps2')
#     keyholder   = request.form.get('keyholder')
#     discount    = request.form.get('discount')

#     try:
#         query = f""" INSERT INTO {os.environ['DB_TABLE']} ({os.environ['DB_COLS']}) VALUES ('{advertiser}', '{tank}', '{healer}', '{first_dps}', '{second_dps}', '{keyholder}',  '{discount}') """
#         connection = psycopg2.connect(user=os.environ['DB_USER'],
#                                     password=os.environ['DB_PASS'],
#                                     host=os.environ['DB_HOST'],
#                                     port=os.environ['DB_PORT'],
#                                     database=os.environ['DB_NAME'])
#         cursor = connection.cursor()
#         cursor.execute(query)

#     except (Exception, psycopg2.Error) as error:
#         print(f"Error while connecting to Postgres:\n {error}")
    
#     finally:
#         if(connection):
#             cursor.close()
#             connection.close()
#             print("Postgres connection closed.")


#     return render_template('review.html', advertiser=advertiser, tank=tank, healer=healer, first_dps=first_dps, second_dps=second_dps, keyholder=keyholder, discount=discount)



# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=True)