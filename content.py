"""All copy and company facts for carsbuyusa.com.

Two rules govern this file, and both exist because the site's only job is to survive a bank
compliance check:

1. Identity facts live in FACTS, once. They are never translated and never retyped. All fifteen
   generated pages render them from here, so the English, Ukrainian, and Russian versions cannot
   drift apart. A compliance officer who translates the pages and finds three slightly different
   businesses is worse off than one who had a single language.

2. A fact that is not yet known is None. build.py omits its row and warns. It never becomes the
   string "TBD" -- on a page whose purpose is verification, a visible placeholder is worse than an
   absence.
"""

# --------------------------------------------------------------------------------------------
# Company identity. Verified against cbusa-audit/templates/agreement.html, which is the header
# printed on every invoice and purchase agreement the company issues. These MUST continue to match
# it: the invoice/site comparison is the check being run.
# --------------------------------------------------------------------------------------------

FACTS = {
    "legal_name": "Cars Buy USA Inc.",
    "address": ["300 W Service Rd, 2nd Floor", "Staten Island, New York 10314", "United States"],
    "ein": "92-3260990",
    "state": "New York, United States",
    # --- Owner to supply. Omitted from every page until filled in. --------------------------
    "dos_id": None,          # New York Department of State entity ID
    "incorporated": None,    # Date of incorporation, e.g. "14 June 2022"
    "phone": None,           # Public telephone number in +1 XXX XXX XXXX form
    # ---------------------------------------------------------------------------------------
    "email": "ops@carsbuyusa.com",  # MUST be a live, monitored mailbox before launch
    # Times only. Each language supplies the surrounding wording via "hours_format", so the hours
    # themselves are still single-sourced but a Ukrainian reader doesn't get an English sentence.
    "hours": "09:00–17:00",
}

DOMAIN = "carsbuyusa.com"
SITE_URL = f"https://{DOMAIN}"

# Order is fixed and shared by every language. build.py asserts all three supply exactly these.
PAGE_ORDER = ["index", "how-it-works", "services", "company", "contact"]

# Ukrainian precedes Russian: the primary client base is Ukrainian.
LANG_ORDER = ["en", "uk", "ru"]


# --------------------------------------------------------------------------------------------
# English
# --------------------------------------------------------------------------------------------

EN = {
    "locale": "en",
    "label": "English",
    "short": "EN",
    "tagline": "Vehicle purchase and export from the United States",
    "nav": {
        "index": "Home",
        "how-it-works": "How it works",
        "services": "Services",
        "company": "Company",
        "contact": "Contact",
    },
    "fact_labels": {
        "legal_name": "Legal name",
        "address": "Registered address",
        "ein": "EIN / Tax ID",
        "state": "State of incorporation",
        "dos_id": "NY DOS entity ID",
        "incorporated": "Date of incorporation",
        "email": "Email",
        "phone": "Telephone",
        "hours": "Business hours",
    },
    "hours_format": "Monday to Friday, {hours} Eastern Time (ET)",
    "footer_heading": "Company details",
    "footer_trademark": (
        "Copart and IAA are trademarks of their respective owners. "
        "Cars Buy USA Inc. is not affiliated with, endorsed by, or sponsored by them."
    ),
    "footer_rights": "All rights reserved.",
    "lang_switch_label": "Language",
    "skip_link": "Skip to content",
    "pages": {
        "index": {
            "h1": "Vehicle purchase and export from the United States",
            "desc": (
                "Cars Buy USA Inc. purchases vehicles at US auto auctions for clients abroad and "
                "handles title, export documentation, and shipping to the destination port."
            ),
            "lead": (
                "Cars Buy USA Inc. purchases vehicles at United States auto auctions on behalf of "
                "clients abroad, handles title and export documentation, and ships them to the "
                "destination port."
            ),
            "blocks": [
                {"type": "steps", "h2": "How a purchase works", "items": [
                    ("Purchase at auction",
                     "We locate the lot, buy it on the client's instruction, and settle payment "
                     "with the auction house."),
                    ("Title and export documents",
                     "We collect the title and prepare the export documentation the destination "
                     "country requires."),
                    ("Transport and ocean freight",
                     "The vehicle moves by road to the port, is loaded, and sails to the client's "
                     "destination port."),
                ]},
                {"type": "prose", "h2": "What we do", "paras": [
                    "Most auto auctions in the United States sell only to registered buyers, and a "
                    "buyer outside the country cannot simply bid, pay, collect a title, and arrange "
                    "export on their own. We do that work for them.",
                    "For each vehicle we confirm the lot and the total landed cost before anything "
                    "is committed, purchase the vehicle, settle with the auction, collect the "
                    "title, prepare the export paperwork, and arrange inland transport and ocean "
                    "freight to the destination port. The client receives a single invoice "
                    "identifying the exact vehicle by VIN and lot number.",
                ]},
                {"type": "prose", "h2": "Looking for a specific vehicle?", "paras": [
                    "Alongside our main business we source individual vehicles to order. If a "
                    "client is looking for a particular make, model, year, and specification, we "
                    "search the auctions and the dealer market on their behalf and report back with "
                    "what is available and what it would cost delivered.",
                ]},
                {"type": "prose", "h2": "Where we ship", "paras": [
                    "Our clients are principally in Ukraine and elsewhere in Europe. We ship to the "
                    "major container and roll-on/roll-off ports serving those markets.",
                ]},
            ],
        },
        "how-it-works": {
            "h1": "How it works",
            "desc": (
                "The six steps of a vehicle purchase and export, from quotation to delivery at the "
                "destination port, and what appears on every invoice."
            ),
            "lead": (
                "Every purchase follows the same six steps, and the client is invoiced once, for a "
                "specific identified vehicle."
            ),
            "blocks": [
                {"type": "steps", "h2": "The process", "numbered": True, "items": [
                    ("Request and quotation",
                     "The client tells us the vehicle, or the lot, they want. We confirm "
                     "availability and quote the total cost: the purchase price, auction fees, our "
                     "fee, inland transport, and ocean freight."),
                    ("Agreement and payment",
                     "The client receives a purchase agreement and an invoice identifying the "
                     "vehicle. Funds are transferred to the company account named on that invoice, "
                     "and nowhere else."),
                    ("Purchase at auction",
                     "We buy the vehicle and settle with the auction house within its payment "
                     "deadline. Auctions charge storage and can cancel a sale if payment is late, "
                     "so this step is time-critical and we handle it directly."),
                    ("Title and export documentation",
                     "We collect the title from the auction and prepare the documents required to "
                     "export the vehicle and to clear it at destination."),
                    ("Inland transport and loading",
                     "The vehicle is transported by road to the port of departure and loaded, in a "
                     "container or roll-on/roll-off, according to what the client has chosen."),
                    ("Ocean freight and delivery",
                     "The vehicle sails to the destination port. We pass the bill of lading and the "
                     "title to the client, who clears the vehicle at their end."),
                ]},
                {"type": "list", "h2": "What appears on every invoice",
                 "intro": "Each invoice we issue identifies one specific vehicle. It states:",
                 "items": [
                     "VIN",
                     "Year, make, and model",
                     "Auction lot or stock number",
                     "Odometer reading, and whether that reading is actual, exceeds mechanical "
                     "limits, or is not actual",
                     "Title status — whether the vehicle carries a clean or a salvage title",
                     "Purchase amount",
                     "Departure date",
                     "The buyer's name, address, and country",
                 ]},
                {"type": "prose", "h2": "Payment", "paras": [
                    "Wire instructions are issued only on the invoice we send to the client "
                    "directly. We never publish bank details on this website, and we do not change "
                    "payment instructions by email once an invoice has been issued.",
                    "If you receive a message that appears to come from us asking you to send funds "
                    "to a different account, telephone us before acting on it.",
                ]},
            ],
        },
        "services": {
            "h1": "Services",
            "desc": (
                "Auction purchase, export documentation and title, inland transport and ocean "
                "freight, and vehicle sourcing to order."
            ),
            "lead": (
                "Everything between a lot on a United States auction site and a vehicle at the "
                "client's port."
            ),
            "blocks": [
                {"type": "cards", "h2": None, "items": [
                    ("Auction purchase",
                     "We buy vehicles at United States auto auctions, including Copart and IAA, on "
                     "behalf of clients who cannot buy there directly. We confirm the total cost "
                     "before committing, purchase the vehicle, and settle with the auction within "
                     "its deadline."),
                    ("Export documentation and title",
                     "We collect the title and prepare the paperwork required to export the vehicle "
                     "from the United States and to clear it on arrival."),
                    ("Transport and ocean freight",
                     "Inland transport from the auction yard to the port of departure, loading in a "
                     "container or roll-on/roll-off, and ocean freight to the destination port."),
                    ("Vehicle sourcing to order",
                     "If a client wants a particular vehicle rather than a particular lot, we "
                     "search the auctions and the dealer market and report what is available, in "
                     "what condition, and at what delivered cost."),
                ]},
            ],
        },
        "company": {
            "h1": "Company details",
            "desc": (
                "Registered details of Cars Buy USA Inc., a corporation registered in the State of "
                "New York, United States."
            ),
            "lead": (
                "Cars Buy USA Inc. is a corporation registered in the State of New York, "
                "United States."
            ),
            "blocks": [
                {"type": "facts", "h2": "Registered details",
                 "note": "These details match those printed on every invoice and purchase "
                         "agreement we issue."},
                {"type": "prose", "h2": "Business activity", "paras": [
                    "The company purchases motor vehicles at auction and by private treaty within "
                    "the United States, on behalf of and for resale to buyers located outside the "
                    "United States, and arranges the documentation, inland transport, and ocean "
                    "freight required to export them.",
                    "Payments received from clients are for identified vehicles, invoiced "
                    "individually, each invoice stating the vehicle's VIN, lot number, and purchase "
                    "amount.",
                ]},
                {"type": "prose", "h2": "Verification", "paras": [
                    "Banks, auditors, and counterparties are welcome to contact us directly to "
                    "verify any invoice, agreement, or transaction. Requests sent to the address "
                    "below are answered on the same business day wherever possible.",
                ]},
            ],
        },
        "contact": {
            "h1": "Contact",
            "desc": "Contact details for Cars Buy USA Inc., Staten Island, New York.",
            "lead": (
                "Reach us by email or telephone. Requests to verify an invoice or agreement should "
                "go to the same address."
            ),
            "blocks": [
                {"type": "contact", "h2": None},
            ],
        },
    },
}


# --------------------------------------------------------------------------------------------
# Ukrainian
# --------------------------------------------------------------------------------------------

UK = {
    "locale": "uk",
    "label": "Українська",
    "short": "UA",
    "tagline": "Купівля та експорт автомобілів зі Сполучених Штатів",
    "nav": {
        "index": "Головна",
        "how-it-works": "Як це працює",
        "services": "Послуги",
        "company": "Компанія",
        "contact": "Контакти",
    },
    "fact_labels": {
        "legal_name": "Юридична назва",
        "address": "Юридична адреса",
        "ein": "EIN / податковий номер",
        "state": "Штат реєстрації",
        "dos_id": "Ідентифікатор у реєстрі штату Нью-Йорк (DOS ID)",
        "incorporated": "Дата реєстрації",
        "email": "Електронна пошта",
        "phone": "Телефон",
        "hours": "Робочі години",
    },
    "hours_format": "З понеділка по п’ятницю, {hours} за східним часом США (ET)",
    "footer_heading": "Реквізити компанії",
    "footer_trademark": (
        "Copart та IAA є торговельними марками відповідних власників. "
        "Cars Buy USA Inc. не пов’язана з ними, не є їхнім партнером і не має їхнього схвалення."
    ),
    "footer_rights": "Усі права захищено.",
    "lang_switch_label": "Мова",
    "skip_link": "Перейти до вмісту",
    "pages": {
        "index": {
            "h1": "Купівля та експорт автомобілів зі Сполучених Штатів",
            "desc": (
                "Cars Buy USA Inc. купує автомобілі на аукціонах США для клієнтів за кордоном, "
                "оформлює титул та експортні документи і доставляє їх до порту призначення."
            ),
            "lead": (
                "Cars Buy USA Inc. купує автомобілі на автомобільних аукціонах Сполучених "
                "Штатів за дорученням клієнтів за кордоном, оформлює титул та експортні "
                "документи і доставляє їх до порту призначення."
            ),
            "blocks": [
                {"type": "steps", "h2": "Як відбувається купівля", "items": [
                    ("Купівля на аукціоні",
                     "Ми знаходимо лот, купуємо його за дорученням клієнта та розраховуємося "
                     "з аукціоном."),
                    ("Титул і експортні документи",
                     "Ми отримуємо титул (документ про право власності) та готуємо "
                     "експортні документи, яких вимагає країна призначення."),
                    ("Перевезення та морський фрахт",
                     "Автомобіль перевозиться автотранспортом до порту, завантажується "
                     "і прямує морем до порту призначення клієнта."),
                ]},
                {"type": "prose", "h2": "Чим ми займаємося", "paras": [
                    "Більшість автомобільних аукціонів у Сполучених Штатах продають лише "
                    "зареєстрованим покупцям, і покупець за межами країни не може "
                    "самостійно взяти участь у торгах, оплатити лот, отримати титул та "
                    "організувати експорт. Ми виконуємо цю роботу за нього.",
                    "Для кожного автомобіля ми підтверджуємо лот і повну вартість із "
                    "доставкою ще до того, як будуть узяті будь-які зобов’язання, купуємо "
                    "автомобіль, розраховуємося з аукціоном, отримуємо титул, готуємо "
                    "експортні документи та організовуємо наземне перевезення і морський "
                    "фрахт до порту призначення. Клієнт отримує один рахунок, у якому "
                    "автомобіль ідентифіковано за VIN-кодом і номером лота.",
                ]},
                {"type": "prose", "h2": "Шукаєте конкретний автомобіль?", "paras": [
                    "Окрім основного напряму, ми підбираємо окремі автомобілі на замовлення. "
                    "Якщо клієнт шукає певну марку, модель, рік випуску та комплектацію, ми "
                    "шукаємо їх на аукціонах і на дилерському ринку та повідомляємо, що є "
                    "в наявності та скільки це коштуватиме з доставкою.",
                ]},
                {"type": "prose", "h2": "Куди ми відправляємо", "paras": [
                    "Наші клієнти — переважно в Україні та інших країнах Європи. Ми "
                    "відправляємо автомобілі до основних контейнерних портів і портів "
                    "ро-ро, що обслуговують ці ринки.",
                ]},
            ],
        },
        "how-it-works": {
            "h1": "Як це працює",
            "desc": (
                "Шість етапів купівлі та експорту автомобіля — від розрахунку вартості до "
                "доставки в порт призначення — та що зазначено в кожному рахунку."
            ),
            "lead": (
                "Кожна купівля проходить ті самі шість етапів, і клієнт отримує один "
                "рахунок за конкретний ідентифікований автомобіль."
            ),
            "blocks": [
                {"type": "steps", "h2": "Процес", "numbered": True, "items": [
                    ("Запит і розрахунок вартості",
                     "Клієнт повідомляє, який автомобіль або лот його цікавить. Ми "
                     "підтверджуємо наявність і називаємо повну вартість: ціну купівлі, "
                     "аукціонні збори, нашу винагороду, наземне перевезення та морський фрахт."),
                    ("Договір і оплата",
                     "Клієнт отримує договір купівлі та рахунок із зазначенням автомобіля. "
                     "Кошти перераховуються на рахунок компанії, вказаний у цьому рахунку, "
                     "і на жодний інший."),
                    ("Купівля на аукціоні",
                     "Ми купуємо автомобіль і розраховуємося з аукціоном у встановлений "
                     "ним строк. Аукціони нараховують плату за зберігання і можуть скасувати "
                     "продаж у разі затримки оплати, тому цей етап критичний за часом "
                     "і ми виконуємо його самостійно."),
                    ("Титул та експортні документи",
                     "Ми отримуємо титул від аукціону та готуємо документи, потрібні для "
                     "експорту автомобіля і для його митного оформлення в країні "
                     "призначення."),
                    ("Наземне перевезення та завантаження",
                     "Автомобіль перевозиться автотранспортом до порту відправлення "
                     "та завантажується — у контейнер або методом ро-ро, залежно від "
                     "вибору клієнта."),
                    ("Морський фрахт і доставка",
                     "Автомобіль прямує морем до порту призначення. Ми передаємо "
                     "клієнтові коносамент і титул, а він здійснює митне оформлення "
                     "на своєму боці."),
                ]},
                {"type": "list", "h2": "Що зазначено в кожному рахунку",
                 "intro": "Кожен виставлений нами рахунок ідентифікує один конкретний автомобіль. У ньому зазначено:",
                 "items": [
                     "VIN-код",
                     "Рік випуску, марку та модель",
                     "Номер лота або складський номер аукціону",
                     "Показник одометра та чи є він фактичним, чи перевищує механічну "
                     "межу, чи не є фактичним",
                     "Статус титулу — чистий (clean) або аварійний (salvage)",
                     "Суму купівлі",
                     "Дату відправлення",
                     "Ім’я, адресу та країну покупця",
                 ]},
                {"type": "prose", "h2": "Оплата", "paras": [
                    "Платіжні реквізити надаються виключно в рахунку, який ми надсилаємо "
                    "клієнтові безпосередньо. Ми ніколи не публікуємо банківські "
                    "реквізити на цьому сайті й не змінюємо платіжні інструкції "
                    "електронною поштою після виставлення рахунка.",
                    "Якщо ви отримали повідомлення нібито від нас із проханням "
                    "перерахувати кошти на інший рахунок, зателефонуйте нам, "
                    "перш ніж діяти.",
                ]},
            ],
        },
        "services": {
            "h1": "Послуги",
            "desc": (
                "Купівля на аукціоні, експортні документи та титул, наземне перевезення "
                "й морський фрахт, підбір автомобіля на замовлення."
            ),
            "lead": (
                "Усе, що між лотом на аукціоні у Сполучених Штатах і автомобілем "
                "у порту клієнта."
            ),
            "blocks": [
                {"type": "cards", "h2": None, "items": [
                    ("Купівля на аукціоні",
                     "Ми купуємо автомобілі на автомобільних аукціонах Сполучених "
                     "Штатів, зокрема Copart та IAA, за дорученням клієнтів, які не можуть "
                     "купувати там напряму. Ми підтверджуємо повну вартість до взяття "
                     "зобов’язань, купуємо автомобіль і розраховуємося з аукціоном "
                     "у встановлений строк."),
                    ("Експортні документи та титул",
                     "Ми отримуємо титул і готуємо документи, потрібні для експорту "
                     "автомобіля зі Сполучених Штатів та для його оформлення після "
                     "прибуття."),
                    ("Перевезення та морський фрахт",
                     "Наземне перевезення від майданчика аукціону до порту "
                     "відправлення, завантаження в контейнер або методом ро-ро "
                     "та морський фрахт до порту призначення."),
                    ("Підбір автомобіля на замовлення",
                     "Якщо клієнтові потрібен певний автомобіль, а не певний лот, "
                     "ми шукаємо його на аукціонах і на дилерському ринку та "
                     "повідомляємо, що є в наявності, у якому стані та за якою "
                     "вартістю з доставкою."),
                ]},
            ],
        },
        "company": {
            "h1": "Реквізити компанії",
            "desc": (
                "Реєстраційні дані Cars Buy USA Inc. — корпорації, зареєстрованої у "
                "штаті Нью-Йорк, США."
            ),
            "lead": (
                "Cars Buy USA Inc. — корпорація, зареєстрована у штаті Нью-Йорк, "
                "Сполучені Штати Америки."
            ),
            "blocks": [
                {"type": "facts", "h2": "Реєстраційні дані",
                 "note": "Ці дані збігаються з тими, що зазначені в кожному виставленому "
                         "нами рахунку та договорі купівлі."},
                {"type": "prose", "h2": "Вид діяльності", "paras": [
                    "Компанія купує транспортні засоби на аукціонах та за приватними "
                    "угодами на території Сполучених Штатів за дорученням "
                    "покупців, розташованих за межами Сполучених Штатів, і для "
                    "подальшого продажу їм, а також організовує оформлення "
                    "документів, наземне перевезення та морський фрахт, потрібні "
                    "для їх експорту.",
                    "Платежі, отримані від клієнтів, стосуються ідентифікованих "
                    "автомобілів і виставляються окремими рахунками; у кожному "
                    "рахунку зазначено VIN-код, номер лота та суму купівлі.",
                ]},
                {"type": "prose", "h2": "Перевірка", "paras": [
                    "Банки, аудитори та контрагенти можуть звертатися до нас "
                    "безпосередньо для перевірки будь-якого рахунка, договору чи "
                    "операції. На запити, надіслані на адресу, зазначену нижче, ми "
                    "відповідаємо, за можливості, того самого робочого дня.",
                ]},
            ],
        },
        "contact": {
            "h1": "Контакти",
            "desc": "Контактні дані Cars Buy USA Inc., Стейтен-Айленд, Нью-Йорк.",
            "lead": (
                "Зв’яжіться з нами електронною поштою або телефоном. Запити щодо "
                "перевірки рахунків і договорів надсилайте на ту саму адресу."
            ),
            "blocks": [
                {"type": "contact", "h2": None},
            ],
        },
    },
}


# --------------------------------------------------------------------------------------------
# Russian
# --------------------------------------------------------------------------------------------

RU = {
    "locale": "ru",
    "label": "Русский",
    "short": "RU",
    "tagline": "Покупка и экспорт автомобилей из Соединённых Штатов",
    "nav": {
        "index": "Главная",
        "how-it-works": "Как это работает",
        "services": "Услуги",
        "company": "Компания",
        "contact": "Контакты",
    },
    "fact_labels": {
        "legal_name": "Юридическое наименование",
        "address": "Юридический адрес",
        "ein": "EIN / налоговый номер",
        "state": "Штат регистрации",
        "dos_id": "Идентификатор в реестре штата Нью-Йорк (DOS ID)",
        "incorporated": "Дата регистрации",
        "email": "Электронная почта",
        "phone": "Телефон",
        "hours": "Рабочие часы",
    },
    "hours_format": "С понедельника по пятницу, {hours} по восточному времени США (ET)",
    "footer_heading": "Реквизиты компании",
    "footer_trademark": (
        "Copart и IAA являются товарными знаками соответствующих владельцев. "
        "Cars Buy USA Inc. не связана с ними, не является их партнёром и не имеет их одобрения."
    ),
    "footer_rights": "Все права защищены.",
    "lang_switch_label": "Язык",
    "skip_link": "Перейти к содержанию",
    "pages": {
        "index": {
            "h1": "Покупка и экспорт автомобилей из Соединённых Штатов",
            "desc": (
                "Cars Buy USA Inc. покупает автомобили на аукционах США для клиентов за "
                "рубежом, оформляет титул и экспортные документы и доставляет их "
                "в порт назначения."
            ),
            "lead": (
                "Cars Buy USA Inc. покупает автомобили на автомобильных аукционах "
                "Соединённых Штатов по поручению клиентов за рубежом, "
                "оформляет титул и экспортные документы и доставляет их в порт "
                "назначения."
            ),
            "blocks": [
                {"type": "steps", "h2": "Как происходит покупка", "items": [
                    ("Покупка на аукционе",
                     "Мы находим лот, покупаем его по поручению клиента и "
                     "рассчитываемся с аукционом."),
                    ("Титул и экспортные документы",
                     "Мы получаем титул (документ о праве собственности) и готовим "
                     "экспортные документы, которых требует страна назначения."),
                    ("Перевозка и морской фрахт",
                     "Автомобиль перевозится автотранспортом в порт, загружается "
                     "и следует морем в порт назначения клиента."),
                ]},
                {"type": "prose", "h2": "Чем мы занимаемся", "paras": [
                    "Большинство автомобильных аукционов в Соединённых Штатах "
                    "продают только зарегистрированным покупателям, и покупатель "
                    "за пределами страны не может самостоятельно участвовать в "
                    "торгах, оплатить лот, получить титул и организовать экспорт. "
                    "Мы выполняем эту работу за него.",
                    "По каждому автомобилю мы подтверждаем лот и полную "
                    "стоимость с доставкой до принятия каких-либо обязательств, "
                    "покупаем автомобиль, рассчитываемся с аукционом, получаем "
                    "титул, готовим экспортные документы и организуем наземную "
                    "перевозку и морской фрахт до порта назначения. Клиент "
                    "получает один счёт, в котором автомобиль идентифицирован по "
                    "VIN-коду и номеру лота.",
                ]},
                {"type": "prose", "h2": "Ищете конкретный автомобиль?", "paras": [
                    "Помимо основного направления мы подбираем отдельные "
                    "автомобили под заказ. Если клиент ищет определённую марку, "
                    "модель, год выпуска и комплектацию, мы ищем их на аукционах и "
                    "на дилерском рынке и сообщаем, что есть в наличии и сколько "
                    "это будет стоить с доставкой.",
                ]},
                {"type": "prose", "h2": "Куда мы отправляем", "paras": [
                    "Наши клиенты находятся преимущественно в Украине и других "
                    "странах Европы. Мы отправляем автомобили в основные "
                    "контейнерные порты и порты ро-ро, обслуживающие эти рынки.",
                ]},
            ],
        },
        "how-it-works": {
            "h1": "Как это работает",
            "desc": (
                "Шесть этапов покупки и экспорта автомобиля — от расчёта "
                "стоимости до доставки в порт назначения — и что указано в "
                "каждом счёте."
            ),
            "lead": (
                "Каждая покупка проходит одни и те же шесть этапов, и клиент "
                "получает один счёт за конкретный идентифицированный автомобиль."
            ),
            "blocks": [
                {"type": "steps", "h2": "Процесс", "numbered": True, "items": [
                    ("Запрос и расчёт стоимости",
                     "Клиент сообщает, какой автомобиль или лот его интересует. "
                     "Мы подтверждаем наличие и называем полную стоимость: цену "
                     "покупки, аукционные сборы, наше вознаграждение, наземную "
                     "перевозку и морской фрахт."),
                    ("Договор и оплата",
                     "Клиент получает договор купли-продажи и счёт с указанием "
                     "автомобиля. Средства перечисляются на счёт компании, "
                     "указанный в этом счёте, и ни на какой другой."),
                    ("Покупка на аукционе",
                     "Мы покупаем автомобиль и рассчитываемся с аукционом в "
                     "установленный им срок. Аукционы начисляют плату за хранение "
                     "и могут отменить продажу при задержке оплаты, поэтому этот "
                     "этап критичен по времени и мы выполняем его сами."),
                    ("Титул и экспортные документы",
                     "Мы получаем титул от аукциона и готовим документы, "
                     "необходимые для экспорта автомобиля и его таможенного "
                     "оформления в стране назначения."),
                    ("Наземная перевозка и погрузка",
                     "Автомобиль перевозится автотранспортом в порт отправления "
                     "и загружается — в контейнер или методом ро-ро, в зависимости "
                     "от выбора клиента."),
                    ("Морской фрахт и доставка",
                     "Автомобиль следует морем в порт назначения. Мы передаём "
                     "клиенту коносамент и титул, а он проводит таможенное "
                     "оформление на своей стороне."),
                ]},
                {"type": "list", "h2": "Что указано в каждом счёте",
                 "intro": "Каждый выставленный нами счёт идентифицирует один конкретный автомобиль. В нём указаны:",
                 "items": [
                     "VIN-код",
                     "Год выпуска, марка и модель",
                     "Номер лота или складской номер аукциона",
                     "Показание одометра и является ли оно фактическим, превышает ли "
                     "механический предел или не является фактическим",
                     "Статус титула — чистый (clean) или аварийный (salvage)",
                     "Сумма покупки",
                     "Дата отправления",
                     "Имя, адрес и страна покупателя",
                 ]},
                {"type": "prose", "h2": "Оплата", "paras": [
                    "Платёжные реквизиты предоставляются исключительно в счёте, "
                    "который мы направляем клиенту напрямую. Мы никогда не "
                    "публикуем банковские реквизиты на этом сайте и не меняем "
                    "платёжные инструкции по электронной почте после выставления "
                    "счёта.",
                    "Если вы получили сообщение якобы от нас с просьбой "
                    "перевести средства на другой счёт, позвоните нам, прежде чем "
                    "действовать.",
                ]},
            ],
        },
        "services": {
            "h1": "Услуги",
            "desc": (
                "Покупка на аукционе, экспортные документы и титул, наземная "
                "перевозка и морской фрахт, подбор автомобиля под заказ."
            ),
            "lead": (
                "Всё, что находится между лотом на аукционе в Соединённых "
                "Штатах и автомобилем в порту клиента."
            ),
            "blocks": [
                {"type": "cards", "h2": None, "items": [
                    ("Покупка на аукционе",
                     "Мы покупаем автомобили на автомобильных аукционах "
                     "Соединённых Штатов, в том числе Copart и IAA, по поручению "
                     "клиентов, которые не могут покупать там напрямую. Мы "
                     "подтверждаем полную стоимость до принятия обязательств, "
                     "покупаем автомобиль и рассчитываемся с аукционом в "
                     "установленный срок."),
                    ("Экспортные документы и титул",
                     "Мы получаем титул и готовим документы, необходимые для "
                     "экспорта автомобиля из Соединённых Штатов и для его "
                     "оформления по прибытии."),
                    ("Перевозка и морской фрахт",
                     "Наземная перевозка от площадки аукциона до порта "
                     "отправления, погрузка в контейнер или методом ро-ро и "
                     "морской фрахт до порта назначения."),
                    ("Подбор автомобиля под заказ",
                     "Если клиенту нужен определённый автомобиль, а не "
                     "определённый лот, мы ищем его на аукционах и на дилерском "
                     "рынке и сообщаем, что есть в наличии, в каком состоянии и по "
                     "какой стоимости с доставкой."),
                ]},
            ],
        },
        "company": {
            "h1": "Реквизиты компании",
            "desc": (
                "Регистрационные данные Cars Buy USA Inc. — корпорации, "
                "зарегистрированной в штате Нью-Йорк, США."
            ),
            "lead": (
                "Cars Buy USA Inc. — корпорация, зарегистрированная в штате "
                "Нью-Йорк, Соединённые Штаты Америки."
            ),
            "blocks": [
                {"type": "facts", "h2": "Регистрационные данные",
                 "note": "Эти данные совпадают с указанными в каждом выставленном "
                         "нами счёте и договоре купли-продажи."},
                {"type": "prose", "h2": "Вид деятельности", "paras": [
                    "Компания покупает транспортные средства на аукционах и по "
                    "частным сделкам на территории Соединённых Штатов по "
                    "поручению покупателей, находящихся за пределами Соединённых "
                    "Штатов, и для последующей продажи им, а также организует "
                    "оформление документов, наземную перевозку и морской фрахт, "
                    "необходимые для их экспорта.",
                    "Платежи, полученные от клиентов, относятся к идентифицированным "
                    "автомобилям и выставляются отдельными счетами; в каждом "
                    "счёте указаны VIN-код, номер лота и сумма покупки.",
                ]},
                {"type": "prose", "h2": "Проверка", "paras": [
                    "Банки, аудиторы и контрагенты могут обращаться к нам "
                    "напрямую для проверки любого счёта, договора или операции. "
                    "На запросы, направленные по адресу, указанному ниже, мы "
                    "отвечаем, по возможности, в тот же рабочий день.",
                ]},
            ],
        },
        "contact": {
            "h1": "Контакты",
            "desc": "Контактные данные Cars Buy USA Inc., Стейтен-Айленд, Нью-Йорк.",
            "lead": (
                "Свяжитесь с нами по электронной почте или по телефону. "
                "Запросы о проверке счетов и договоров направляйте по тому же адресу."
            ),
            "blocks": [
                {"type": "contact", "h2": None},
            ],
        },
    },
}


LANGS = {"en": EN, "uk": UK, "ru": RU}
