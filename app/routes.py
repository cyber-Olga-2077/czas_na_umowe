from app import app
from flask import render_template, flash, redirect
from app.forms import UmowaNajmu
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import make_response


@app.route('/')
@app.route('/index')
def index():
    return "yes"

@app.route('/najem', methods = ['GET', 'POST'])
def formularz_najmu():
    form = UmowaNajmu()
    return render_template('umowa_najmu.html', title='Umowa Najmu', form=form)

