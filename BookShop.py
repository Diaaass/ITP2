import psycopg2
from BookManager import BookManager
from PostgreSQLBookStrategy import PostgreSQLBookStrategy

class BookShop:
    @staticmethod
    def main():
        try:
            while True:
                connection = psycopg2.connect(host="localhost", dbname="User", user="postgres", password="NuOchenHard")

                strategy = PostgreSQLBookStrategy()
                book_manager = BookManager(strategy, connection)

                print("Choose an option:")
                print("1. Add book")
                print("2. View all books")
                print("3. Update book")
                print("4. Delete book")
                print("5. Exit")
                option = int(input("Choose the number: "))

                if option == 1:
                    book_manager.add_book()
                elif option == 2:
                    book_manager.view_all_books()
                elif option == 3:
                    book_manager.update_book()
                elif option == 4:
                    book_manager.delete_book()
                elif option == 5:
                    print("Thanks for using our system.")
                    break
                else:
                    print("Invalid option. Please choose again.")
        except psycopg2.DatabaseError as e:
            print(f"Error accessing database: {e}")
        finally:
            if connection:
                connection.close()

if __name__ == "__main__":
    BookShop.main()
