class Person:

    def __init__(self, name, gender, age, salary):
        self.name = name
        self.gender = gender
        self.age = age
        self.salary = salary

    def __str__(self):
        if self.gender == "male":
            return f"{self.age} წლის ბატონ {self.name}-ს თვიური შემოსავალია: {self.salary} ლარი"
        elif self.gender == "female":
            return f"{self.age} წლის ქალბატონ {self.name}-ს თვიური შემოსავალია: {self.salary} ლარი"

    def monthly_income(self):
        pension = self.salary / 5
        income_tax = self.salary / 100
        return f"თქვენი ყოველთვიური გადასახადია: {pension + income_tax}"

    def retirement_savings(self):
        wliuri_income = (self.salary / 100) * 12
        if self.gender == "female" and self.age <= 30:
            return f"თქვენი საპენსიო დანაზოგია: {wliuri_income * 30}"
        elif self.gender == "male" and self.age <= 30:
            return f"თქვენი საპენსიო დანაზოგია: {wliuri_income * 35}"
        else:
            return "თქვენ საკმარისი წელი არ დაგიყვიათ ამ კომპანიაში მაშასადამე ჩვენ თქვენ არ მოგქცემთ საპენსიო დანაზოგს"

    def wasvlis_weli(self):
        if self.gender == "female" and self.age <= 30:
            return f"თქვენ პენსიაზე გახვალთ {60 - self.age} წელში"
        elif self.gender == "male" and self.age <= 30:
            return f"თქვენ პენსიაზე გახვალთ {65 - self.age} წელში"
        else:
            return "თქვენ კი გახვალთ პენსიაზე მაგრამ დანაზოგს არ გაგატანთ რადგან აქ ოცდაათი წელი არ გიმუშავიათ"


ob1 = Person("დათა", "male", 18, 1000000)
print(ob1)
print(ob1.monthly_income())
print(ob1.retirement_savings())
print(ob1.wasvlis_weli())
