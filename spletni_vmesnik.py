
from bottle import route, run, template, request, response, redirect
from model import Igralec, Plosca
import db

@route('/zacetek', method = 'POST')
def zacetek():
    ime1 = request.forms.get('igralec1')
    ime2 = request.forms.get('igralec2')

    igralec1 = None
    igralec2 = None
    for igralec in db.igralci:
        if igralec.ime == ime1:
            igralec1 = igralec 
        elif igralec.ime == ime2:
            igralec2 = igralec
    
    if igralec1 is None:
        igralec1 = Igralec(ime1, False)
        db.igralci.append(igralec1)
    if igralec2 is None:
        igralec2 = Igralec(ime2, False)
        db.igralci.append(igralec2)

    plosca = Plosca(igralec1.ime, igralec2.ime)
    db.igre.append(plosca)
    response.set_cookie('id_plosce', str(plosca.id))
    db.shrani()
    return template('igra.html', plosca=plosca)

@route('/', method = 'GET')
def index():
    response.delete_cookie('id_plosce')
    return template('index.html', igralci=db.igralci, igre=db.igre)

@route('/vnos', method = 'POST')
def vnos_post():
    x = int(request.forms.get('koordinata_x'))
    y = int(request.forms.get('koordinata_y'))
    igralec = int(request.forms.get('igralec'))
    id_plosce = int( request.cookies.get('id_plosce'))
    for plosca in db.igre:
        if plosca.id == id_plosce and not plosca.konec:
            plosca.vnos(x, y, igralec)
            if plosca.konec:
                for igralec in db.igralci:
                    if igralec.ime == plosca.zmagovalec:
                        igralec.tocke += 1
                db.shrani()
                redirect('/')
            else:
                db.shrani()
                return template('igra.html', plosca=plosca)

@route('/vnos', method = 'GET')
def vnos_get():
    id_plosce = int( request.cookies.get('id_plosce'))
    for plosca in db.igre:
        if plosca.id == id_plosce and not plosca.konec:
            return template('igra.html', plosca=plosca)

    
db.nalozi()
run(host='localhost', port=8080)
