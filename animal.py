class Animal:
    def __init__(self, strength, letter):
        self._strength = strength
        self._letter = letter
        self._conquered = False

    def capital_letter(self):
        print(self._letter)

    def __str__(self):
        if self._conquered:
            return "-"
        else:
            return self._letter

    def conquer(self, other):
        return self._strength > other._strength

    def equal(self, other):
        return self._strength == other._strength


class Lion(Animal):
    def __init__(self):
        super().__init__(3, "L")

    def clone_conquered(self):
        cloned = Lion()
        cloned._conquered = True
        return cloned


class Tiger(Animal):
    def __init__(self):
        super().__init__(2, "T")

    def clone_conquered(self):
        cloned = Tiger()
        cloned._conquered = True
        return cloned


class Wolf(Animal):
    def __init__(self):
        super().__init__(1, "W")

    def clone_conquered(self):
        cloned = Wolf()
        cloned._conquered = True
        return cloned


class Deer(Animal):
    def __init__(self):
        super().__init__(0, "D")

    def clone_conquered(self):
        cloned = Deer()
        cloned._conquered = True
        return cloned
