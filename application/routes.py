from application import app
from flask import Flask, request, render_template, redirect, url_for, flash
import psycopg2
import os
"""
import os


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


@app.route('/final', methods = ['POST', 'GET'])
def final():
    advertiser  = request.form.get('advertiserName')
    tank        = request.form.get('tankName')
    healer      = request.form.get('healerName')
    first_dps   = request.form.get('DPS1Name')
    second_dps  = request.form.get('DPS2Name')
    keyholder   = request.form.get('keyholderName')
    discount    = request.form.get('discount')
    print(advertiser)
    print(tank)
    print(healer)
    print(first_dps)
    print(second_dps)
    print(keyholder)
    print(discount)
    try:
        query = f""" INSERT INTO {os.environ['DB_TABLE']} ({os.environ['DB_COLS']}) VALUES ('{advertiser}', '{tank}', '{healer}', '{first_dps}', '{second_dps}', '{keyholder}',  '{discount}') """
        connection = psycopg2.connect(user=os.environ['DB_USER'],
                                    password=os.environ['DB_PASS'],
                                    host=os.environ['DB_HOST'],
                                    port=os.environ['DB_PORT'],
                                    database=os.environ['DB_NAME'])
        cursor = connection.cursor()
        cursor.execute(query)
        

    except (Exception) as error:
        print(f"Error while connecting to Postgres:\n {error}")
    
    # finally:
    #     if(connection):
    #         cursor.close()
    #         connection.close()
    #         print("Postgres connection closed.")


    return render_template('final.html', advertiser=advertiser, tank=tank, healer=healer, first_dps=first_dps, second_dps=second_dps, keyholder=keyholder, discount=discount)



# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=True)