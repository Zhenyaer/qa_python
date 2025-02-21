import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        collector = BooksCollector()
        collector.books_genre['Видоизмененный углерод'] = 'Детективы'
        collector.books_genre['Пространство'] = ''
        collector.books_genre['Шерлок Холмс'] = 'Детективы'
        collector.books_genre['Том и Джерри'] = 'Мультфильмы'
        return collector

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_book_collector_genre(self, collector, genre):
        assert genre in collector.genre

    def test_book_collector_genre_age_rating(self, collector):
        assert len(collector.genre_age_rating) > 0 and 'Ужасы' in collector.genre_age_rating

    def test_add_new_book_in_books(self, collector):
        collector.add_new_book('Ромео и Джульетта')
        assert 'Ромео и Джульетта' in collector.books_genre.keys()

    def test_add_new_book_book_not_in_books(self, collector):
        collector.add_new_book('Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции')
        assert ('Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции'
                not in collector.books_genre.keys())

    def test_set_book_genre_for_books(self, collector):
        collector.set_book_genre('Пространство', 'Фантастика')
        assert collector.books_genre['Пространство'] == 'Фантастика'

    def test_get_book_genre_from_books(self, collector):
        assert collector.get_book_genre('Видоизмененный углерод') == 'Детективы'

    def test_get_books_with_specific_genre_from_books(self, collector):
        assert collector.get_books_with_specific_genre('Детективы') == ['Видоизмененный углерод', 'Шерлок Холмс']

    def test_get_books_genre_in_books(self, collector):
        assert collector.books_genre == {'Видоизмененный углерод': 'Детективы',
                                     'Пространство': '',
                                     'Шерлок Холмс': 'Детективы',
                                     'Том и Джерри': 'Мультфильмы'}

    def test_get_books_for_children_in_books(self, collector):
        assert collector.get_books_for_children() == ['Том и Джерри']

    def test_add_book_in_favorites_from_books(self, collector):
        collector.add_book_in_favorites('Видоизмененный углерод')
        assert collector.favorites == ['Видоизмененный углерод']

    def test_delete_book_from_favorites_from_books(self, collector):
        collector.favorites.append('Том и Джерри')
        collector.favorites.append('Шерлок Холмс')
        collector.delete_book_from_favorites('Шерлок Холмс')
        assert collector.favorites == ['Том и Джерри']

    def test_get_list_of_favorites_books_from_books(self, collector):
        collector.favorites.append('Том и Джерри')
        collector.favorites.append('Шерлок Холмс')
        assert collector.get_list_of_favorites_books() == ['Том и Джерри', 'Шерлок Холмс']
