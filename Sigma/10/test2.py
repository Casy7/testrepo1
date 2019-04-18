class Book():
    def __init__(self, fst_name, lst_name=None, mobile_phone=None, work_phone=None, second_phone=None, mail=None, more_info={}):
        self.fst_name = fst_name
        self.lst_name = lst_name
        self.mobile_phone = mobile_phone
        self.second_phone = second_phone
        self.more_info = more_info
        self.work_phone = work_phone
        self.mail = mail

    def info(self):
        print(self.fst_name, self.lst_name, self.mail)
        for i in self.more_info:
            print(i, ": ", self.more_info[i], sep="")

    def add_adress(self, adress):
        self.adress = adress

    def add_mail(self, input_mail):
        self.mail = input_mail

    def add_work_phone(self, input_work_phone):
        self.work_phone = input_work_phone

    def add_second_phone(self, input_second_phone):
        self.second_phone = input_second_phone

    def add_else_info(self, kind_of_info, info):
        self.more_info[kind_of_info] = info


class Person(Book):
    def __init__(self, name, more_info={}):
        self.name = name

    @Book
    def get_info_from_book(self, name):
        print(Person.__dict__)


# ,"299792458","2718281828","epbitkplz@gmail.com")
pirr = Book(fst_name="Pirr", mobile_phone="3141592653",
            mail="epbitkplz@gmail.com")
Person.get_info_from_book(Person, "pirr")
pirr.add_else_info("Должность", "Младший дворник")
pirr.info()
