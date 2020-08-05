import model

trenutna_igra = model.nova_igra()

def izpis_poraza(igra):
    return f"Izgubil si."

def izpis_zmage(igra):
    return f'Zmagal si!'

def izpis_remija(igra):
    return f'Izid je neodločen.'

def zahtevaj_vnos_polja():
    return input('Izberi polje:')

def pozeni_vmesnik():
    trenutna_igra = model.nova_igra()
    while True:
        print(izpis_igre(trenutna_igra))
        polje = zahtevaj_vnos_polja()
        trenutna_igra.izberi_polje(polje)
        if trenutna_igra.ali_je_zmagal_racunalnik():
            print(izpis_poraza(trenutna_igra))
            return 
        if trenutna_igra.ali_je_zmagal_igralec():
            print(izpis_zmage(trenutna_igra))
            return
        if trenutna_igra.ali_je_remi(trenutna_igra):
            print(izpis_remija(trenutna_igra))
            return

pozeni_vmesnik()