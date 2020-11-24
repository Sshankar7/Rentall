class User:
    def __init__(self,name="default",password="default",balance = 0):
        self.name = name
        self.password = password
        self.balance = balance

    def update_details(self,nam,pas,bal):
        self.name=nam
        self.balance = bal
        self.password = pas

    def get_details(self):
        return self.name,self.password,self.balance



class Stock:
    def __init__(self,item="null",value=0):
        self.goods = {item:value}

    def update_stocks(self,item,value):
        self.goods = {item:value}

    def get_details(self):
        return self.goods
