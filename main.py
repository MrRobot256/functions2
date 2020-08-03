class Contact:

    def __init__(self, name, surname, telephone, favorite_contact=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.favorite_contact = favorite_contact
        self.args = args
        self.kwargs = kwargs

    def create_favorite_contact(self):
        self.favorite_contact = True

    def del_favorite_contact(self):
        self.favorite_contact = False

    def __str__(self):
        tag = '\n\t'
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.telephone}\n'
                f'В избранных: {"да" if self.favorite_contact else "нет"}\n'
                f'Доп.инфо: {tag + ", ".join(self.args if self.args else "")}'
                f'{tag + tag.join(item for item in self.kwargs) if self.kwargs else ""}'
                f'{tag + "Нет" if not self.args and not self.kwargs else ""}')


class PhoneBook:

    def __init__(self, name):
        self.name = name
        self.contacts_list = []

    def chose_contacts(self):
        for item in self.contacts_list:
            print(item)

    def add_new_person(self, Contact):
        self.contacts_list.append(Contact)

    def chose_favorite_contacts(self):
        for item in self.contacts_list:
            if item.favorite_contact:
                print(item.telephone)

    def find_contact(self, name, surname):
        for item in self.contacts_list:
            if item.name == name and item.surname == surname:
                print(item.telephone)

    def del_contact(self, telephone):
        for item in self.contacts_list:
            if item.telephone == telephone:
                self.contacts_list.remove(item)
                print(f'Удален! {telephone}')


if __name__ == '__main__':
    jhon1 = Contact('Jhon1', 'Smith1', '+891234567809', telegram='@jhony1', email='jhony1@smith1.com1')
    jhon = Contact('Jhon', 'Smith', '+791234567809', telegram='@jhony', email='jhony@smith.com')
    phonebook = PhoneBook('Телефонный справочник')
    phonebook.add_new_person(jhon)
    phonebook.add_new_person(jhon1)
    jhon.create_favorite_contact()
    print('Список контактов: ')
    phonebook.chose_contacts()
    print('____________')
    print('Избранные: ')
    phonebook.chose_favorite_contacts()
    print('____________')
    print('Выбор избранного контакта: ')
    phonebook.find_contact('Jhon', 'Smith')
    print('____________')
    print('Удаляем контакт')
    phonebook.del_contact('+891234567809')
    print('____________')
    print('Выбор контактов')
    phonebook.chose_contacts()