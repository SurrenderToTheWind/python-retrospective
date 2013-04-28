class Person:

    def __init__(
        self, name, birth_year,
        gender, mother=None, father=None,
    ):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.mother = mother
        self.father = father
        self.kids = []
        if mother is not None:
            self.mother.kids.append(self)
        if father is not None:
            self.father.kids.append(self)

    def get_brothers(self):
        return self.get_siblings(gender='M')

    def get_sisters(self):
        return self.get_siblings(gender='F')

    def get_siblings(self, gender=None):
        siblings = []
        if self.father is not None:
            siblings += self.father.children(gender)
        if self.mother is not None:
            siblings += self.mother.children(gender)
        non_doubling_siblings = {x for x in siblings if x != self}
        return list(non_doubling_siblings)

    def children(self, gender="both"):
        if gender == 'F':
            return [child for child in self.kids if child.gender is 'F']
        elif gender == 'M':
            return [child for child in self.kids if child.gender is 'M']
        else:
            return self.kids

    def is_direct_successor(self, other_person):
        return self in other_person.kids or other_person in self.kids
