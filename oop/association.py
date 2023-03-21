"============================Associaciya============================"
# Associaciya - princip OOP v kotorom dva klassa drug s drugom svyazany
# associaciya delitsya na 2 principa:
# 1 - agregaciya (bolee slabaya svyaz')
# 2 - kompoziciya (bolee sil'naya svyaz')

class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100

class Iphone:
    def __init__(self, color):
        self.color = color
        self.battery = Battery()
        # kogda my sozdaem ob'ekt ot drugogo klassa pryam
        # vnutri drugogo - kompoziciya

battery = Battery()
print(battery.power) # 100
iphone = Iphone('gold')
print(iphone.battery.power) # 100

del iphone
# ob'ekt udalyaetsya vmeste s ob'ektom iphone



class Nokia:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery
        # kogda my prinimaem uje sozdannyi vne klassa ob'ekt - agregaciya

battery = Battery
nokia = Nokia('black', battery)
# print(nokia.battery.power)

del nokia
# udalyaetsya tol'ko ob'ekt nokia, batareika sohranyaetsya
print(battery.power)