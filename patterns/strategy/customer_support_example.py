import string
import random
from abc import ABC, abstractmethod


class ProcessTicketStrategy(ABC):
    @abstractmethod
    def process_tickets(self, ticket_list): pass


class FIFOProcessStrategy(ProcessTicketStrategy):
    def process_tickets(self, ticket_list):
        return ticket_list


class FILOProcessStrategy(ProcessTicketStrategy):
    def process_tickets(self, ticket_list):
        return list(reversed(ticket_list))


class RandomProcessStrategy(ProcessTicketStrategy):
    def process_tickets(self, ticket_list):
        list_copy = ticket_list.copy()
        random.shuffle(list_copy)
        return list_copy

class EmptyListStrategy(ProcessTicketStrategy):
    def process_tickets(self, ticket_list):
        return []

def generateID(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class CustomerTicket:
    def __init__(self, name, issue):
        self.id = generateID()
        self.name = name
        self.issue = issue

    def __str__(self):
        info = [f'ID:\t{self.id}', f'Name:\t{self.name}',
                f'Issue:\t{self.issue}']
        return '\n'.join(info)


strategy_list = [
    ('FIFOProcessStrategy', FIFOProcessStrategy()),
    ('FILOProcessStrategy', FILOProcessStrategy()),
    ('RandomProcessStrategy', RandomProcessStrategy()),
    ('EmptyListStrategy',EmptyListStrategy())]


class TicketSupport:

    def __init__(self, process_strategy=RandomProcessStrategy()):
        self.process_strategy = process_strategy
        self.tickets = []

    def create_ticket(self, name, issue):
        self.tickets.append(CustomerTicket(name, issue))

    def handle_tickets(self):
        processed_tickets = []

        processed_tickets = self.process_strategy.process_tickets(
            self.tickets)

        if len(processed_tickets) == 0:
            print('No tickets to process')
            return

        for ticket in processed_tickets:
            print('=========== PROCESSING TICKET ===========')
            print('=========================================')
            print(ticket)
            print('=========================================')

    def set_strategy(self, strategy):
        self.process_strategy = strategy


class App:
    def __init__(self):
        print('Welcome to ticket creator..')
        print(
            'To create your ticket, please write it in the following format:[Customer Name, Issue Content]')
        self.ticket_support = TicketSupport()

    def game(self):
        while(True):
            s = input('Customer Name: ')
            name = s
            s = input('Issue Content: ')
            issue = s

            self.ticket_support.create_ticket(name, issue)

            s = input('Add another one?(Y/n)')
            if s.lower() == 'y':
                pass
            elif s.lower() == 'n':
                break

        print('\nSelect a process strategy:')
        for idx, strategy in enumerate(strategy_list):
            print(f'{idx}. {strategy[0]}')

        idx = int(input(''))
        self.ticket_support.set_strategy(strategy_list[idx][1])

        self.ticket_support.handle_tickets()


if __name__ == "__main__":
    App().game()
