# qa_python

# Описание тестов tests.py для класса BooksCollector в файле main.py.

# Создание фикстуры с объектом collector и наполнение collector.books_genre данными для тестов.
# def collector(self):

# Проверка содержания collector.genre.
# def test_book_collector_genre(self, collector, genre):

# Проверка наличия определенного жанра в genre_age_rating.
# def test_book_collector_genre_age_rating(self, collector):

# Проверка добавления книги в books_genre. Проверяемый метод - add_new_book.
# def test_add_new_book_in_books(self, collector):

# Проверка не добавления книги в books_genre при длине названия > 41 символа. Проверяемый метод - set_book_genre
# def test_add_new_book_book_not_in_books(self, collector):

# Проверка установке книги жанра. Проверяемый метод - set_book_genre.
# def test_set_book_genre_for_books(self, collector):

# Проверка получения жанра книги по её имени. Проверяемый метод - get_book_genre.
# def test_get_book_genre_from_books(self, collector):

# Проверка вывода списка книг с определенным жанром. Проверяемый метод - get_books_with_specific_genre.
# def test_get_books_with_specific_genre_from_books(self, collector):

# Проверка получения словаря books_genre. Проверяемый метод - get_books_genre.
# def test_get_books_genre_in_books(self, collector):

# Проверка получения списка книг, подходящим детям. Проверяемый метод - get_books_for_children.
# def test_get_books_for_children_in_books(self, collector):

# Проверка добавления книги в избранное. Проверяемый метод - add_book_in_favorites.
# def test_add_book_in_favorites_from_books(self, collector):

# Проверка удаления книги из избранного. Проверяемый метод - delete_book_in_favorites.
# def test_delete_book_from_favorites_from_books(self, collector):

# Проверка получения избранных книг. Проверяемый метод - get_list_of_favorites_books.
# def test_get_list_of_favorites_books_from_books(self, collector):
