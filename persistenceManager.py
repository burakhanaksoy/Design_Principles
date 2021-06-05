class PersistenceManager:
    @staticmethod
    def save(journal, filename):
        ''' Persists data to filename '''
        with open(f'{filename}', 'w') as f:
            f.write(str(journal))

    @staticmethod
    def load(filename):
        ''' Loads data from filename '''
        with open(f'{filename}', 'r') as f:
            return f.read()
