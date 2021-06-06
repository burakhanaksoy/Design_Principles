class Machine:
    def print(self):
        raise NotImplementedError

    def fax(self):
        raise NotImplementedError

    def scan(self):
        raise NotImplementedError


class Printer:
    @abstractmethod
    def print(self):
        raise NotImplementedError


class Faxer:
    @abstractmethod
    def fax(self):
        raise NotImplementedError


class Scanner:
    @abstractmethod
    def scan(self):
        raise NotImplementedError


class ModernPrinter(Printer, Faxer, Scanner):
    def print(self):
        # does something
        pass

    def fax(self):
        # does something
        pass

    def scan(self):
        # does something
        pass


class OldPrinter(Printer):
    def print(self):
        # does something
        pass


printer = ModernPrinter()
printer.fax()
printer.scan()
printer.print()

old_printer = OldPrinter()
old_printer.print()
