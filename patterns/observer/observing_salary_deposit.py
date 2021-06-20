
class Event(list):

    def notify(self, name):
        print(f'salary deposit e-mail sent to {name}')

    def __call__(self, *args, **kwargs):
        for customer in self:
            self.notify(customer.name)


class Person:
    def __init__(self, name):
        self.name = name


class Bank:

    def __init__(self, address=''):
        self.customers = []
        self.address = address
        self.maas_odemesi = Event()

    def maasi_ode(self):
        self.maas_odemesi()

    def add_customer(self, customer):
        self.customers.append(customer)


if __name__ == '__main__':
    burakhan = Person('Burakhan')
    ahmet = Person('Ahmet')
    mehmet = Person('Mehmet')

    bank = Bank()
    bank.add_customer(burakhan)
    bank.add_customer(ahmet)
    bank.add_customer(mehmet)

    bank.maas_odemesi.append(burakhan)
    bank.maas_odemesi.append(ahmet)
    bank.maasi_ode()
