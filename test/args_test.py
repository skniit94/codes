def test(a, b, *abc, **kky):
    print (a , b, abc, kky)
    print (type(abc))
    print (type(kky))

# test(1, 2, 3, c=2)

def test2(a,b,c):
    print (a,b,c)

test2(*[1,2,3])
print (*[1,2,3])
*a, = "abc"
print (a)
a, = "a"
print (type(a))

class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

x = Comedian('a', 'c', '3')
print (f'{x!r}')