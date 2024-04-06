from app import app
from flask import render_template, flash, redirect
from app.forms import UmowaNajmu
from app.creating_pdf import create_pdf_najem
from app.forms import UmowaAuto
from app.creating_pdf import create_pdf_pojazd

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Strona Główna')

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
        return create_pdf_najem(data)
    return render_template('umowa_najmu.html', title='Umowa Najmu', form=form)

@app.route('/auto', methods = ['GET', 'POST'])
def formularz_auta():
    import json
    with open("data.json", "r", encoding='utf-8') as f:
        data_json = json.load(f)
        from datetime import datetime

        date_str = data_json["data_zawarcia"]
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        data_json["data_zawarcia"] = date_obj

    form = UmowaAuto(**data_json)
    
    if form.validate_on_submit():
        data = {
            'miejsce_zawarcia': form.miejsce_zawarcia.data,
            'data_zawarcia': form.data_zawarcia.data,
            'imie_sprzedajacego': form.imie_sprzedajacego.data,
            'nazwisko_sprzedajacego': form.nazwisko_sprzedajacego.data,
            'miasto_sprzedajacego': form.miasto_sprzedajacego.data,
            'ulica_sprzedajacego': form.ulica_sprzedajacego.data,
            'numer_sprzedajacego': form.numer_sprzedajacego.data,
            'pesel_sprzedajacego': form.pesel_sprzedajacego.data,
            'dowod_sprzedajacego': form.dowod_sprzedajacego.data,
            'wydawca_sprzedajacego': form.wydawca_sprzedajacego.data,
            'imie_kupujacego': form.imie_kupujacego.data,
            'nazwisko_kupujacego': form.nazwisko_kupujacego.data,
            'miasto_kupujacego': form.miasto_kupujacego.data,
            'ulica_kupujacego': form.ulica_kupujacego.data,
            'numer_kupujacego': form.numer_kupujacego.data,
            'pesel_kupujacego': form.pesel_kupujacego.data,
            'dowod_kupujacego': form.dowod_kupujacego.data,
            'wydawca_kupujacego': form.wydawca_kupujacego.data,
            'marka_auta': form.marka_auta.data,
            'model_auta': form.model_auta.data,
            'rok_produkcji': form.rok_produkcji.data,
            'numer_rejestracyjny': form.numer_rejestracyjny.data,
            'numer_vin': form.numer_vin.data,
            'cena': form.cena.data,
            'przebieg_start': form.przebieg_start.data,
            'przebieg_pokonany': form.przebieg_pokonany.data,

        }
        return create_pdf_pojazd(data)
    return render_template('umowa_auto.html', title='Umowa Sprzedaży Pojazdu', form=form)