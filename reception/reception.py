class Reception:
    def __init__(self):  
        self.vip=[]
        self.ordinary=[]

    def store_vip(self):
        temp_vip=open('vip.txt','r')       
        for line in temp_vip:
            self.vip.append(line.strip('\n'))
        return self.vip

    def store_ordinary(self):
        temp_ordinary=open('ordinary.txt','r')
        for line in temp_ordinary:
            self.ordinary.append(line.strip('\n'))
        return ordinary
    
    def search_name(self):
        vip_name=input("Entetr name ")
        names=[]
        names=self.store_vip()
        for nm in names:
            if vip_name in nm:
                return nm

people=Reception()
print(people.search_name())
    