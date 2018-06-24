import logging
import configparser
import time

#get current temp -> currentTemp
#get set temp -> setTemp
"""
some variables
currentTemp = real environmental temp
setTemp = the current temp setting (scheduled or override)
sheduledTemp = temp is scheduled

"""
class thermo():
    def __init__(self):

        #start
        logging.info('starting')
        

    def getSchedule(self):
        #read schedule file
        logging.info('reading schedule')
        return 70

    def getCurrTemp(self):
        currentTemp = int(input('What is the temp? '))
        return currentTemp

    def setTemp(self, temp):
        return int(temp)

    def act(self):
        logging.info('its cold!')
        logging.info('turning on heater...')


class heater():
    """
    interacts with heater
    """
    def __init_(self):
        print('lets heat things up')

if __name__ == "__main__":
    logging.warning('entering main')
    t = thermo()
#   d = dht22()
#   h = heater()
#   while True:
    #get the current temp
    temp = t.getCurrTemp()
    #get scheduled temp
    scheduledTemp = t.getSchedule()
    t.setTemp(scheduledTemp)
    #override temp
    override = int(input('Set temp: '))
    t.setTemp(override)
    #compare
    if temp < t.setTemp():
        heater.On()
    else:
        heater.Off()
    home = thermo()
    home.run()
    setting = setTemp(70)
    currentTemp = getCurrTemp()
    logging.info(currentTemp, setting)
    if currentTemp <= setting:
        act()

