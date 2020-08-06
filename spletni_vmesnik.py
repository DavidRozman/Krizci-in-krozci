import bottle
import model

@bottle.get('/')
def index():
    return bottle.template('./Krizci-in-krozci/izgled.tpl')






bottle.run(reloader=True, debug=True)