from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import requests
from loader import dp

flags = {
    "USD": "🇺🇸",
    "EUR": "🇪🇺",
    "RUB": "🇷🇺",
    "GBP": "🇬🇧",
    "JPY": "🇯🇵",
    "AZN": "🇦🇿",
    "BDT": "🇧🇩",
    "BGN": "🇧🇬",
    "BHD": "🇧🇭",
    "BND": "🇧🇳",
    "BRL": "🇧🇷",
    "BYN": "🇧🇾",
    "CAD": "🇨🇦",
    "CHF": "🇨🇭",
    "CNY": "🇨🇳",
    "CUP": "🇨🇺",
    "CZK": "🇨🇿",
    "DKK": "🇩🇰",
    "DZD": "🇩🇿",
    "EGP": "🇪🇬",
    "AFN": "🇦🇫",
    "ARS": "🇦🇷",
    "GEL": "🇬🇪",
    "HKD": "🇭🇰",
    "HUF": "🇭🇺",
    "IDR": "🇮🇩",
    "ILS": "🇮🇱",
    "INR": "🇮🇳",
    "IQD": "🇮🇶",
    "IRR": "🇮🇷",
    "ISK": "🇮🇸",
    "JOD": "🇯🇴",
    "AUD": "🇦🇺",
    "KGS": "🇰🇬",
    "KHR": "🇰🇭",
    "KRW": "🇰🇷",
    "KWD": "🇰🇼",
    "KZT": "🇰🇿",
    "LAK": "🇱🇦",
    "LBP": "🇱🇧",
    "LYD": "🇱🇾",
    "MAD": "🇲🇦",  # Marokash dirhami
    "MDL": "🇲🇩",  # Moldaviya leyi
    "MMK": "🇲🇲",  # Myanma k'yati
    "MNT": "🇲🇳",  # Mongoliya tugriki
    "MXN": "🇲🇽",  # Meksika pesosi
    "MYR": "🇲🇾",  # Malayziya ringgiti
    "NOK": "🇳🇴",  # Norvegiya kronasi
    "NZD": "🇳🇿",  # Yangi Zelandiya dollari
    "OMR": "🇴🇲",  # Ummon riali
    "PHP": "🇵🇭",  # Filippin pesosi
    "PKR": "🇵🇰",  # Pokiston rupiyasi
    "PLN": "🇵🇱",  # Polsha zlotiysi
    "QAR": "🇶🇦",  # Qatar riali
    "RON": "🇷🇴",  # Ruminiya leyi
    "RSD": "🇷🇸",  # Serbiya dinori
    "AMD": "🇦🇲",  # Armaniston drami
    "SAR": "🇸🇦",  # Saudiya Arabistoni riali
    "SDG": "🇸🇩",  # Sudan funti
    "SEK": "🇸🇪",  # Shvetsiya kronasi
    "SGD": "🇸🇬",  # Singapur dollari
    "SYP": "🇸🇾",  # Suriya funti
    "THB": "🇹🇭",  # Tailand bati
    "TJS": "🇹🇯",  # Tojikiston somonisi
    "TMT": "🇹🇲",  # Turkmaniston manati
    "TND": "🇹🇳",  # Tunis dinori
    "TRY": "🇹🇷",  # Turkiya lirasi
    "UAH": "🇺🇦",  # Ukraina grivnasi
    "AED": "🇦🇪",  # BAA dirhami
    "UYU": "🇺🇾",  # Urugvay pesosi
    "VES": "🇻🇪",  # Venesuela bolivari
    "VND": "🇻🇳",  # Vetnam dongi
    "XDR": "🌐",    # SDR
    "YER": "🇾🇪",  # Yaman riali
    "ZAR": "🇿🇦"   # Janubiy Afrika randi

}

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    url = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    response = url.json()

    valyutalar = []
    for item in response:
        valyuta_nomi = item['CcyNm_UZ']
        valyuta_kursi = item['Rate']
        valyuta_code = item['Ccy']

        bayroq = flags.get(valyuta_code, "")

        valyutalar.append(f"{bayroq} 1 {valyuta_nomi} ~ {valyuta_kursi}\n")

    await message.answer("\n".join(valyutalar))

@dp.message_handler(commands='onesatart')
async def bot_start(message: types.Message):
    urls = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    emanzil = urls.json()
    bayrak = []
    await message.reply("davlatni kiriting!!!")


    for items in emanzil:
        valyutanomi=items['CcyNm_UZ']
        valyutakursi=items['Rate']
        valyutakode=items['Ccy']

        bayroqlar = flags.get(valyutakode, "")

        bayrak.append(f"{bayroqlar} 1 {valyutanomi} ~ {valyutakursi}\n")

        if bayrak:
            await message.answer("\n".join(bayrak))
        else:
            await message.answer("Ma'lumotlar mavjud emas.")


