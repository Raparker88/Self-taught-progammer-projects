class Person:
    def __init__(self):
        self.name="becca"


becca=Person()
myself=becca
print(becca is myself)

me=Person()
print(becca is me)
