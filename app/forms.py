from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TimeField, SelectField
from wtforms.validators import DataRequired


class UmowaNajmu(FlaskForm):

    miejsce_zawarcia = StringField('Miejsce zawarcia', validators=[DataRequired()])
    data_zawarcia = DateField('Data zawarcia', validators=[DataRequired()])
    imie_wynajmujacego = StringField('Imię wynajmującego', validators=[DataRequired()])
    nazwisko_wynajmujacego = StringField('Nazwisko wynajmującego', validators=[DataRequired()])
    pesel_wynajmujacego = StringField('PESEL wynajmującego', validators=[DataRequired()])
    imie_najemcy = StringField('Imię najemcy', validators=[DataRequired()])
    nazwisko_najemcy = StringField('Nazwisko najemcy', validators=[DataRequired()])
    pesel_najemcy = StringField('PESEL najemcy', validators=[DataRequired()])
    adres_lokalu = StringField('Adres lokalu', validators=[DataRequired()])
    wielkosc_lokalu = StringField('Wielkość lokalu', validators=[DataRequired()])
    kwota_czynszu = StringField('Kwota czynszu', validators=[DataRequired()])
    kwota_kaucji = StringField('Kwota kaucji', validators=[DataRequired()])
    dni_kaucji = StringField('Dni kaucji', validators=[DataRequired()])
    data_zaplaty_czynszu = StringField('Data zapłaty czynszu', validators=[DataRequired()])
    data_zakonczenia_umowy = DateField('Data zakończenia umowy', validators=[DataRequired()])
    submit = SubmitField('Utwórz umowę najmu')

class UmowaAuto(FlaskForm):

    miejsce_zawarcia = StringField('Miejsce zawarcia', validators=[DataRequired()])
    data_zawarcia = DateField('Data zawarcia', validators=[DataRequired()])
    imie_sprzedajacego = StringField('Imię sprzedającego', validators=[DataRequired()])
    nazwisko_sprzedajacego = StringField('Nazwisko sprzedającego', validators=[DataRequired()])
    pesel_sprzedajacego = StringField('PESEL sprzedającego', validators=[DataRequired()])
    imie_kupujacego = StringField('Imię kupującego', validators=[DataRequired()])
    nazwisko_kupujacego = StringField('Nazwisko kupującego', validators=[DataRequired()])
    pesel_kupujacego = StringField('PESEL kupującego', validators=[DataRequired()])
    marka_auta = StringField('Marka auta', validators=[DataRequired()])
    model_auta = StringField('Model auta', validators=[DataRequired()])
    rok_produkcji = StringField('Rok produkcji', validators=[DataRequired()])
    numer_rejestracyjny = StringField('Numer rejestracyjny', validators=[DataRequired()])
    przebieg = StringField('Przebieg', validators=[DataRequired()])
    numer_vim = StringField('Numer VIM', validators=[DataRequired()])
    cena = StringField('Cena', validators=[DataRequired()])
    submit = SubmitField('Utwórz umowę sprzedaży auta')


class UmowaKupno(FlaskForm):

    miejsce_zawarcia = StringField('Miejsce zawarcia', validators=[DataRequired()])
    data_zawarcia = DateField('Data zawarcia', validators=[DataRequired()])
    imie_sprzedajacego = StringField('Imię sprzedającego', validators=[DataRequired()])
    nazwisko_sprzedajacego = StringField('Nazwisko sprzedającego', validators=[DataRequired()])
    pesel_sprzedajacego = StringField('PESEL sprzedającego', validators=[DataRequired()])
    imie_kupujacego = StringField('Imię kupującego', validators=[DataRequired()])
    nazwisko_kupujacego = StringField('Nazwisko kupującego', validators=[DataRequired()])
    pesel_kupujacego = StringField('PESEL kupującego', validators=[DataRequired()])
    submit = SubmitField('Utwórz umowę kupna')