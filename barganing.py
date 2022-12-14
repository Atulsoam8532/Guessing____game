from threading import *
from time import*
import sys
class shop():
    tomato = 20
    potato = 30
    carrot = 40
    def __init__(self,c,t,p):
        self.carrot = c
        self.tomato = t
        self.potato = p


def market():
    while True:
        print("Enter what do you want")
        a = input().lower()
        if a == "tomato":
            print("The price of",a,"is",shop.tomato)
            sleep(2)
            print("product is eligible for discount")
            sleep(1)
            print("do you want to buy")
            b = input().lower()
            sleep(1)
            if b == "no":

                choice()
                c = int(input())
                sleep(1)
                if c == 1:
                    print("tell me the price you want")
                    d = int(input())

                    print("let me check")
                    if d > 15 and d < 20:
                        print("i am happy to give you on this price")
                        pri1 = shop(0,d,0)
                        print("your final price is",pri1.tomato)
                        more()

                    else:
                        fix()
                        break
                elif c == 2:
                    print("you want something else")
                    more()

            else:
                print("now you are eligible for 5% dicount")
                print("your final price after discount is",((5*100)/shop.tomato))
                print("do you want more")
                more()



        elif a == "potato":
            print("The price of",a,"is",shop.potato)
            print("product is eligible for discount")
            print("do you want to buy")
            b = input().lower()
            if b == "no":
                choice()
                c = int(input())
                if c == 1:
                    print("tell me the price you want")
                    d = int(input())
                    print("let me check")
                    if d > 25 and d < 30:
                        print("i am happy to give you on this price")
                        pri2 = shop(0, 0, d)
                        print("your final price is", pri2.potato)
                        print("you want something else")
                        more()
                    else:
                        fix()
                        break
                elif c == 2:
                    print("you want something else")
                    more()
            else:
                print("now you are eligible for 5% dicount")
                print("you final price after discount is",((5*100)/shop.potato))
                print("do you want more")
                more()



        elif a == "carrot":
            print("The price of",a,"is",shop.carrot)
            print("do you want to buy")
            b = input().lower()
            if b == "no":
                choice()
                c = int(input())
                if c == 1:
                    print("tell me the price you want")
                    d = int(input())
                    print("let me check")
                    if d > 35 and d < 40:
                        print("i am happy to give you on this price")
                        pri3 = shop(d, 0, 0)
                        print("your final price is", pri3.carrot)
                        print("you want something else")
                        more()

                    else:
                        fix()
                        break
                elif c ==2:
                    print("you want something else")
                    more()
            else:
                print("now you are eligible for 5% dicount")
                print("you price is", ((5*100)/shop.carrot))
                more()

        else:
            print("invalid input")



def more():
    print("do you want anything else apart of this")
    e = input().lower()
    if e == "yes":
        market.market()
    else:
        print("Thanks")
        sys.exit()

def choice():
    print("tell me the reason")
    print("1.price is high ")
    print("2.no need of this")
    print("enter 1 or 2")



def fix():
    print("price is fixed")
market()