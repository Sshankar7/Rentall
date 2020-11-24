
from database import User
from database import Stock

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    u = User("Ash","123",100)
    print(u.get_details())
    s1 = Stock()
    print(s1.get_details())
    s2=Stock("candy",10)
    print(s2.get_details())
    s2.update_stocks("cdy",20)
    print(s2.get_details())


