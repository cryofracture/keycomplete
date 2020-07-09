from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Regexp


class UploadForm(FlaskForm):
    advertiser  = StringField("Advertiser Name", validators=[DataRequired(),Length(min=8, max=40)])
    tank        = StringField("Tank Name", validators=[DataRequired(),Length(min=8, max=40)])
    healer      = StringField("Healer Name", validators=[DataRequired(),Length(min=8, max=40)])
    first_dps   = StringField("First DPS Name", validators=[DataRequired(),Length(min=8, max=40)])
    second_dps  = StringField("Second DPS Name", validators=[DataRequired(),Length(min=8, max=40)])
    keyholder   = StringField("Keyholder Name", validators=[DataRequired(),Length(min=8, max=40)])
    discount    = IntegerField("Discount Amount", validators=DataRequired())
    submit      = SubmitField('Upload Sale')