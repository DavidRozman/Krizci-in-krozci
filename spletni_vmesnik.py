import bottle
import model

ID_IGRE_COOKIE_NAME = 'id_igre'
COOKIE_SECRET = 'piskot'

krizcikrozci = model.KrizciKrozci()

krizcikrozci.preberi_iz_datoteke()

@bottle.get('/')
def index():
    # dokončaj
    return bottle.template('izgled.tpl')


@bottle.post('/nova_igra/')
def nova_igra():
    id_nove_igre = krizcikrozci.nova_igra()

    bottle.response.set_cookie(
        ID_IGRE_COOKIE_NAME, str(id_nove_igre), path='/',
        secret=COOKIE_SECRET
    )

    bottle.redirect(f'/igra/')



@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie(ID_IGRE_COOKIE_NAME, secret=COOKIE_SECRET))
    igra, poskus = krizcikrozci.igre[id_igre]

    return bottle.template('izgled.tpl', igra=igra, poskus=poskus, id_igre=id_igre)



@bottle.post('/igra/')
def izberi_polje():

    id_igre = int(bottle.request.get_cookie(ID_IGRE_COOKIE_NAME, secret=COOKIE_SECRET))
    polje = bottle.request.forms.getunicode('polje')
    
    krizcikrozci.izberi_polje(id_igre, polje)

    bottle.redirect(f'/igra/')



bottle.run(reloader=True, debug=True)