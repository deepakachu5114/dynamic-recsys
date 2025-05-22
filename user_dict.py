class UserProfile:
    def __init__(self, user_id, name, age, nationality, language_level, favorite_movies, favorite_books, favorite_tv_shows, hobbies, favorite_artists, favorite_songs):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.nationality = nationality
        self.language_level = language_level
        self.favorite_movies = favorite_movies
        self.favorite_books = favorite_books
        self.favorite_tv_shows = favorite_tv_shows
        self.hobbies = hobbies
        self.favorite_artists = favorite_artists
        self.favorite_songs = favorite_songs

    def __str__(self):
        return f"User ID: {self.user_id}\n" \
               f"Name: {self.name}\n" \
               f"Age: {self.age}\n" \
               f"Nationality: {self.nationality}\n" \
               f"Language Level: {self.language_level}\n" \
               f"Favorite Movies: {', '.join(self.favorite_movies)}\n" \
               f"Favorite Books: {', '.join(self.favorite_books)}\n" \
               f"Favorite TV Shows: {', '.join(self.favorite_tv_shows)}\n" \
               f"Hobbies: {', '.join(self.hobbies)}\n" \
               f"Favorite Artists: {', '.join(self.favorite_artists)}\n" \
               f"Favorite Songs: {', '.join(self.favorite_songs)}"





