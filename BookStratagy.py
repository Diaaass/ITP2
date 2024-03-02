from abc import ABC, abstractmethod

class BookStrategy(ABC):
    @abstractmethod
    def add_book(self, connection):
        pass

    @abstractmethod
    def view_all_books(self, connection):
        pass

    @abstractmethod
    def update_book(self, connection):
        pass

    @abstractmethod
    def delete_book(self, connection):
        pass
