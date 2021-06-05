from persistence_manager import PersistenceManager


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count} : {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


my_journal = Journal()
my_journal.add_entry('Bugun guzel bir gundu..')
my_journal.add_entry('Sahilde dolasmak cok keyifliydi..')

# my_journal.save('My First Journal.txt')
# j = my_journal.load('My First Journal.txt')
PersistenceManager.save(my_journal, 'My First Journal.txt')
j = PersistenceManager.load('My First Journal.txt')
print(j)
