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
        all_brothers = []
        if self.mother is not None:
            all_brothers += self.mother.children('M')
        if self.father is not None:
            all_brothers += self.father.children('M')
        non_doubling_brothers = {x for x in all_brothers if x != self}
        return list(non_doubling_brothers)

    def get_sisters(self):
        all_sisters = []
        if self.mother is not None:
            all_sisters += self.mother.children('F')
        if self.father is not None:
            all_sisters += self.father.children('F')
        non_doubling_sisters = {x for x in all_sisters if x != self}
        return list(non_doubling_sisters)

    def children(self, gender="both"):
        if gender == 'F':
            return [child for child in self.kids if child.gender is 'F']
        elif gender == 'M':
            return [child for child in self.kids if child.gender is 'M']
        else:
            return self.kids

    def is_direct_successor(self, other_person):
        return self in other_person.kids or other_person in self.kids
