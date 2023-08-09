
movies = [('Captain Marvel', 7.0), ('Aladdin', 7.4), ('Toy Story 4', 8.2), ('Avengers: Endgame', 8.7)]


def find_popularity(mov):

    def get_rating(m):
        return m[1]

    most_popular = max(mov, key=get_rating)
    less_popular = min(mov, key=get_rating)

    print(f"Most popular: {most_popular[0]} - {most_popular[1]}")
    print(f"Less popular: {less_popular[0]} - {less_popular[1]}")


find_popularity(movies)
