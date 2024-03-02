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
