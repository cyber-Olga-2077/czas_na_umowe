from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from flask import make_response
import textwrap
from docxtpl import DocxTemplate
from flask import send_file

def create_pdf_najem(data):
    response = make_response()
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=umowa_najmu.pdf'


    c = canvas.Canvas(response.stream, pagesize=letter)

    pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
    c.setFont("Verdana", 8)


    text = c.beginText(40, 750)
    text.textLine(f"{data['miejsce_zawarcia']}, {data['data_zawarcia'].strftime('%d-%m-%Y')}")
    text.textLine("Umowa Najmu")
    text.textLine("Umowa zostaje zawarta między:")
    text.textLine(f"{data['imie_wynajmujacego']} {data['nazwisko_wynajmujacego']}, PESEL: {data['pesel_wynajmujacego']}, zwanym dalej Wynajmującym")
    text.textLine("a")
    text.textLine(f"{data['imie_najemcy']} {data['nazwisko_najemcy']}, PESEL: {data['pesel_najemcy']}, zwanym dalej Najemcą.")
    text.textLine(f"Umowa tyczy się nieruchomości znajdującej się na {data['adres_lokalu']}, o powierzchni {data['wielkosc_lokalu']}m^2.")
    text.textLine(f"Czynsz za wynajem wynosi miesięcznie {data['kwota_czynszu']}. Kaucja za lokal wynosi {data['kwota_kaucji']}.")
    text.textLine(f"Kaucja musi zostać uiszczona {data['dni_kaucji']} dni po zawarciu umowy.")
    text.textLine(f"Czynsz należy uiszczać do {data['data_zaplaty_czynszu']} dnia każdego miesiąca.")
    text.textLine(f"Umowa obowiązuje do {data['data_zakonczenia_umowy'].strftime('%d-%m-%Y')}.")

    c.drawText(text)
    c.showPage()
    c.save()
    return response

def create_pdf_pojazd(data):
    from io import BytesIO
    doc_buffer = BytesIO()
    doc=DocxTemplate("app/templates/umowa_auto.docx")
    context=data
    doc.render(context)
    doc.save(doc_buffer)
    doc_buffer.seek(0)
    # response = make_response()
    # response.headers['Content-Type'] = 'application/docx'
    # response.headers['Content-Disposition'] = 'attachment; filename=umowa_sprzedazypojazdu.docx'

    # c = canvas.Canvas(response.stream, pagesize=letter)
    # pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
    # c.setFont("Verdana", 10)

    # text_lines = [
    #     "Umowa Sprzedaży Pojazdu",
    #     f"Umowa zawarta dnia {data['data_zawarcia'].strftime('%d-%m-%Y')} w miejscowości {data['miejsce_zawarcia']} pomiędzy:",
    #     f"{data['imie_sprzedajacego']} {data['nazwisko_sprzedajacego']}",
    #     f"zamieszkałą/łym w {data['miasto_sprzedajacego']} przy {data['ulica_sprzedajacego']} {data['numer_sprzedajacego']}, legitymującą/cym się dowodem osobistym {data['dowod_sprzedajacego']} wydanym przez {data['wydawca_sprzedajacego']}, nr PESEL: {data['pesel_sprzedajacego']}, nazywana/y dalej Sprzedającą/cym",
    #     "a",
    #     f"{data['imie_kupujacego']} {data['nazwisko_kupujacego']}",
    #     f"zamieszkałą/łym w {data['miasto_kupujacego']} przy {data['ulica_kupujacego']} {data['numer_kupujacego']}, legitymującą/cym się dowodem osobistym {data['dowod_kupujacego']} wydanym przez {data['wydawca_kupujacego']} nr PESEL: {data['pesel_kupujacego']}, nazywana/y dalej Kupującą/cym",
    #     "§ 1",
    #     f"Przedmiotem umowy jest sprzedaż pojazdu marki {data['marka_auta']}, model {data['model_auta']}, rok produkcji {data['rok_produkcji']}, numer nadwozia {data['numer_vin']}, numer rejestracyjny {data['numer_rejestracyjny']}, przebieg {data['przebieg']} km.",
    #     "§ 2",
    #     "Sprzedający oświadcza, że pojazd określony w §1 stanowi jego własność, jest wolny od wad fizycznych i prawnych oraz nie stanowi przedmiotu zabezpieczenia.",
    #     "§ 3",
    #     "Sprzedający przenosi na rzecz Kupującego własność w/w pojazdu za kwotę określoną w §4 niniejszej umowy.",
    #     "§ 4",
    #     f"Strony ustaliły wartość przedmiotu umowy na kwotę: {data['cena']} zł.",
    #     "§ 5",
    #     "Strony zgodnie oświadczają, że wszelkiego rodzaju koszty wynikające z realizacji ustaleń niniejszej umowy w tym koszty opłaty skarbowej poniesie Kupujący.",
    #     "§ 6",
    #     "W sprawach nieuregulowanych niniejszą umową mają zastosowanie przepisy Kodeksu Cywilnego. ",
    #     "§ 7",
    #     "Umowę niniejszą sporządzono w dwóch jednobrzmiących egzemplarzach, po jednym dla każdej ze stron."
    # ]

    # # text = c.beginText(40, 750)
    # y = 750
    # for line in text_lines:
    #     lines = textwrap.wrap(line, width=100)
    #     for wrapped_line in lines:
    #         c.drawString(40, y, wrapped_line)
    #         y -= 20

    # # c.drawText(text)
    # c.showPage()
    # c.save()

    # return response
    # return send_file(doc_path, as_attachment=True)
    return send_file(doc_buffer, as_attachment=True, download_name="generated_umowa_auto.docx")
