from dict import resources, MENU


def give_report(current_balance):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${round(current_balance,2)}")

def check_resources(order):
    ingridents=MENU[order]['ingredients']
    if resources['water']<ingridents['water']:
       return (False,'water')
    elif resources['milk']<ingridents['milk']:
        return(False,'milk')
    elif resources['coffee']<ingridents['coffee']:
        return(False,'coffee')
    else:
        return(True,'Clear')

def validate_money(amount,order):
    price=MENU[order]['cost']
    if amount>=price:
        refund=amount-price
        return True, round(refund,3)
    else:
        refund=amount
        return False, round(refund,3)
def process_inventory(order):
    ingredients=MENU[order]['ingredients']
    resources['water']-=ingredients['water']
    resources['milk']-=ingredients['milk']
    resources['coffee']-=ingredients['coffee']

def main():
    balance=0.0
    money=[0,0,0,0]
    while True:
        order=input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order=='report':
            give_report(balance)
        elif order=='off':
            break
        else:
            status,problem=check_resources(order)
            if not status:
                print(f"Sorry there is not enough {problem}")
            else:
                money[0]=0.25*(int(input("How many quarters?: ")))
                money[1]=0.1*(int(input("How many dimes?: ")))
                money[2]=0.05*(int(input("How many nickles?: ")))
                money[3]=0.01*(int(input("How many pennies?:  ")))
                total=sum(money)
                enough,refund=validate_money(total,order)
                if enough:
                    balance=balance+total-refund
                    print(f"Here is ${refund} in change 💵 ")
                    process_inventory(order)
                    print(f"Here is your {order} ☕️ enjoy.")
                else:
                    print(f"sorry that's not enough money,${refund} Money Refunded.💶")



if __name__=="__main__":
    main()
