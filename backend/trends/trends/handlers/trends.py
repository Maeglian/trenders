from flask import Blueprint, Response

trends = Blueprint('trends', __name__)

mock_json = '''
    {"data": [
    {"title": "Спартак москва – Арсенал тула", "avatar": "https://t1.gstatic.com/images?q=tbn:ANd9GcSe1sh_sy38pPP7b868ch4rdFQEgrY1g1kDFLRCrJYGa2zdpj6800mFFb3iIfzLCCSUaCfYsKXW", "description": "Первая победа за несколько месяцев: «Арсенал» обыграл ..."}, 
    {"title": "Что с ВК", "avatar": "https://t1.gstatic.com/images?q=tbn:ANd9GcQbcroySyBezCrnRTl6rWON-XPMBjnGCzMZq3Ubs1qahKyNSkP4hmk7PWDG8wBreKq-urrTQyQk", "description": "Почему не работает «ВКонтакте»"}, 
    {"title": "4 ноября", "avatar": "https://t0.gstatic.com/images?q=tbn:ANd9GcQUe0rj_c-DlIZVQ2JfT_91hKIiaxJs1K2Wrz0DOO5QRiTAhl9cRGLV3NLIAUWBJZKrOzvkoByK", "description": "Единством сыт не будешь: что праздновать 4 ноября"}, 
    {"title": "Спартак", "avatar": "https://t3.gstatic.com/images?q=tbn:ANd9GcQeUMYRYhkaNimzGx1F0PqNGZHSyt6tiB21OD-QXj9TZu7S5gA4E7Dm7e_s1kZ6167zHSl3ASck", "description": "«Арсенал» — кошмар «Спартака». Тедеско потерпел первое ..."}, 
    {"title": "Крылья советов – Рубин", "avatar": "https://t1.gstatic.com/images?q=tbn:ANd9GcTgdLBTaNOJ595qjpP9ar6zmnWnkamgE1ZEfQE0hhoZLdMaYwdisVJ-p6oz3kYEMjG88t3CdduS", "description": "«Крылья Советов» — «Рубин». Видеотрансляция"}, 
    {"title": "Мари Лафоре", "avatar": "https://t2.gstatic.com/images?q=tbn:ANd9GcR95hLOImG-6QC5Lfam7JOe0iDbqnYkNmZ9Qsh1uBJXrvYevOXiMhJtc9iNtB4qj0IZAKnVVGcasg", "description": "Умерла французская певица и актриса Мари Лафоре"}, 
    {"title": "Что с ВКонтакте", "avatar": "https://t3.gstatic.com/images?q=tbn:ANd9GcRMyPYL-2cg3p2nVSFsTwFlozxslY3qGWTByRNNrxoRYhA1ov-jIl2-6XqbeXWlSVP0hXwRQojc", "description": "Пользователи  ВКонтакте  пожаловались на сбои в работе ..."}, 
    {"title": "Спартак Арсенал смотреть онлайн", "avatar": "https://t1.gstatic.com/images?q=tbn:ANd9GcS9OyDUdTRfx75g5MoLoVArVZFUN9P595NT3Nhp1Mmh8vIe_mjU7bSnImovToicf0d4beeNKQ5P", "description": "АРЕНА LIVE! «Спартак» — «Арсенал»"}]}
'''

@trends.route('/fetch', methods=['GET'])
def import_trends():
        
    return Response(mock_json, status=200)
