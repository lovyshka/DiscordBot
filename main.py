# -*- coding utf-8 -*-

import discord
from discord.ext import commands
from con import token
import random
import requests


bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    '''
    Проверка на готовность. В этой и всех дальнейших функциях я использую ассинхронное програмирование ,
    о чем сидетельствуют ключевые слова async и await(в следующей функции). await - ключевое слово с помощью которого
    осуществляется вызов функции.
    :return: str
    '''
    print('Бот готов к использованию')


@bot.command()
async def hello(ctx):
    '''
    Приветствие.
    Для создания команды используется декоратор bot.command . На вход в функцию должен подаваться миниму 1 аргумент,
    в нашем случае мы подаем в функцию hello параментр ctx. ctx(контекст) - ответ сервера о случившемся
    событии или вызове команды.
    ctx содержит:
    args : list   [Список преобразованных аргументов, переданных в команду],
    author : union[User, Member]    [Возвращает автора, связанного с этой командой]
    bot : bot  [Бот, содержащий выполняемую команду]
    channel : union[abc.Messageable]    [Возвращает канал, связанный с командой этого контекста.]
    cog : optional[Cog]  []
    command : command [Команда, которая вызывается в данный момент]
    command_failed : bool  [Возвращает логической значение, которое означает статус выполнения команды]
    guild : optional[Guild]   [Возвращает канал, связанный с ctx этой команды]
    invoked_parents : list[str]  [Имена команд родителей который вызвали этот вызов]
    invoked_subcommand : command  [Подкоманда, котрая была вызвана]
    invoked_with : str [Имя команды которая вызвала этот вызов]
    kwargs : dict [Словарь преобразованных аргументов, переданных в команду]
    me : union[Member, ClientUser]   [Похоже на guild за исключением того, что может вернуть ClientUser]
    message : message  [Сообщение вызвавшее выполнение команды]
    prefix : str  [префикс, который был использован для вызова команды]
    subcommand_passed : optional[str]   [Строка с помощью которой была предпринята попытка вызвать подкоманду]
    valid : bool    [Проверяет допустим ли контекст вызова для вызова]
    voice_client : optional[VoiceProtocol]   [Кратчайший путь к Guild.voice_client, если возможно]
    :param: author
            prefix
            me
            bot
            channel
            command
    :return: message
    '''
    author = ctx.message.author
    await ctx.send(f'Привет,дорогой, {author.mention}!Как твои дела? А в прочем, мне не итнересно.')

@bot.command()
async def cat(ctx):
    '''
    Котики
    Отправляем случайный jpg файл котиков из списка возможных отправителю команды. Данные об авторе команды, а также
    расположении сообщении в текстовых каналах.
    :param ctx: author
            prefix
            me
            bot
            channel
            command
    :return: file
    '''
    author = ctx.message.author
    cats_list = ['cats/1.jpg', 'cats/2.jpg', 'cats/3.jpg', 'cats/4.jpg', 'cats/5.jpg', 'cats/6.jpg', 'cats/7.jpg', 'cats/8.jpg', 'cats/9.jpg', 'cats/10.jpg']
    img = discord.File(random.choice(cats_list))
    await ctx.send(f'К {author.mention} пришла кошка!!!')
    await ctx.send(file=img)

@bot.command()
async def meme(ctx):
    '''
    Мем
    Отправляем случайный jpg/jpeg/png файл с мемом отправителю команды. Опять же подавая на вход функции meme параметр ctx.
    :param ctx: author
                prefix
                me
                bot
                channel
                command
    :return: file
    '''
    author = ctx.message.author
    memes_list = ['memes/1.jpg', 'memes/2.jpg', 'memes/3.jpeg', 'memes/4.jpg', 'memes/5.png', 'memes/6.jpg']
    img = discord.File(random.choice(memes_list))
    await ctx.send(f'Вот твой мем{author.mention}')
    await ctx.send(file=img)

@bot.command()
async def anec(ctx):
    '''
    Анекдот
    Отправляем случайно выбранный анекдот отправителю команды, данные о котором хранятся в ctx, который мы подаем на вход
    в функцию anec.
    :param ctx: author
                prefix
                me
                bot
                channel
                command
    :return: str
    '''
    author = ctx.message.author
    anec_list = ['Штирлиц вёл двойную жизнь и очень надеялся, что хоть одна из них сложится удачно.', 'Курица клевала носом."Наверное не выспалась", - подумал Штирлиц', 'Штирлиц стрелял вслепую. Слепая отпрыгнула и стала отстреливаться.', 'Штирлиц вошёл в комнату, из окна дуло. Штирлиц закрыл окно, дуло исчезло.']
    anec = random.choice(anec_list)
    await ctx.send(f'Ха-ха-ха, вот держи мой любимый анекдот {author.mention},как вспомню так смеюсь')
    await ctx.send(anec)


@bot.command()
async def coin_flip(ctx):
    '''
    Имитируем подбрасывание монетки
    Отправляем результат подбрасывания монетки человеку, который вызвал команду.
    :param ctx: author
                prefix
                me
                bot
                channel
                command
    :return: str
    '''
    author = ctx.message.author
    coin_side = random.choice(['Орел', 'Решка'])
    await ctx.send(f'Смотри внимательно,{author.mention}')
    await ctx.send(coin_side)



@bot.command()
async def weath(ctx):
    '''
    Погода в МСК
    Формируем запрос на зайт openweathermap о погоде в Москве, затем с помощью фильтров вытаскиваем нуную информацию
    :param ctx: author
                prefix
                me
                bot
                channel
                command
    :return: str
    '''
    author = ctx.message.author
    '''Заимствованно отсюда https://habr.com/ru/post/315264/  Начала заимствования '''
    city_id = 524901
    appid = "01799e3ab6dce77ef232475e6908debb"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        opisanie = data['weather'][0]['description']   #состояние
        aver = data['main']['temp']   #средняя температура в городе
        await ctx.send(f'Вот. Как и просил, {author.mention} - последние погодные сводки.')
        await ctx.send(opisanie)
        await ctx.send(aver)
    except Exception as e:
        print("Exception (weather):", e)
        pass
    '''Конец заимствования'''

@bot.command()
async def quote(ctx):
    '''
    Цитата
    Отправляем челоку, который ввел команду, цитату одного из великих деятелей своего времени
    :param ctx:author
                prefix
                me
                bot
                channel
                command
    :return: str
    '''
    author = ctx.message.author
    quotes = ['Надо любить жизнь больше, чем смысл жизни. Федор Достоевский', 'Вы никогда не пересечете океан, если не наберетесь мужества потерять берег из виду. Христофор Колумб', 'Лучшая месть – огромный успех. Фрэнк Синатра', 'Стоит только поверить, что вы можете – и вы уже на полпути к цели. Теодор Рузвельт', 'Если нет ветра, беритесь за вёсла. Латинская поговорка']
    quo = random.choice(quotes)
    await ctx.send(f'Мне кажется {author.mention} не в настроение... Возможно это приободрит тебя')
    await ctx.send(quo)


@bot.command()
async def roulet(ctx, arg):
    '''
    Русская рулетка, для выбора введите -roulet [число]
    Имитируем игру в русскую рулетку
    :param ctx:author
                prefix
                me
                bot
                channel
                command
    :param arg: int
    :return: message
    '''
    smert = random.choice([1, 2, 3, 4, 5, 6])
    'Генерируем номер каморы в револьвере'
    if int(arg) == smert:
        await ctx.send('Ты не знал но уже сыграл в русскую рулетку и ты проиграл.')
        await ctx.send('Патрон был в барабане под твоим номером')
    else:
        await ctx.send('Тебе сказочно повезло, ты мог умереть, барабан остановился на номере')
        await ctx.send(smert)
        await ctx.send('Береги себя и не играй больше в такие игры')


@bot.command()
async def news(ctx):
    '''
    Новости
    Отправляем челоку, который ввел команду url страницы с новостями. Данные об авторе команды хранятся в ctx.
    :param ctx:author
                prefix
                me
                bot
                channel
                command
    :return: message
    '''
    author = ctx.message.author
    newspaper = random.choice(['https://tass.ru/obschestvo/13236943?utm_source=yxnews&utm_medium=desktop', 'https://yandex.ru/news/story/Sobyanin_poruchil_prodlit_rabotu_metro_i_MCK_navsyu_novogodnyuyu_noch--0d37781b0edda3020fba85cfd250473a?lang=ru&from=reg_portal&fan=1&stid=buPsYbU3w1po0v_gxEET&t=1639811236&persistent_id=173150630&lr=213&msid=1639811635.58391.94794.53086&mlid=1639811236.geo_213.0d37781b&utm_source=morda_desktop&utm_medium=topnews_region', 'https://3dnews.ru/1056204/tencent-prisoedinila-k-sebe-studiyurazrabotchika-left-4-dead-i-back-4-blood?utm_source=yxnews&utm_medium=desktop', 'https://yandex.ru/news/story/GSC_Game_World_otmenila_vsyo_svyazannoe_sNFT_vS.T.A.L.K.E.R._2--19d52d6b10e6dfbf75ea40e759b8a370?lang=ru&from=api-rubric&rubric=personal_feed&wan=1&stid=7u4NKaRLyndGIuHjlJBx&t=1639811236&persistent_id=172160575&utm_source=morda_desktop&utm_medium=topnews_personal', 'https://www.kinonews.ru/news_104355/?utm_source=yxnews&utm_medium=desktop'])
    await ctx.send(f'А вот и свежие новости, все как ты просил{author.mention}')
    await ctx.send(newspaper)

@bot.command()
async def goroscop(ctx, arg):
    '''
    Гороскоп для вызова введите -goroscop [ваш ЗЗ с большой буквы]
    :param ctx: author
                prefix
                me
                bot
                channel
                command
    :param arg: text
    :return: str
    '''
    if arg == 'Овен':
        await ctx.send('Не торопите события – поспешные действия могут вызвать сильное разочарование и привести к неприятностям и переживаниям.')
    elif arg == 'Телец':
        await ctx.send('Спокойный и благоприятный день для того, чтобы справиться с любыми проблемами и задачами.')
    elif arg =='Близнецы':
        await ctx.send('Некоторые неприятности из прошлого могут напомнить о себе с новой силой, как и неприятные люди')
    elif arg == 'Рак':
        await ctx.send('Удачный день для поездок и встреч – они принесут много положительных впечатлений и ярких эмоций. ')
    elif arg == 'Лев':
        await ctx.send('Удачный день для общения – новые контакты, знакомства и налаживания отношений могут принести вам пользу, причем на длительное время.')
    elif arg == 'Дева':
        await ctx.send('Благоприятный день для осуществления задуманного, а также для передачи различных идей другим, которые принесут вам пользу, причем в самом ближайшем будущем.')
    elif arg == 'Весы':
        await ctx.send('Не торопите события. Сегодня лучше ничего не делать и не спешить с выводами – вряд ли они будут правильными.')
    elif arg == 'Скорпион':
        await ctx.send('Не торопите события – сегодня у вас не все получится так быстро, как вы хотели бы. Звезды советуют вам отдохнуть и расслабиться')
    elif arg == 'Стрелец':
        await ctx.send('Удачный день для принятия решений и проявления характера – сегодня вы справитесь со всеми неприятностями самостоятельно.')
    elif arg == 'Козерог':
        await ctx.send('Сложный и непредсказуемый день во всех отношениях, особенно в любви. Страхи и сомнения могут испортить вам настроение, поэтому не стоит давать ход отрицательным эмоциям – пересмотрите ситуацию.')
    elif arg == 'Водолей':
        await ctx.send('Не торопите события – сегодня вам придется выполнить много неприятных, но необходимых дел.')
    elif arg == 'Рыбы':
        await ctx.send('Хороший и легкий день во всех отношениях при условии, что вы не будете поддаваться мрачному настроению. ')



bot.run(token)
