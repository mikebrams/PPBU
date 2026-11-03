class Human():
    def __init__(self, name, *entities, magic=0):
        self.name = name
        self.magic = magic
        self.entities = list(entities)

    def change_name(self, name):
        self.name += ' ' + name

    def __add__(self, other):
        self.magic += len(other) // 4
        self.entities.append(other)
        return self
        # return Human(self.name, *self.entities, magic=self.magic)

    def __call__(self, num):
        return self.entities[:num]

    def __eq__(self, other):
        return (self.magic == other.magic and len(self.entities) == len(other.entities)
                and self.name == other.name)

    def __gt__(self, other):
        if self.magic > other.magic:
            return True
        elif (self.magic == other.magic
              and len(self.entities) == len(other.entities)):
            return True
        elif (self.magic == other.magic and len(self.entities) == len(other.entities)
                and self.name > other.name):
            return True
        return False

    def __le__(self, other):
        if self.magic < other.magic:
            return True
        elif (self.magic == other.magic
              and len(self.entities) < len(other.entities)):
            return True
        elif (self.magic == other.magic and len(self.entities) == len(other.entities)
                and self.name < other.name):
            return True
        return self == other

    def __ne__(self, other):
        return (self.magic != other.magic or len(self.entities) != len(other.entities)
                and self.name != other.name)

    def __sub__(self, other):
        name = self.name[:3].capitalize() + other.name[-3:].capitalize()
        entities = list(set(self.entities) - set(other.entities))
        entities.sort()
        return Human(name, *entities, magic=0)


    def __str__(self):
        return f'Человек по имени {self.name} ({', '.join(self.entities)}, {self.magic})'


# hm = Human('Illmarrannen', 'Forgiving', 'Forgiven', magic=2)
# hm.change_name('Rual')
# id_hm = id(hm)
# hm += 'Skyman'
# print(hm, hm(2), sep='\n')
# print(id_hm == id(hm))

hm = Human('Marran', 'Hanger', 'Stick', 'Wizzard', magic=10)
hm1 = Human('Lart', 'Wizzard')
print(hm, hm1, sep='\n')
print(hm > hm1, hm <= hm1, hm == hm1)
hm2 = hm - hm1
print(hm2)
print(hm2 > hm1, hm2 <= hm, hm2 != hm)
