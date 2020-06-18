#!/usr/bin/python

import sys


# 0 - Service is OK.
# 1 - Service has a WARNING.
# 2 - Service is in a CRITICAL status.
# 3 - Service status is UNKNOWN.

nagios_codes = {
    "OK":0,
    "WARNING":1,
    "CRITICAL":2,
    "UNKNOWN":3
}


def count_lines(filename):
    '''
    zlicza linie w pliku
    '''
    lines = 0
    for line in open(filename):
        lines += 1
    return lines

def save_position():
    '''
    Zapisuje do pliku pozycję "ilość" lini od ostatniego sprawdzania
    '''
    pass

def read_position():
    '''
    wczytuje ostatnią pozycję pliku
    '''
    pass

def subtraction():
    '''
    zwraca różnicę miedzy plikami.
    '''
    pass


def load_settings():
    '''
    ładuje konfigurację pluginu.
    '''
    pass


def main():
    '''
    założenia: 
        skrypt bedzie na cliencie. odpalany przez nagios_nrpe.

    Jeżeli linie zapisane = sprawdzanym, status ok. 2=2
    jeżeli linie zapisane < sprawdzanych i różnica jest mniejsza od X status WARNING
    jeżeli linie zapisane < sprawdzanych i różnica jest większa od X status CRITICAL
    jeżeli linie zapisane > sprawdzonych plik został zlogowany przez rsysloga, należy ustawić znacznik.

    TODO: Co jaki czas ma się ustawiać status ok, jeżeli nie dochodzi do "zdarzenia", timestap wystarczy?
    TODO: Opracować zwracane komunikaty.
    TODO: args czy konfig file.
    '''
    if read_position() == count_lines():
        sys.exit(nagios_codes.get("OK"))
    

if if __name__ == "__main__":
    main()