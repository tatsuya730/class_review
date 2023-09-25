class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.family_name

    def entry_fee(self):
        if self.age < 20:
            return "1000"
        elif 20 <= self.age < 65:
            return "1500"
        else:
            return "1200"

    def info_csv(self):
        return self.full_name() + "," + str(self.age) + "," + self.entry_fee()


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)


print(ken.full_name())
print(ken.age)
print(ken.entry_fee())
print(ken.info_csv())

print(tom.full_name())
print(tom.age)
print(tom.entry_fee())
print(tom.info_csv())

print(ieyasu.full_name())
print(ieyasu.age)
print(ieyasu.entry_fee())
print(ieyasu.info_csv())
