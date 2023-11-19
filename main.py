# 1 Задание
class Car:
    def go(self):
        pass

my_car = Car()
my_car.go() #В метод go () аргументы не передаются
# 2 Задание

class Book:
    def __init__(self, name_book, author, name_publisher):
        self.name_book = name_book
        self.author = author
        self.name_publisher = name_publisher

    def get_name_book(self):
        return self.name_book
    def set_name_book(self, name_book):
        self.name_book = name_book
    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author

    def get_name_publisher(self):
        return self.name_publisher
    def set_name_publisher(self, name_publisher):
        self.name_publisher = name_publisher

    def __str__(self):
        return f'Название книги: {self.name_book}, автор: {self.author}, издатель: {self.name_publisher}'

bk = Book('Vidland', 'Misha Zalirov', 'Miroslava Legaeva')
bk.set_name_book('boont')
bk.set_author('name2')
bk.set_name_publisher('name3')
print(bk)
# 3 Задание

class Pet:
    def __init__(self):
        self._name = ""
        self._animal_type = ""
        self._age = 0

    def set_name(self, name):
        self._name = name

    def set_animal_type(self, animal_type):
        self._animal_type = animal_type

    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def get_animal_type(self):
        return self._animal_type

    def get_age(self):
        return self._age

my_pet = Pet()
my_pet.set_name(input("Введите имя своего домашнего животного: "))
my_pet.set_animal_type(input("Введите тип домашнего животного (например, собака, кот, птица): "))
my_pet.set_age(int(input("Введите возраст домашнего животного: ")))

print(f"Имя: {my_pet.get_name()}")
print(f"Тип: {my_pet.get_animal_type()}")
print(f"Возраст: {my_pet.get_age()} лет")
# 4 Задание

class Car:
    def __init__(self, _year_model, make):
        self._year_model = ''
        self.make = make
        self._speed = 0

    def accelerate(self):
        self._speed += 5

    def brake(self):
        self._speed -= 5
    def get_speed(self):
        return self._speed

my_car = Car("2004", "Lada Granta")

print("Ускорение:")
for _ in range(5):
    my_car.accelerate()
    print(f"Текущая скорость: {my_car.get_speed()}")

print("\nТорможение:")
for _ in range(5):
    my_car.brake()
    print(f"Текущая скорость: {my_car.get_speed()}")
# 5 Задание

class InfoPerson:
    def __init__(self, name, address, age, phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address

    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

    def get_phone_number(self):
        return self.phone_number
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

person1 = InfoPerson("Андрей", "Ваш адрес", 17, "+7 992 221 *0 **")
person2 = InfoPerson("Михаил", "Адрес друга1", 28, "+7 983 238 ** **")
person3 = InfoPerson("Артём", "Адрес друга2", 22, "+7 994 314 1* **")
print("Информация о вас:")
print("Имя:", person1.get_name())
print("Адрес:", person1.get_address())
print("Возраст:", person1.get_age())
print("Телефонный номер:", person1.get_phone_number())
print()

print("Информация о друге 1:")
print("Имя:", person2.get_name())
print("Адрес:", person2.get_address())
print("Возраст:", person2.get_age())
print("Телефонный номер:", person2.get_phone_number())
print()

print("Информация о друге 2:")
print("Имя:", person3.get_name())
print("Адрес:", person3.get_address())
print("Возраст:", person3.get_age())
print("Телефонный номер:", person3.get_phone_number())
# 6 Задание

class Employee:
    def __init__(self, name, number, department, post):
        self.name = name
        self.number = number
        self.departament = department
        self.post = post

    def info_employee(self):
        print(f'Имя: {self.name}, индентификационный номер: {self.number}, отдел: {self.departament}, должность {self.post}')
employee1 = Employee("Сьюзан Мейерс", 47899, "Бухгалтерия", "Вице-президент")
employee2 = Employee("МаркДжоунс", 39119, "ИТ", "Программист")
employee3 = Employee("Джой Роджерс", 81774, "Производственный", "Инженер")

employee1.info_employee()
employee2.info_employee()
employee3.info_employee()
# 7 Задание
class RetailItem:
    def __init__(self, number, description, units_in_stock, price):
        self.number = number
        self.description = description
        self.units_in_stock = units_in_stock
        self.price = price

    def info(self):
        print(f'Товар № {self.number}\nОписание товара: {self.description}\nКоличество на складе: {self.units_in_stock}\nЦена: {self.price}\n')

item1 = RetailItem(1,"Пиджак", 12, 59.95)
item2 = RetailItem(2,"Дизайнерские джинсы", 40, 34.95)
item3 = RetailItem(3,"Рубашка", 20, 24.95)
item1.info()
item2.info()
item3.info()
# 8 Задание

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, region, postal_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.region = region
        self.postal_code = postal_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_address(self):
        return f"{self.address}, {self.city}, {self.region}, {self.postal_code}"

    def get_phone_number(self):
        return self.phone_number

    def get_emergency_contact_info(self):
        return f"{self.emergency_contact_name}: {self.emergency_contact_phone}"

class Procedure:

    def __init__(self, procedure_name, procedure_date, doctor_name, procedure_cost):
        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        self.doctor_name = doctor_name
        self.procedure_cost = procedure_cost

    def get_procedure_info(self):
        return f"Название процедуры: {self.procedure_name}\nДата: {self.procedure_date}\nВрач: {self.doctor_name}\nСтоимость: {self.procedure_cost}"

patient = Patient('Андрей', 'Анатольевич', 'Третьяков', 'окружное шоссе 30', 'елабуга', 'елабуга', '4567876', '8 992 221 ** **', 'неизвестный', '8 992 388 29 39')

procedure1 = Procedure("Врачебный осмотр", "Сегодняшняя", "Ирвин", 250.00)
procedure2 = Procedure("Рентгеноскопия", "Сегодняшняя", "Джемисон", 500.00)
procedure3 = Procedure("Анализ крови", "Сегодняшняя", "Смит", 200.00)

print("Информация о пациенте:")
print("Полное имя:", patient.get_full_name())
print("Адрес:", patient.get_address())
print("Телефонный номер:", patient.get_phone_number())
print("Контактное лицо для экстренной связи:", patient.get_emergency_contact_info())


print("\nИнформация о процедуре №1:")
print(procedure1.get_procedure_info())

print("\nИнформация о процедуре №2:")
print(procedure2.get_procedure_info())

print("\nИнформация о процедуре №3:")
print(procedure3.get_procedure_info())

total_cost = procedure1.procedure_cost + procedure2.procedure_cost + procedure3.procedure_cost
print(f"\nОбщая стоимость всех процедур: {total_cost}")
# 9 Задание
class Employee:
    def __init__(self, id_number, name, department, post):
        self.id_number = id_number
        self.name = name
        self.department = department
        self.post = post

    def display_info(self):
        print(f"ID: {self.id_number}, Имя: {self.name}, Отдел: {self.department}, Должность: {self.post}")

employees_dict = {}

def find_employee(id_number):
    if id_number in employees_dict:
        employees_dict[id_number].display_info()
    else:
        print("Сотрудник не найден.")

def add_employee(id_number, name, department, post):
    new_employee = Employee(id_number, name, department, post)
    employees_dict[id_number] = new_employee
    print("Сотрудник добавлен.")

def update_employee(id_number, name, department, post):
    if id_number in employees_dict:
        employees_dict[id_number].name = name
        employees_dict[id_number].department = department
        employees_dict[id_number].post = post
        print("Информация о сотруднике обновлена.")
    else:
        print("Сотрудник не найден.")

def delete_employee(id_number):
    if id_number in employees_dict:
        del employees_dict[id_number]
        print("Сотрудник удален.")
    else:
        print("Сотрудник не найден.")

while True:
    print("\nМеню:")
    print("1. Найти сотрудника")
    print("2. Добавить нового сотрудника")
    print("3. Изменить информацию о сотруднике")
    print("4. Удалить сотрудника")
    print("5. Выйти из программы")

    choice = input("Выберите действие (1-5): ")

    if choice == "1":
        id_number = input("Введите ID номер сотрудника: ")
        find_employee(id_number)
    elif choice == "2":
        id_number = input("Введите ID номер нового сотрудника: ")
        name = input("Введите имя: ")
        department = input("Введите отдел: ")
        post = input("Введите должность: ")
        add_employee(id_number, name, department, post)
    elif choice == "3":
        id_number = input("Введите ID номер сотрудника для изменения: ")
        name = input("Введите новое имя: ")
        department = input("Введите новый отдел: ")
        post = input("Введите новую должность: ")
        update_employee(id_number, name, department, post)
    elif choice == "4":
        id_number = input("Введите ID номер сотрудника для удаления: ")
        delete_employee(id_number)
    elif choice == "5":
        print("Программа завершена.")
        break
    else:
        print("У нас нет больше возможностей. Пожалуйста, выберите от 1 до 5.")
# 10 Задание
class RetailItem:
    def __init__(self, number, description, units_in_stock, price):
        self.number = number
        self.description = description
        self.units_in_stock = units_in_stock
        self.price = price

    def info(self):
        print(f'Товар № {self.number}\nОписание товара: {self.description}\nКоличество на складе: {self.units_in_stock}\nЦена: {self.price}\n')
class CashRegister:
    def __init__(self):
        self.items = []

    def purchase_item(self, retail_item):
        self.items.append(retail_item)

    def get_total(self):
        total_cost = sum(item.price for item in self.items)
        return total_cost

    def show_items(self):
        for item in self.items:
            item.info()

    def clear(self):
        self.items = []


cash_register = CashRegister()

item1 = RetailItem(1,"Пиджак", 12, 59.95)
item2 = RetailItem(2,"Дизайнерские джинсы", 40, 34.95)
item3 = RetailItem(3,"Рубашка", 20, 24.95)

cash_register.purchase_item(item1)
cash_register.purchase_item(item2)
cash_register.purchase_item(item3)

print("Выбранные товары:\n")
cash_register.show_items()

total_cost = round(cash_register.get_total(), 2)
print(f"Общая стоимость: {total_cost}")

cash_register.clear()
# 11 Задание
class Question:
    def __init__(self, question, op1, op2, op3, op4, correct_answer):
        self.question = question
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.correct_answer = correct_answer

    def display_question(self):
        print(f'{self.question}\n1: {self.op1}\n2: {self.op2}\n3: {self.op3}\n4: {self.op4}')

    def set_correct_answer(self, correct_answer):
        self.correct_answer = correct_answer

    def get_correct_answer(self):
        return self.correct_answer

question1 = Question("Вопрос 1: Какая самая большая планета в Солнечной системе?", "Юпитер", "Марс", "Земля", "Венера", 1)
question2 = Question("Вопрос 2: Кто написал 'Мёртвые души'?", "Достоевский", "Шекспир", "Толстой", "Гоголь", 4)
question3 = Question("Вопрос 3: Какая самая маленькая планета в Солнечной системе?", "Марс", "Меркурий", "Венера", "Сатурн", 2)
question4 = Question("Вопрос 4: Сколько сторон у квадрата?", "2", "3", "4", "5", 3)
question5 = Question("Вопрос 5: В каком году отменили крепостное право?", "1776", "1789", "1801", "1861", 4)
question6 = Question("Вопрос 6: Кто был автором картины 'Мона Лиза'?", "Микеланджело", "Леонардо да Винчи", "Ван Гог", "Пикассо", 2)
question7 = Question("Вопрос 7: Сколько материков на Земле?", "5", "6", "7", "8", 2)
question8 = Question("Вопрос 8: Сколько химических элементов в таблице Менделеева?", "96", "54", "132", "118", 4)
question9 = Question("Вопрос 9: Сколько углов в шестиугольной пирамиде?", "6", "7", "8", "5", 2)
question10 = Question("Вопрос 10: Сколько костей в человеческом скелете?", "150", "206", "250", "300", 2)

quiz_questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
def start_test():
    player1_score = 0
    player2_score = 0

    for i in range(5):
        print(f"\nВопрос {i + 1} для игрока 1:")
        quiz_questions[i].display_question()
        player1_answer = int(input("Введите номер правильного ответа (1-4): "))
        if player1_answer == quiz_questions[i].get_correct_answer():
            player1_score += 1

        print(f"\nВопрос {i + 1} для игрока 2:")
        quiz_questions[i + 5].display_question()
        player2_answer = int(input("Введите номер правильного ответа (1-4): "))
        if player2_answer == quiz_questions[i + 5].get_correct_answer():
            player2_score += 1

    print(f'Результаты:\nПервый игрок: {player1_score} очков\nВторой игрок: {player2_score} очков')

    if player1_score > player2_score:
        print('Первый игрок победил!!!')
    elif player1_score < player2_score:
        print('Второй игрок победил!!!')
    else:
        print('Ничья!')

start_test()