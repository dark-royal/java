class Praise:
    def __init__(self):
        self._school = ""

    def getString(self):
        school = input("enter school")

    def printString(self):
        return self._school.upper()

    def __repr__(self):
        return f'praise school:{self._school.upper()}'


praise = Praise()
#praise.getString()
print(praise.printString())
