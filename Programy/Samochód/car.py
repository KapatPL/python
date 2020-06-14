# -*- coding: utf-8 -*-

import time
from carclass import Car

def main():
    audi = Car() 
    
    audi.startEngine()
    
    if audi.isRun():
        while audi.isRun():
            if audi.get_gear() == 0:
                print("Jedziemy? wbij bieg 1")
                b = input()
                if int(b) == 1:
                    audi.set_gear(int(b))
                else:
                    print("Od kiedy ruszmy z ", b)
                    audi.stopEngine()
            else:
                audi.carCockpit()
                time.sleep(1)
                if audi.get_gear() == 1:
                    audi.accelerator(4, 30, 5000)
                if audi.get_gear() == 2:
                    audi.accelerator(4, 60, 5000)
                if audi.get_gear() == 3:
                    audi.accelerator(4, 90, 5000)
                if audi.get_gear() == 4:
                    audi.accelerator(4, 120, 5000)
                    if audi.get_engine_speed() >= 9000:
                        audi.stopEngine(2)
    
if __name__ == '__main__':
    main()        


