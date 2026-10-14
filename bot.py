
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

import os
TOKEN = os.environ["8871448974:AAGNLO9tQ_G5I0Ef7a4u0qNSy4mFtWoCw-E"]

# =====================================
# RETSEPTLAR
# Har bir retsept: masalliqlar va tayyorlanishi
# =====================================

retseptlar = {
    "🍲 Milliy taomlar": {
        "🍚 Osh": (
            "Guruch, go‘sht, sabzi, piyoz, yog‘, tuz, ziravorlar",
            "Piyoz va go‘shtni qovuring. Sabzi qo‘shing. Suv quying, "
            "guruchni soling va suv tortilgach, past olovda damlang."
        ),
        "🥟 Manti": (
            "Xamir, qiyma go‘sht, piyoz, tuz, murch",
            "Qiyma va piyozni aralashtiring. Xamirga solib tuging. "
            "Bug‘da taxminan 35–45 daqiqa pishiring."
        ),
        "🥘 Dimlama": (
            "Go‘sht, kartoshka, sabzi, piyoz, karam, pomidor",
            "Masalliqlarni yirik to‘g‘rab qozonga qatlamlang. "
            "Ozroq suv solib, qopqog‘ini yoping va past olovda dimlang."
        ),
        "🥣 Sho‘rva": (
            "Go‘sht, kartoshka, sabzi, piyoz, pomidor, suv",
            "Go‘shtni qaynatib, ko‘pigini oling. Sabzavotlarni qo‘shib, "
            "hammasi yumshaguncha past olovda pishiring."
        ),
        "🍜 Mastava": (
            "Guruch, go‘sht, sabzi, piyoz, kartoshka, pomidor",
            "Go‘sht va piyozni qovuring. Sabzavot hamda suv qo‘shing. "
            "Guruchni solib, pishguncha qaynatib oling."
        ),
        "🥢 Lag‘mon": (
            "Lag‘mon xamiri, go‘sht, qalampir, sabzi, piyoz, pomidor",
            "Go‘sht va sabzavotlarni qovurib, ozroq suv bilan pishiring. "
            "Xamirni alohida qaynatib, ustidan qayla quying."
        ),
        "🥟 Chuchvara": (
            "Xamir, qiyma, piyoz, tuz, murch, bulon",
            "Qiyma va piyozni aralashtirib xamirga tuging. "
            "Qaynayotgan bulonda to‘liq pishguncha qaynatib oling."
        ),
        "🍗 Qozon kabob": (
            "Go‘sht, kartoshka, piyoz, yog‘, tuz, ziravorlar",
            "Go‘shtni qozonda qovuring. Kartoshka va ziravorlarni qo‘shib, "
            "qopqoq ostida past olovda pishiring."
        ),
        "🥘 Moshkichiri": (
            "Mosh, guruch, go‘sht, piyoz, sabzi",
            "Piyoz va go‘shtni qovuring. Mosh va suv qo‘shing. "
            "Mosh yumshagach guruch solib, quyuqlashguncha pishiring."
        ),
        "🥚 Tuxum barak": (
            "Xamir, tuxum, sut yoki suv, tuz",
            "Xamirni yupqa yoying. Tuxumli aralashma solib chetlarini "
            "yoping. Qaynayotgan suvda to‘liq pishiring."
        )
    },

    "🌍 Chet el taomlari": {
        "🍕 Pitsa": (
            "Pitsa xamiri, pomidor sousi, pishloq, qo‘ziqorin yoki sabzavot",
            "Xamirga sous surting, masalliqlar va pishloq qo‘ying. "
            "220°C pechda taxminan 12–18 daqiqa pishiring."
        ),
        "🍝 Carbonara": (
            "Makaron, tuxum, qattiq pishloq, murch",
            "Makaronni qaynatib oling. Tuxum va pishloqni aralashtiring. "
            "Issiq makaron bilan aralashtirib, tuxum to‘liq pishganiga "
            "ishonch hosil qiling."
        ),
        "🍣 Sushi": (
            "Sushi guruchi, nori, bodring, avokado, pishgan baliq",
            "Guruchni pishirib sovuting. Nori ustiga yoyib, ichlik soling. "
            "O‘rab, bo‘laklarga kesing."
        ),
        "🍜 Ramen": (
            "Makaron, bulon, pishgan tovuq, tuxum, ko‘kat",
            "Makaronni pishiring. Issiq bulonga solib, ustiga pishgan "
            "tovuq, tuxum va ko‘kat qo‘shing."
        ),
        "🍙 Kimpab": (
            "Guruch, nori, sabzi, bodring, tuxum, pishgan go‘sht",
            "Guruchni nori ustiga yoying. Sabzavot va pishgan go‘shtni "
            "solib o‘rang, so‘ng bo‘laklarga kesing."
        ),
        "🥪 Sendvich": (
            "Non, pishloq, pomidor, salat bargi, pishgan tovuq",
            "Masalliqlarni non orasiga joylang. Xohlasangiz, tovaga "
            "qo‘yib pishloq eriguncha qizartiring."
        ),
        "🌮 Tako": (
            "Tortilya, pishgan qiyma yoki loviya, pomidor, pishloq",
            "Qiyma yoki loviyani pishiring. Tortilyaga solib, "
            "sabzavot va pishloq qo‘shing."
        ),
        "🍗 Tovuq naggets": (
            "Tovuq filesi, tuxum, un, suxari, tuz, ziravorlar",
            "Tovuqni bo‘laklang. Un, tuxum va suxariga bulang. "
            "Ichigacha to‘liq pishguncha pechda yoki tovda pishiring."
        ),
        "🥔 Kartoshka fri": (
            "Kartoshka, ozroq yog‘, tuz",
            "Kartoshkani tayoqcha qilib kesib, quriting. Pechda "
            "yoki mos usulda tillarang bo‘lguncha pishiring."
        ),
        "🍗 Qarsildoq tovuq": (
            "Tovuq, un, tuxum, suxari, ziravorlar",
            "Tovuqni ziravorlang va suxariga bulang. Ichki qismi "
            "to‘liq pishguncha pechda yoki tovda pishiring."
        )
    },

    "🥗 Salatlar": {
        "🥗 Grek salati": (
            "Pomidor, bodring, bulg‘or qalampiri, feta pishlog‘i, zaytun",
            "Sabzavotlarni to‘g‘rang. Pishloq va zaytun qo‘shib, "
            "ozroq zaytun yog‘i bilan aralashtiring."
        ),
        "🥗 Sezar salati": (
            "Salat bargi, pishgan tovuq, non qotirmasi, pishloq, sous",
            "Salat bargini yuvib quriting. Tovuq va non qotirmasini "
            "qo‘shib, sous va pishloq bilan aralashtiring."
        ),
        "🥗 Olivye": (
            "Kartoshka, sabzi, tuxum, no‘xat, bodring, mayonez",
            "Masalliqlarni pishirib sovuting. Kubik qilib to‘g‘rab, "
            "no‘xat va mayonez bilan aralashtiring."
        ),
        "🥗 Kapreze": (
            "Pomidor, mozzarella, rayhon, zaytun yog‘i",
            "Pomidor va mozzarellani kesib tering. Rayhon va ozroq "
            "zaytun yog‘i qo‘shing."
        ),
        "🥗 Kolslou": (
            "Karam, sabzi, yogurt yoki mayonez, limon sharbati",
            "Karam va sabzini ingichka to‘g‘rang. Sous bilan "
            "aralashtirib, biroz tindiring."
        ),
        "🥗 Tovuqli ananas salati": (
            "Pishgan tovuq, ananas, pishloq, yogurt yoki mayonez",
            "Tovuq va ananasni to‘g‘rang. Pishloq va sous bilan "
            "aralashtiring."
        ),
        "🥗 Koreyscha sabzi": (
            "Sabzi, sarimsoq, yog‘, sirka, tuz, koriandr",
            "Sabzini uzun qilib qiring. Sarimsoq, ziravor va sirka "
            "qo‘shib aralashtiring, sovutkichda tindiring."
        ),
        "🥗 Mimoza": (
            "Konserva baliq, kartoshka, sabzi, tuxum, pishloq, mayonez",
            "Masalliqlarni pishirib qiring. Qatlamlab terib, "
            "har qatlamga ozroq mayonez surting."
        ),
        "🥗 Meksikacha loviya": (
            "Pishgan loviya, makkajo‘xori, pomidor, qalampir, limon",
            "Masalliqlarni aralashtiring. Limon sharbati va ko‘kat "
            "qo‘shing."
        ),
        "🥗 Makaronli salat": (
            "Makaron, bodring, pomidor, makkajo‘xori, yogurtli sous",
            "Makaronni pishirib sovuting. Sabzavotlar va sous bilan "
            "aralashtiring."
        )
    },

    "🍳 Yengil nonushtalar": {
        "🧀 Pishloqli sendvich": (
            "Non, pishloq, pomidor yoki ko‘kat",
            "Masalliqlarni non orasiga qo‘ying va tovda pishloq "
            "eriguncha qizartiring."
        ),
        "🥞 Pankeyk": (
            "Un, sut, tuxum, ozroq shakar, qabartma",
            "Masalliqlarni aralashtiring. Tovaga oz-ozdan quyib, "
            "ikki tomonini pishiring."
        ),
        "🥔 Kartoshkali omlet": (
            "Tuxum, kartoshka, piyoz, tuz",
            "Kartoshkani mayda to‘g‘rab pishiring. Ko‘pirtirilgan "
            "tuxum qo‘shib, tuxum to‘liq pishguncha ushlang."
        ),
        "🌯 Pishloqli lavash": (
            "Lavash, pishloq, pomidor, ko‘kat",
            "Masalliqlarni lavashga solib o‘rang. Tovada ikki "
            "tomonini qizartiring."
        ),
        "🍎 Olmali quymoq": (
            "Olma, tuxum, un, sut, ozroq shakar",
            "Olmani qiring. Tuxum, sut va un bilan aralashtirib, "
            "kichik quymoqlar qilib pishiring."
        ),
        "🥣 Sutli bo‘tqa": (
            "Sut, suli yormasi yoki guruch, suv, ozroq tuz",
            "Yorma va sutni past olovda aralashtirib, yumshaguncha "
            "pishiring."
        ),
        "🥚 Tuxumli rulet": (
            "Tuxum, pishloq, ko‘kat",
            "Tuxumni ko‘pirtirib yupqa omlet tayyorlang. Pishloq "
            "va ko‘kat solib o‘rang; tuxum to‘liq pishsin."
        )
    },

    "🍰 Shirinliklar": {
        "🍯 Medovik": (
            "Asal, un, tuxum, shakar, sariyog‘, smetana",
            "Asalli xamir qatlamlarini pishiring. Sovuting, krem "
            "surting va sovutkichda tindiring."
        ),
        "🍫 Brownie": (
            "Shokolad, sariyog‘, tuxum, shakar, un, kakao",
            "Shokolad va sariyog‘ni eriting. Qolgan masalliqlarni "
            "aralashtirib, 175°C pechda pishiring."
        ),
        "🧁 Kapkeyk": (
            "Un, tuxum, shakar, sut, sariyog‘, qabartma",
            "Masalliqlarni aralashtirib qoliplarga quying. "
            "180°C pechda 18–22 daqiqa pishiring."
        ),
        "🥐 Kruassan": (
            "Kruassan xamiri, sariyog‘, tuxum surtmasi",
            "Xamirni uchburchak qilib kesib o‘rang. Ustiga tuxum "
            "surting va tillarang bo‘lguncha pishiring."
        ),
        "🍮 Ekler": (
            "Suv, sariyog‘, un, tuxum, sutli krem",
            "Suv, sariyog‘ va un bilan xamir tayyorlang, tuxum "
            "qo‘shing. Pishirib, sovigach krem bilan to‘ldiring."
        ),
        "☁️ Pavlova": (
            "Tuxum oqi, shakar, kraxmal, qaymoq, mevalar",
            "Tuxum oqini shakar bilan ko‘pirtirib, past haroratda "
            "quritib pishiring. Sovigach qaymoq va meva qo‘ying."
        ),
        "🧀 San-Sebastyan chizkeyki": (
            "Qaymoqli pishloq, qaymoq, tuxum, shakar, ozroq un",
            "Masalliqlarni silliq aralashtiring. Qolipda yuqori "
            "haroratda usti qizarguncha pishiring."
        ),
        "🍯 Asalli rulet": (
            "Tuxum, asal, un, shakar, qaymoqli krem",
            "Yupqa biskvit pishiring. Sovigach krem surting "
            "va ehtiyotkorlik bilan o‘rang."
        ),
        "☕ Tiramisu": (
            "Savoyardi pechenyesi, mascarpone, qahva, kakao",
            "Pechenyeni sovigan qahvaga tez botiring. Krem bilan "
            "qatlamlang va sovutkichda tindiring."
        ),
        "🥞 Blinchik": (
            "Un, sut, tuxum, tuz, yog‘",
            "Suyuq xamir tayyorlang. Tovaga yupqa qilib quyib, "
            "ikki tomonini pishiring."
        ),
        "🍫 Kinder Delice": (
            "Kakao, un, tuxum, shakar, sut, qaymoqli krem, shokolad",
            "Kakao qo‘shilgan biskvit pishiring. Sovigach krem "
            "surting va ustini shokolad bilan qoplang."
        ),
        "🎂 Napoleon": (
            "Qatlama xamir, sut, tuxum, shakar, un, sariyog‘",
            "Xamir qatlamlarini pishiring. Sutli krem tayyorlab, "
            "qatlamlar orasiga surting va sovutkichda tindiring."
        ),
        "🌀 Sinnabon": (
            "Un, sut, xamirturush, shakar, sariyog‘, dolchin",
            "Xamirni qorib oshiring. Yoyib, sariyog‘, shakar va "
            "dolchin surting. O‘rab kesing va pishiring."
        ),
        "❤️ Red Velvet": (
            "Un, kakao, tuxum, shakar, sut yoki kefir, krem pishloq",
            "Biskvit masalliqlarini aralashtirib pishiring. Sovigach "
            "qatlamlar orasiga krem surting."
        ),
        "🍫 Snickers torti": (
            "Biskvit, yeryong‘oq, karamel, shokolad, qaymoq",
            "Biskvit pishiring. Karamel va yeryong‘oq qatlamini "
            "qo‘shib, ustini shokolad bilan qoplang."
        )
    }
}

# =====================================
# MENYULAR
# =====================================

ASOSIY = [
    ["🆓 Bepul tarif", "👑 Premium tarif"],
    ["🍲 Milliy taomlar", "🌍 Chet el taomlari"],
    ["🥗 Salatlar", "🍳 Yengil nonushtalar"],
    ["🍰 Shirinliklar"],
    ["🔎 Retsept qidirish", "ℹ️ Yordam"]
]

def asosiy_menyu():
    return ReplyKeyboardMarkup(
        ASOSIY,
        resize_keyboard=True
    )

def bolim_menyu(bolim):
    nomlar = list(retseptlar[bolim].keys())
    qatorlar = [
        nomlar[i:i + 2]
        for i in range(0, len(nomlar), 2)
    ]
    qatorlar.append(["⬅️ Bosh menyu"])
    return ReplyKeyboardMarkup(
        qatorlar,
        resize_keyboard=True
    )

# =====================================
# /start
# =====================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    context.user_data["bolim"] = None
    await update.message.reply_text(
        "Assalomu alaykum! 🍽\n"
        "Retseptlar botiga xush kelibsiz!\n\n"
        "Kerakli bo‘limni tanlang 👇",
        reply_markup=asosiy_menyu()
    )

# =====================================
# TUGMALAR ISHLOVCHISI
# =====================================

async def tugmalar(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    matn = update.message.text.strip()

    if matn == "⬅️ Bosh menyu":
        context.user_data["bolim"] = None
        await update.message.reply_text(
            "Asosiy menyu 👇",
            reply_markup=asosiy_menyu()
        )
        return

    if matn == "🆓 Bepul tarif":
        await update.message.reply_text(
            "🆓 Bepul tarif\n\n"
            "Quyidagi bo‘limlardagi retseptlarni tanlang. "
            "Hozircha barcha ko‘rsatilgan retseptlar bepul.",
            reply_markup=asosiy_menyu()
        )
        return

    if matn == "👑 Premium tarif":
        await update.message.reply_text(
            "👑 PREMIUM TARIF\n\n"
            "Bu bo‘lim keyinchalik maxsus retseptlar va "
            "obuna to‘loviga ulanadi.\n"
            "Hozircha haqiqiy to‘lov yoqilmagan.",
            reply_markup=asosiy_menyu()
        )
        return

    if matn == "🔎 Retsept qidirish":
        await update.message.reply_text(
            "Taom nomini yozing. Masalan: Osh, Pitsa yoki Medovik."
        )
        return

    if matn == "ℹ️ Yordam":
        await update.message.reply_text(
            "Kerakli bo‘lim tugmasini bosing. "
            "Retseptni ochish uchun uning nomini tanlang.",
            reply_markup=asosiy_menyu()
        )
        return

    # Bo‘lim tanlanganmi?
    if matn in retseptlar:
        context.user_data["bolim"] = matn
        await update.message.reply_text(
            f"{matn} bo‘limini tanladingiz. Retseptni bosing 👇",
            reply_markup=bolim_menyu(matn)
        )
        return

    # Tanlangan bo‘limdagi retseptni topish
    bolim = context.user_data.get("bolim")
    if bolim and matn in retseptlar[bolim]:
        masalliqlar, tayyorlash = retseptlar[bolim][matn]
        await update.message.reply_text(
            f"{matn}\n\n"
            f"🛒 Masalliqlar:\n{masalliqlar}\n\n"
            f"👩‍🍳 Tayyorlanishi:\n{tayyorlash}\n\n"
            "Yoqimli ishtaha! 😋"
        )
        return

    # Qidiruv
    qidiruv = matn.casefold()
    for nomlar in retseptlar.values():
        for nom, malumot in nomlar.items():
            if qidiruv in nom.casefold():
                await update.message.reply_text(
                    f"{nom}\n\n"
                    f"🛒 Masalliqlar:\n{malumot[0]}\n\n"
                    f"👩‍🍳 Tayyorlanishi:\n{malumot[1]}"
                )
                return

    await update.message.reply_text(
        "Bu nomdagi retsept topilmadi. "
        "Menyudan bo‘lim tanlang yoki boshqa nom yozing.",
        reply_markup=asosiy_menyu()
    )

# =====================================
# BOTNI ISHGA TUSHIRISH
# =====================================

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        tugmalar
    )
)

print("Bot ishga tushmoqda...")
app.run_polling()
