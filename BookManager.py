class BookManager:
    def __init__(self, strategy, connection):
        self.strategy = strategy
        self.connection = connection

    def add_book(self):
        self.strategy.add_book(self.connection)

    def view_all_books(self):
        self.strategy.view_all_books(self.connection)

    def update_book(self):
        self.strategy.update_book(self.connection)

    def delete_book(self):
        self.strategy.delete_book(self.connection)
