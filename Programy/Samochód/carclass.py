# -*- coding: utf-8 -*-

class Car:

    '''
    self.__isRunning = 0        => 0 - wy??czony, 1 - Uruchomiony 2 - Popsu? si?
    self.__Speed = 0            => Pr?dko?? pocz?tkowa
    self.__Gear = 0             => bieg
    self.__EngineSpeed = 0      => predko?? obrotowa 
    '''
    def __init__(self):
        self.__isRunning = 0
        self.__Speed = 0
        self.__Gear = 0
        self.__EngineSpeed = 1000
    
    ''' Biegi '''
    def get_gear(self):
        return self.__Gear
    
    def set_gear(self,gear):
        self.__Gear = gear

    ''' Predkosc '''

    def get_speed(self):
        return self.__Speed
        
    def set_speed(self,speed):
        self.__Speed = speed
        
    ''' Obroty '''
    def get_engine_speed(self):
        return self.__EngineSpeed
    
    def set_engine_speed(self, engineSpeed):
        self.__EngineSpeed = engineSpeed

    ''' Czy dziala '''
    def isRun(self):
        if self.__isRunning == 1:
            return True
        else:
            return False
    
    ''' Uruchomienie silnika '''
    def startEngine(self):
        self.__isRunning = 1

    ''' zatrzymanie silnika '''
    def stopEngine(self, error):
        if error == 0:
            self.__isRunning = 0
        if error == 1:
            self.__isRunning = 1
        if error == 2:
            self.__isRunning = 2

    ''' Wyswietla kokpit '''
    def carCockpit(self):
        if self.__Speed > 9 and self.__Speed < 100:
            print("Predkosc: 0"+str(self.__Speed) + " Obroty: " + str(self.__EngineSpeed) + " Bieg: " + str(self.__Gear), end="\r")
        elif self.__Speed > 99 and self.__Speed < 1000:
            print("Predkosc: "+str(self.__Speed) + " Obroty: " + str(self.__EngineSpeed) + " Bieg: " + str(self.__Gear),end="\r")
        else:
            print("Predkosc: 00"+str(self.__Speed) + " Obroty: " + str(self.__EngineSpeed) + " Bieg: " + str(self.__Gear),end="\r")

    ''' Przyspiesza '''
    def accelerator(self, maxGear, speed, engine_speed):
        self.set_engine_speed(self.get_engine_speed()+500)
        self.set_speed(self.get_speed()+5)
    
        if self.get_engine_speed() > engine_speed:
            if not self.get_gear() == maxGear:
                self.set_engine_speed(int(self.get_engine_speed()/3))
                self.set_gear(self.get_gear()+1)
    
