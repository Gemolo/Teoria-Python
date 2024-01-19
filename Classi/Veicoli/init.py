from autoelettrica import AutoElettrica
from motoelettrica import MotoElettrica

def init():
    tesla = AutoElettrica("Tesla","X", 1000)
    print(tesla.stampa_autonomia())
    
    moto = MotoElettrica("Yamaha", "Moto", 500)
    print(moto.stampa_autonomia())
init()