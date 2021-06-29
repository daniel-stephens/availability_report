from flask import render_template, url_for, flash, redirect, request
from app.forms import DelayForm, AssetForm, DeleteForm, WaterForm
from app import app, db
from app.models import Location, Asset, Department, Delayance, Water, Water_Type, Area

@app.route('/',  methods=['GET', 'POST'])
def delay():
    form = DelayForm()
    if form.validate_on_submit():
        ass = form.asset.data
        # asset = Asset.query.filter_by(name=ass).first()
        delay = Delayance(name=form.name.data, asset=ass, department=form.department.data, time_from = form.time_from.data, 
                        time_to = form.time_to.data, date=form.date.data, action = form.action_taken.data)
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
    if form.validate_on_submit():

        jimi = Water(asset_id = 1, water_id=1, area_id = 7, volume=form.raw_water.data , date= form.date.data)
        biney = Water(asset_id = 3, water_id=2, area_id = 1, volume=form.biney.data, date= form.date.data)
        toytown = Water(asset_id = 3, water_id=2, area_id =2 , volume=form.toytown.data, date= form.date.data)
        monsi_valley = Water(asset_id =3, water_id=2, area_id =3, volume=form.monsi_valley.data, date= form.date.data)
        sam_jonah = Water(asset_id = 2, water_id=2, area_id = 5, volume=form.sam_jonah.data, date= form.date.data)
        bill_hussey = Water(asset_id =2 , water_id=2, area_id = 4, volume=form.bill_hussey.data, date= form.date.data)
        old_anyinam= Water(asset_id =2 , water_id=2, area_id = 6, volume=form.old_anyinam.data, date= form.date.data)
        db.session.add(jimi)
        db.session.add(biney)
        db.session.add(toytown)
        db.session.add(monsi_valley)
        db.session.add(sam_jonah)
        db.session.add(bill_hussey)
        db.session.add(old_anyinam)
        db.session.commit()
        flash("Data has been removed from the Database")
        return redirect(url_for("water"))
    return render_template('water.html', form=form)


@app.route('/water_list', methods=['GET', 'POST'])
def waters():
    delete_form=DeleteForm()
    records = Water.query.order_by(Water.id.desc()).limit(10).all()
    if delete_form.validate_on_submit():
        entry_to_delete = Water.query.get(delete_form.delete_id.data)
        db.session.delete(entry_to_delete)
        db.session.commit()
        flash("Record has been removed from the Database")
        return redirect(url_for("home"))
    return render_template('water_list.html', title='Water list', records=records, 
                                Asset=Asset, delete_form=delete_form,Area =Area, Water_Type=Water_Type)

