from flask import render_template, url_for, flash, redirect, request
from app.forms import DelayForm, AssetForm
from app import app, db
from  wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import Location, Asset, Asset_Type, Department, Delayance

@app.route('/',  methods=['GET', 'POST'])
def delay():
    form = DelayForm()
    if form.validate_on_submit():
        ass = form.asset.data
        # asset = Asset.query.filter_by(name=ass).first()
        delay = Delayance(asset=ass, department=form.department.data, time_from = form.time_from.data, 
                        time_to = form.time_to.data, date = form.date.data, action = form.action_taken.data)
        db.session.add(delay)
        db.session.commit()
        flash(f'Delay has been added to the database', 'Success')
        return redirect(url_for('delay'))

    return render_template('delay.html', title='Delay', form=form)




@app.route('/asset',  methods=['GET', 'POST'])
def assets():
    form = AssetForm()
    if form.validate_on_submit():
        assets = Asset(name=form.asset.data, asset_type = form.asset_type.data, location=form.location.data)
        db.session.add(assets)
        db.session.commit()
        flash(f'Asset has been added to the database', 'Success')
        return redirect(url_for('assets'))
    
    
    return render_template('asset.html', title='Delay', form=form)

