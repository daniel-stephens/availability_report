from flask import render_template, url_for, flash, redirect, request
from app.forms import DelayForm, AssetForm, DeleteForm, WaterForm
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


@app.route('/delete',  methods=['GET', 'POST'])
def listing():
    delete_form = DeleteForm()
    delays =  Delayance.query.order_by(Delayance.id.desc()).limit(10).all()
    if delete_form.validate_on_submit():
        entry_to_delete = Delayance.query.get(delete_form.delete_id.data)
        db.session.delete(entry_to_delete)
        db.session.commit()
        flash("Delay has been removed from the Database")
        return redirect(url_for("listing"))
    return render_template('list.html', title='List', delays=delays, 
                                Asset=Asset, Department=Department, delete_form=delete_form)

@app.route('/water', methods=['GET', 'POST'])
def water():
    form = WaterForm()
    return render_template('water.html', form = form)