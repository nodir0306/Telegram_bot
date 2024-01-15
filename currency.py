import requests
def currensy():
    dct = {}
    url = "https://nbu.uz/exchange-rates/json"
    response = requests.get(url)
    malumot = response.json()
    for kurs in malumot:
        if kurs["code"] == "EUR" or kurs["code"] == "USD" or kurs["code"] == "RUB":
            dct[kurs["title"]] = kurs["cb_price"]
    return f"""
Hozirgi kunda valyuta kursi:    
💶{list(dct.keys())[0]} :    {list(dct.values())[0]} so'm \n
💲{list(dct.keys())[1]} :    {list(dct.values())[1]} so'm \n
®️{list(dct.keys())[2]} :    {list(dct.values())[2]} so'm \n
"""

