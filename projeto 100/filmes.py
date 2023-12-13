class MovieReview:
    def __init__(self, movie_name, story_rating, actor_rating, music_rating):
        self.movie_name = movie_name
        self.story_rating = story_rating
        self.actor_rating = actor_rating
        self.music_rating = music_rating
        self.avg = int((self.story_rating + self.actor_rating + self.music_rating) / 3)
        self.myrating = {'movie_name': self.movie_name, 'story_rating': self.story_rating,
                         'actor_rating': self.actor_rating, 'music_rating': self.music_rating,
                         'avg_rating': self.avg}

    def add_movie_ratings(self, movie_list):
        movie_list.append(self.myrating)

    def get_star_rating(self):
        stars = ''
        for i in range(self.avg):
            stars += '*'
        print(f"Movie: {self.movie_name} Avg Rating: {self.avg} Stars: {stars}")


movie_reviews = []

movie1 = MovieReview("Filme1", 4, 5, 4)
movie2 = MovieReview("Filme2", 5, 4, 5)
movie3 = MovieReview("Filme3", 3, 3, 3)

movie1.add_movie_ratings(movie_reviews)
movie2.add_movie_ratings(movie_reviews)
movie3.add_movie_ratings(movie_reviews)

for movie in movie_reviews:
    review = MovieReview(movie['movie_name'], movie['story_rating'], movie['actor_rating'], movie['music_rating'])
    review.get_star_rating()