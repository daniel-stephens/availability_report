from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import StringField, SubmitField, BooleanField, IntegerField, FloatField, HiddenField
from wtforms.fields.html5 import DateField, TimeField
from  wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import Location, Asset, Asset_Type, Department, Delayance


def department_query():
    return Department.query


def asset_type_query():
    return Asset_Type.query


def location_query():
    return Location.query


def asset_query():
    return Asset.query


class DelayForm(FlaskForm):
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
    raw_water = FloatField('RAW WATER', validators=[DataRequired()])
    biney = FloatField('Biney Estate', validators = [DataRequired()])
    toytown = FloatField('Toy Town', validators = [DataRequired()])
    monsi_valley = FloatField('Monsi Valley', validators = [DataRequired()])
    sam_jonah = FloatField('Sam Jonah ', validators = [DataRequired()])
    bill_hussey = FloatField('Bill Hussey', validators = [DataRequired()])
    old_anyinam = FloatField('Old Anyinam', validators = [DataRequired()])
    submit = SubmitField('Sumbit')


  