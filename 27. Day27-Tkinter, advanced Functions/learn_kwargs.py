def calculate(**kwargs):
    print(kwargs) ## keyword arguments.
    for key, value in kwargs.items():
        print(f"{key} = {value}")

calculate(name="John",age=20)



def calculation(n,**kwargs):
    n+=kwargs['add'] # 2+3 =5
    n*=kwargs['multiply'] # 5*4 =20
    print(n)

calculation(2, add=3, multiply=4)



class car:
    def __init__(self, **kwargs):
        self.make= kwargs['make']
        self.model= kwargs['model']
        self.year= kwargs.get('year') ## get method returns None if it's argument is not passed or not in dictionary rather than crashing .
        self.price= kwargs.get('price')
        print(f"I am {self.make} {self.model} {self.year} {self.price}")

my_car=car(make='Nissan',model="Mustang",year=2021,price=1500)
print(my_car.make)
new_car=car(make='Ford',model="Mustang")
print(new_car.make)