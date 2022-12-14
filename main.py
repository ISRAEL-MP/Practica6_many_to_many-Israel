from src.modelo.declarative_base import Base, engine, session
from src.modelo.Actor import Actor
from src.modelo.Movie import Movie
from src.modelo.declarative_base import session
from src.logica.PersistenciaActor import PersistenciaActor
from src.logica.PersistenciaMovie import PersistenciaMovie

def almacenar():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    persistenciaActor = PersistenciaActor()
    persistenciaMovie = PersistenciaMovie()

    # crear Actor
    actor1 = Actor(name="Nombre del Actor")
    actor2 = Actor(name="Elvis Carmen")
    session.add(actor1)
    session.add(actor2)
    session.commit()

    # crear Peliculas
    movie1 = Movie(pelicula="Pedro Cardenas")
    movie2 = Movie(pelicula="Buen Tipo")
    session.add(movie1)
    session.add(movie2)
    session.commit()

    # Relacionar Actor con peliculas
    actor1.comments = [movie2]
    actor2.comments = [movie1]
    session.commit()

    persistenciaActor.VerFilas()
    persistenciaMovie.VerFilas()

    session.close()

def almacenarPersitencia():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    persistenciaActor = PersistenciaActor()
    persistenciaMovie = PersistenciaMovie()

    # crear Actor
    persistenciaActor.agregarActor(name="Aplicaciones de ML en medicina")
    persistenciaActor.agregarActor(name="Ingeniería de software ágil")
    actor1 = persistenciaActor.dar_id(1)
    actor2 = persistenciaActor.dar_id(2)

    # crear Pelicula
    persistenciaMovie.agregarMovie(pelicula="Es un artículo de revisión")
    persistenciaMovie.agregarMovie(pelicula="Buen artículo")
    movie1 = persistenciaMovie.dar_id(1)
    movie2 = persistenciaMovie.dar_id(2)

    # Relacionar Actor con Peliculas
    actor1.movies = [movie2]
    actor2.movies = [movie1]
    session.commit()

    persistenciaActor.VerFilas()
    persistenciaMovie.VerFilas()

    session.close()

if __name__ == '__main__':
   almacenar()
   #almacenarPersitencia()