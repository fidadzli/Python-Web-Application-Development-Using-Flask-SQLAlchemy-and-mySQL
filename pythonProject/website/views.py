from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Barber55, Barber44, Barber33, Barber22, Barber11
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('barber33')
        haircut = request.form.get('barber22')
        apptime = request.form.get('barber44')
        # contact = request.form.get('contact')

        if len(note) < 4:
            flash('Barber is too short!', category='error')
        elif len(haircut) < 4:
            flash('haircut not added!', category='error')
        elif len(apptime) < 4:
            flash('No appointment time added!', category='error')

        else:
            new_note = Barber33(barber=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()


            new_haircut = Barber22(haircut=haircut, user_id=current_user.id)
            db.session.add(new_haircut)
            db.session.commit()


            new_apptime = Barber44(time=apptime, user_id=current_user.id)
            db.session.add(new_apptime)
            db.session.commit()


            new_contact = Barber55(status='pending', user_id=current_user.id)
            db.session.add(new_contact)
            db.session.commit()
            flash('Submission is done! The status of your appointment is pending. Thank you', category='success')
            return redirect(url_for('views.home'))

    return render_template("home.html", barber11=current_user)
