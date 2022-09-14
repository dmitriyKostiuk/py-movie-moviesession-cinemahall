import init_django_orm  # noqa: F401
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time,
        movie_id,
        cinema_hall_id):
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(pk=movie_id),
        cinema_hall=CinemaHall.objects.get(pk=cinema_hall_id))


def get_movies_sessions(session_date=None):
    if session_date is not None:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(session_id: int,
                         show_time=None,
                         movie_id: int = None,
                         cinema_hall_id=None):
    movie_session = MovieSession.objects.get(pk=session_id)
    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie = Movie.objects.get(pk=movie_id)
    if cinema_hall_id is not None:
        movie_session.cinema_hall = CinemaHall.objects.get(pk=cinema_hall_id)
    movie_session.save()


def delete_movie_session_by_id(session_id):
    MovieSession.objects.get(pk=session_id).delete()
