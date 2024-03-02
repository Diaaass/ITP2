class PostgreSQLBookStrategy:
    def add_book(self, connection):
        new_id = int(input("Enter free ID: "))
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (new_id,))
            if cursor.fetchone():
                print("This id already exists.")
                return

            new_title = input("Enter book title: ")
            new_genre = input("Enter book genre: ")
            new_release_year = int(input("Enter release year: "))
            new_developer = input("Enter author: ")
            new_price = int(input("Enter book price: "))

            insert_query = "INSERT INTO users (id, title, genre, release_year, developer, price) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (new_id, new_title, new_genre, new_release_year, new_developer, new_price))
            connection.commit()
            print("The book has been successfully added.")

    def view_all_books(self, connection):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            for row in cursor:
                print(row)

    def update_book(self, connection):
        book_id = int(input("Enter book ID: "))
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (book_id,))
            if not cursor.fetchone():
                print(f"No book found with that ID: {book_id}")
                return

            new_title = input("Enter book title: ")
            new_genre = input("Enter book genre: ")
            new_release_year = int(input("Enter release year: "))
            new_developer = input("Enter book developer: ")
            new_price = int(input("Enter book price: "))

            update_query = "UPDATE users SET title=%s, genre=%s, release_year=%s, developer=%s, price=%s WHERE id=%s"
            cursor.execute(update_query, (new_title, new_genre, new_release_year, new_developer, new_price, book_id))
            connection.commit()

    def delete_book(self, connection):
        book_id = int(input("Enter book ID to delete: "))
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s", (book_id,))
            connection.commit()
    def delete_all_books(self, connection):
        confirmation = input("Are you sure you want to delete all books? Type 'yes' to confirm: ")
        if confirmation.lower() == 'yes':
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM users")
                connection.commit()
                print("All books have been deleted.")
        else:
            print("Deletion cancelled.")

    def reserve_book(self, connection):
        book_id = int(input("Enter book ID to reserve: "))
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (book_id,))
            book = cursor.fetchone()
            if not book:
                print(f"No book found with that ID: {book_id}")
                return

            # Check if the book is already reserved
            if book.get('reserved'):  # Assuming there's a 'reserved' column in the table
                print("This book is already reserved.")
                return

            cursor.execute("UPDATE users SET reserved = True WHERE id = %s", (book_id,))
            connection.commit()
            print(f"Book ID {book_id} has been reserved.")
