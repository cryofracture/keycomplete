from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class SubmitRunForm(FlaskForm):
    advertiser = StringField('Advertiser', validators=[DataRequired(), Length(min=8, max=40)])
    tank = StringField('Tank', validators=[DataRequired(), Length(min=8, max=40)])
    healer = StringField('Healer', validators=[DataRequired(), Length(min=8, max=40)])
    first_dps = StringField('DPS1', validators=[DataRequired(), Length(min=8, max=40)])
    second_dps = StringField('DPS2', validators=[DataRequired(), Length(min=8, max=40)])
    keyholder = StringField('Keholder', validators=[DataRequired(), Length(min=8, max=40)])
    discount = IntegerField('10k', validators=[DataRequired()])
    submit = SubmitField('Submit Run')