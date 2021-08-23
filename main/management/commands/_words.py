def getword(word, lang):
    language = {
        '1': {
            'uz': 'Yotoq soni',
            'ru': 'Кол-во спальных мест',
            'en': 'Count of beds'
        },
        '2': {
            'uz': 'Nonushta',
            'ru': 'Завтрак',
            'en': 'Breakfast'
        },
        '3': {
            'uz': 'Yosh bolalar',
            'ru': 'Дети',
            'en': 'Children'
        },
        '4': {
            'uz': 'Uy hayvoni',
            'ru': 'Домашние питомцы',
            'en': 'Pets'
        },
        '5': {
            'uz': 'Band qilish',
            'ru': 'Забронировать',
            'en': 'Book'
        },
        '6': {
            'uz': 'Orqaga',
            'ru': 'Назад ',
            'en': 'Back'
        },
        '7': {
            'uz': '''
            Xona narxiga 2 kishilik nonushta kiradi. 3 yoshgacha bo'lgan bolalarga - nonushta bepul. 3 yoshdan ortiq -
          Bir kishiga 100.000 so'm.
      Shuningdek, siz mehmonlar ixtiyorida mehmonxona xonasini ijaraga olish majburiyatisiz qo'ng'iroq qilishingiz mumkin
      basseyn
      3 ta sauna
      restoran majmuasi
      1 kishi uchun 300 000 so'm, 12 yoshgacha bo'lgan bolalarga bepul. Tashrif 18:00 gacha mavjud.
            ''',
            'ru': '''
            ***В стоимость номеров входит завтрак на 2 персоны. Детям до 3х лет - завтрак бесплатный. Свыше 3х лет - 
         100.000 сум за персону.
     Также можно заехать без обязательства снятия гостиничного номера, в распоряжении гостей
     бассейн
     3 сауны
     ресторанный комплекс
     Стоимость на 1 человека - 300.000 сум, детям до 12 лет бесплатно. Посещение доступно до 18:00.
            ''',
            'en': '''
	    *** The room rate includes breakfast for 2 persons. Children under 3 years old - breakfast is free. Over 3 years -
         100,000 soums per person.
     You can also call in without the obligation to rent a hotel room, at the disposal of guests
     pool
     3 saunas
     restaurant complex
     The cost for 1 person is 300,000 soums, children up to 12 years old are free. The visit is available until 18:00
	    '''
        },
        '8': {
            'uz': 'Spa',
            'ru': 'Спа',
            'en': 'Spa'
        },
        '9': {
            'uz': 'Basseyn',
            'ru': 'Бассейн',
            'en': 'Swimming pool'
        },
        '10': {
            'uz': 'Restoran',
            'ru': 'Ресторан',
            'en': 'Restaurant'
        },
        '11': {
            'uz': 'Avvaldan buyurtma bermoq',
            'ru': 'Бронировать',
            'en': 'Book'
        },
        '12': {
            'uz': 'Xonalar',
            'ru': 'Комнаты',
            'en': 'Rooms'
        },
        '13': {
            'uz': 'Shartlar',
            'ru': 'Условия',
            'en': 'Comforts'
        },
        '14': {
            'uz': 'Biz haqimizda',
            'ru': 'О нас',
            'en': 'About us'
        },
        '15': {
            'uz': '''
            HEAVENS GARDEN mehmonxonasi 2020 yil 31 avgustda ochilgan, 46 xonadan iborat;
         12 ta yarimlyuks, 4 ta lyuks, 4 ta ekonom va 26 ta standart. Hovuz tashqarida joylashgan va isitiladi.
         Spa fin saunasi va turk hammomdan iborat. Mehmonxonada bepul internet va sun'iy yo'ldoshli televidenie mavjud.

            ''',
            'ru': '''
            Гостиница HEAVENS GARDEN открылась 31 августа 2020 года, имеет 46 номеров;  
        12 полулюксов, 4 люкса, 4 эконома и 26 стандарта. Бассейн расположен на улице и имеет подогрев. 
        Спа состоит из Финской сауны и Турецкого хаммама. В гостинице имеется бесплатный интернет а также спутниковое телевидение.

            ''',
            'en': '''
		HEAVENS GARDEN Hotel opened on August 31, 2020, has 46 rooms;
        12 junior suites, 4 suites, 4 economy and 26 standards. The pool is located outside and is heated.
        The spa consists of a Finnish sauna and a Turkish hammam. The hotel has free internet and satellite TV.

	    '''
        },
        '16': {
            'uz': '''
               Spa ikkita saunadan (fin, turk) va turk hammomdan iborat
                ''',
            'ru': '''
                Спа состоит из двух саун(финская,турецкая) и турецкий хаммам
                ''',
            'en': '''
		The spa consists of two saunas (Finnish, Turkish) and a Turkish hammam
		'''
        },
        '17': {
            'uz': '''
                   Mehmonlar uchun bepul ochiq basseyn Endless pool formatida tayyorlangan va isitish tizimiga ega .
                    ''',
            'ru': '''
                    Бесплатный открытый бассейн для гостей сделан в формате Endless pool и имеет подогрев.
                    ''',
            'en': '''
		    Free outdoor pool for guests is made in Endless pool format and is heated.
	 	    '''
        },
        '18': {
            'uz': 'Bugun',
            'ru': 'Cегодня',
            'en': 'Today'
        },
        '19': {
            'uz': 'Ertaga',
            'ru': 'Завтра',
            'en': 'Tomorrow'
        },
        '20': {
            'uz': 'Kalendar',
            'ru': 'Календарь',
            'en': 'Calendar'
        },
        '21': {
            'uz': 'Kunni tanlash',
            'ru': 'Выберите день',
            'en': 'Choose a day'
        },
        '22': {
            'uz': "Boshlang'ich kunni tanlang",
            'ru': 'Выберите дату начала',
            'en': 'Check-in date'
        },
        '23': {
            'uz': "Oxirgi kunni tanlang ",
            'ru': 'Выберите последний день',
            'en': 'Check-out day'
        },
        '24': {
            'uz': "Xona olish uchun iltimos shaxsim ma'lumotlaringizni to'ldiring\nTo'liq ismingizni kiriting",
            'ru': 'Чтобы получить номер, введите свои личные данные \nВведите свое полное имя',
            'en': 'To get a number, enter your personal data \nEnter your full name'
        },
        '25': {
            'uz': "Iltmos to'g'ri telefon raqam kiriting",
            'ru': 'Пожалуйста, введите правильный номер телефона',
            'en': 'Please, enter a true phone number'
        },
        '26': {
            'uz': "Iltmos to'g'ri email kiriting",
            'ru': 'Пожалуйста, введите правильный адрес электронной почты',
            'en': 'Please, enter a true mail'
        },
        '27': {
            'uz': "To'liq ismingizni jo'nating",
            'ru': 'Отправьте свое полное имя',
            'en': 'Please, send your fullname	'
        },
        '28': {
            'uz': "Telefon raqamingizni kiriting",
            'ru': 'Введите свой номер телефона',
            'en': 'Please send your number'
        },
        '29': {
            'uz': "Elektron pochtangizni kiriting",
            'ru': 'Введите адрес электронной почты',
            'en': 'Please, send your mail'
        },
        '30': {
            'uz': "Manzilingizni kiriting",
            'ru': 'Введите ваш адрес',
            'en': 'Enter your address'
        },
        '31': {
            'uz': "Asosiy",
            'ru': 'Главный ',
            'en': 'Main'
        },
        '32': {
            'uz': "Sizning arizangiz Qabul qilindi javobni kuting",
            'ru': 'Ваша заявка принята. Ждите ответа',
            'en': 'Please, wait, we will contact you shortly'
        }

    }

    return language[word][lang]
