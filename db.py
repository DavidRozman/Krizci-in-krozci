import json
import os.path
from model import Igralec, Plosca

igre = []
igralci = []

db_file = "db.json"

def shrani():
    file = open(db_file, 'w')
    dic = {
        'igre': [plosca.__dict__ for plosca in igre],
        'igralci':[igralec.__dict__ for igralec in igralci]
    }
    json.dump(dic, file,indent='  ')
    file.close()

def nalozi():
    if not os.path.isfile(db_file):
        shrani()
    file = open(db_file, 'r')
    dic = json.load(file)
    for p in dic['igralci']:
        igralec = Igralec()
        igralec.__dict__ = p
        igralci.append(igralec)
    for p in dic['igre']:
        plosca = Plosca()
        plosca.__dict__ = p
        igre.append(plosca)
    file.close()


