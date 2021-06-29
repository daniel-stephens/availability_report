from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import StringField, SubmitField, BooleanField, IntegerField, FloatField, HiddenField
from wtforms.fields.html5 import DateField, TimeField
from  wtforms.validators import DataRequired
from app.models import Location, Asset, Asset_Type, Department, Delayance, Area, Water, Water_Type


def department_query():
    return Department.query


def asset_type_query():
    return Asset_Type.query


def location_query():
    return Location.query


def asset_query():
    return Asset.query


class DelayForm(FlaskForm):
    name = StringField('DELAY', validators=[DataRequired()])
    asset = QuerySelectField(query_factory = asset_query, allow_blank=False, get_label='name', validators=[DataRequired()])
    department =  QuerySelectField(query_factory = department_query, allow_blank=False, get_label='department', validators=[DataRequired()])
    time_from = TimeField('START TIME', validators=[DataRequired()])
    time_to = TimeField('STOP TIME', validators=[DataRequired()])
    date = DateField('DATE', validators=[DataRequired()] )
    action_taken = StringField('ACTION TAKEN')
    submit = SubmitField('SUBMIT')


class AssetForm(FlaskForm):
    asset = StringField('NAME', validators=[DataRequired()])
    asset_type = QuerySelectField(query_factory = asset_type_query, allow_blank=False, get_label='asset_type', validators=[DataRequired()])
    location = QuerySelectField(query_factory = location_query, allow_blank=False, get_label='location', validators=[DataRequired()])
    submit = SubmitField('SUBMIT')


class DeleteForm(FlaskForm):
    delete_id = HiddenField("Hidden table row ID")
    delete = SubmitField("Delete")


class WaterForm(FlaskForm):
    raw_water = FloatField('RAW WATER')
    biney = FloatField('Biney Estate')
    toytown = FloatField('Toy Town')
    monsi_valley = FloatField('Monsi Valley')
    sam_jonah = FloatField('Sam Jonah ')
    bill_hussey = FloatField('Bill Hussey')
    old_anyinam = FloatField('Old Anyinam')
    date = DateField('Date',  validators=[DataRequired()])
    submit = SubmitField('Sumbit')


  