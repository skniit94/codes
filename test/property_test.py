class Test():
    def __init__(self):
        print (1)

    @property
    def test(self):
        return 1


class Test2(Test):
    def __init__(self):
        print (2)

    @property
    def test(self):
        return 1 + super().test

print (Test2().test)