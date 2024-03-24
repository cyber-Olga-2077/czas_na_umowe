from app import app
from flask import render_template, flash, redirect
from app.forms import UmowaNajmu
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import make_response
from app.creating_pdf import create_pdf

@app.route('/')
@app.route('/index')
def index():
    return "yes"

@app.route('/najem', methods = ['GET', 'POST'])
def formularz_najmu():
    form = UmowaNajmu()
    if form.validate_on_submit():
        data = {
            'miejsce_zawarcia': form.miejsce_zawarcia.data,
            'data_zawarcia': form.data_zawarcia.data,
            'imie_wynajmujacego': form.imie_wynajmujacego.data,
            'nazwisko_wynajmujacego': form.nazwisko_wynajmujacego.data,
            'pesel_wynajmujacego': form.pesel_wynajmujacego.data,
            'imie_najemcy': form.imie_najemcy.data,
            'nazwisko_najemcy': form.nazwisko_najemcy.data,
            'pesel_najemcy': form.pesel_najemcy.data,
            'adres_lokalu': form.adres_lokalu.data,
            'wielkosc_lokalu': form.wielkosc_lokalu.data,
            'kwota_czynszu': form.kwota_czynszu.data,
            'kwota_kaucji': form.kwota_kaucji.data,
            'dni_kaucji': form.dni_kaucji.data,
            'data_zaplaty_czynszu': form.data_zaplaty_czynszu.data,
            'data_zakonczenia_umowy': form.data_zakonczenia_umowy.data
        }
        return create_pdf(data)
    return render_template('umowa_najmu.html', title='Umowa Najmu', form=form)

