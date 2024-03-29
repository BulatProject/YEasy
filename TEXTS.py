EXAMPLES = ('https://youtu.be/', 'youtu.be/', 'https://www.youtube.com/watch?', 'youtube.com/watch?', 'https://youtube.com/playlist?', 'youtube.com/playlist?')

CLEAN_LINK = f'Ссылка на видео должна начинаться как один из примеров и быть не длиннее 130 символов:\n"{EXAMPLES[0]}"\n"{EXAMPLES[1]}"\n"{EXAMPLES[2]}"\n"{EXAMPLES[3]}"\n"{EXAMPLES[4]}"\n"{EXAMPLES[5]}"'

ERRORS = ("Ресурс недоступен.", 
            r'Ошибка в ссылке или доступ к видео ограничен. Видео: {} Код ошибки: {}.',
            f"Ссылка не соответстует требованиям:\n{CLEAN_LINK}",
            "Доступ к видео ограничен, или по ссылке {} видео нет.")

BAN_LIST = ('/', '\\', ':', '*', '?', '<', '>', '|', '"', "'", '@', '#', '&', '%', '^',
        '(Official Video)', '(Official Music Video)', '(Official Audio)', '(Music Video)', 
        '(OFFICIAL VIDEO)', '(OFFICIAL MUSIC VIDEO)', '(OFFICIAL AUDIO)', '(MUSIC VIDEO)',
        '[Official Video]', '[Official Music Video]', '[Official Audio]', '[Music Video]',
        '[OFFICIAL VIDEO]', '[OFFICIAL MUSIC VIDEO]', '[OFFICIAL AUDIO]', '[MUSIC VIDEO]',
        'Official Video', 'Official Music Video', 'Official Audio', 'Music Video',
        'OFFICIAL VIDEO', 'OFFICIAL MUSIC VIDEO', 'OFFICIAL AUDIO', 'MUSIC VIDEO',
        '(Official HD Video)', '(Official HQ Video)', '(High Quality)', '(HIGH QUALITY)', 
        '(OFFICIAL HD VIDEO)', '(OFFICIAL HQ VIDEO)', '(Video)', '(Audio)', '[Audio]',
        '(Official Lyrics Video)', '(Lyric Video)', '(VIDEO)', '(AUDIO)', '[AUDIO]',
        '[Official Lyrics Video]', '[Lyric Video]',
        '(lyrics)', '(Lyrics)', '(LYRICS)',
        '[lyrics]', '[Lyrics]', '[LYRICS]',
        'Lyrics', 'lyrics', 'LYRICS',
        '(hd)', '(hq)', '[hd]', '[hq]',
        '(HD)', '(HQ)', '[HD]', '[HQ]', '[CC]')

CONVERSION = r"ffmpeg -i {} -codec:a libmp3lame -qscale:a 2 {}"
WEBM = r'{}.webm'
MP3 = r"{}.mp3"
CONVERSION_ERROR = r'Произошла ошибка при конвертации в mp3 песни {} канала {}'
DOWNLOADING_ERROR = r'Произошла ошибка при скачивании файла. Видео: {} канала {}.'

START = 'Перед использованием ОБЯЗАТЕЛЬНО прочтите описание и инструкцию по использованию бота, введя: "/help" и "/info".'
HELP = '''\
Данный бот предназначен для скачивания песен с YouTube, но его можно использовать и для скачивания аудиоряда из любого видео.
Бот скачивает аудиоряд в формате webm, а затем конвертирует в mp3, добавляя теги.

Скачивать песни можно как по одной, так группой из плейлистов.

Из-за особенностей библиотеки FFMPEG, которая используется для конвертации файлов, название файла может не совпадать с названием видео.

Если в названии видео присутстуют символы из следующего списка: '/', '\\', ':', '*', '?', '<', '>', '|', '"', "'", то файл точно будет иметь другое название.
Воздержитесь от скачивания видео с нестандартными символами в названии.

ВАЖНО!
Бот автоматически убирает из названия песни следующие комбинации символов (в теги они тоже не попадут):
'/', '\\', ':', '*', '?', '<', '>', '|', '"', "'", '@', '#', '&', '%', '^', \
'(Official Video)', '(Official Music Video)', '(Official Audio)', '(Music Video)', \
'(OFFICIAL VIDEO)', '(OFFICIAL MUSIC VIDEO)', '(OFFICIAL AUDIO)', '(MUSIC VIDEO)', \
'[Official Video]', '[Official Music Video]', '[Official Audio]', '[Music Video]', \
'[OFFICIAL VIDEO]', '[OFFICIAL MUSIC VIDEO]', '[OFFICIAL AUDIO]', '[MUSIC VIDEO]', \
'Official Video', 'Official Music Video', 'Official Audio', 'Music Video', \
'OFFICIAL VIDEO', 'OFFICIAL MUSIC VIDEO', 'OFFICIAL AUDIO', 'MUSIC VIDEO', \
'(Official HD Video)', '(Official HQ Video)', '(High Quality)', '(HIGH QUALITY)', \
'(OFFICIAL HD VIDEO)', '(OFFICIAL HQ VIDEO)', '(Video)', '(Audio)', '[Audio]', \
'(Official Lyrics Video)', '(Lyric Video)', '(VIDEO)', '(AUDIO)', '[AUDIO]', \
'[Official Lyrics Video]', '[Lyric Video]', \
'(lyrics)', '(Lyrics)', '(LYRICS)', \
'[lyrics]', '[Lyrics]', '[LYRICS]', \
'Lyrics', 'lyrics', 'LYRICS', \
'(hd)', '(hq)', '[hd]', '[hq]', \
'(HD)', '(HQ)', '[HD]', '[HQ]', '[CC]'.

Также он заполняет теги "исполнители" и "название".
Если в названии видео нет символа "-", то название видео становится названием трека, а название канала - именем исполнителя.
В противном случае он делит название видео пополам, и левая часть становится именем исполнителя, а правая - названием трека.

После скачивания, соответственно, советую подкорректировать теги, если это имеет для вас значение.

Чтобы посмотреть доступные команды, наберите /commands.\
'''

COMMANDS = \
'''
/start - запустить бота.
/info - инструкция по работе с ботом.
/help - узнать основную информацию о боте (перед использование ОБЯЗАТЕЛЬНО ознакомьтесь).
/commands - получить эту инструкцию.\
'''

INFO = \
f'''ВАЖНО. Если видео, аудиоряд которого вы хотите скачать, имеет возрастные или иные ограничения, то видео скачано не будет!

Использовать бота просто:
Введите: "Трек, ССЫЛКА_НА_ВИДЕО", - и отправьте сообщение, если хотите скачать аудиоряд из одного видео.

Пример:
Трек, https://youtu.be/Z6kNQEzQJpA

{CLEAN_LINK}

Если же вы хотите скачать видео из плейлиста, то инструкция следующая:
Введите: "Лист, ДИАПАЗОН, ССЫЛКА_НА_ППЛЕЙЛИСТ".
Диапазон, в котором находятся треки, должен быть не больше 20.

Пример:
Лист, 1-21, https://youtube.com/playlist?list=КОДПЛЕЙЛИСТА

В данном случае скачаны будут первые 20 песен из указанного плейлиста.
Если в вашем диапазоне больше 20 песен, то песни скачаны не будут.
Если в плейлисте меньше песен, нежели в диапазоне, что вы указали, песни скачаны не будут.

К сожалению, каждый раз вам придётся присылать ссылку и диапазон заново.
Возможно, в будущем это неудобство будет устранено.\
'''

WRONG_COMMAND = "Эта комманда не поддерживается."

ILOVEYOU = 'Обнимаю и целую. =3'

COMMA_MESSAGE_ERROR = 'Нет запятой - диапазон не распознан.'
HYPHEN = 'Нет дефиса - диапазон не распознан.'
SYMBOLS_ERROR = 'В диапазоне есть лишние символы - диапазон не распознан.'
RANGE_ERROR = 'Количество песен, которое вы хотите скачать: {}. Это не соответствует правилам.'
INSTRUCTION_ERROR = 'Сообщение должно начинаться с символов "трек," или " лист,".'
LENGHT_ERROR = F'Ошибка.\nПроверьте свою команду:\n{INSTRUCTION_ERROR}'
STARTING_WORDS = ('трек,', 'лист,')
NO_FIRST_NUM_ERROR = 'Вы пропустили первое число диапазона.'
RANGE_TOO_BIG = 'Диапазон не может быть больше размера плейлиста.'