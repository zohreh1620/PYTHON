class Device:
    count=0
    def __init__(self,ip, mac, name) -> None:
        self.ip=ip
        self.mac_address=mac
        self.name=name
        result=1 #ping the device
        if result:
            self.status='active'
        else:
            self.status='unknown'
    def get_status(self):
            print('result')       #return result


class TV(Device):
    def turn_off(self):
        #connect to self.ip and turn on
        pass
    def turn_off(self):
        #connect to self.ip and turn off
        pass


class Tuermo(Device):
    def get_degree(self):
        result= 2 #connect and read degree
        return result
        


class SmartTV(TV):
    def turn_on(self):
        print('Turn_on')
    

jadi_tv=TV(2,5,6)
jadi_tv.get_status()



