from src.modelo.Actor import Actor
from src.modelo.Movie import Movie
from sqlalchemy.exc import SQLAlchemyError
from src.modelo.declarative_base import session

class PersistenciaActor():
    def agregarActor(self, name):
        busqueda = session.query(Actor).filter(Actor.name == name).all()
        if len(busqueda) == 0:
            actor = Actor(name=name)
            session.add(actor)
            session.commit()
            return True
        else:
            return False

    def VerFilas(self):
        actores = session.query(Actor).all()
        print('\n### Actores:')
        for actor in actores:
            print(f'id: {actor.id} Name: {actor.name}')
        print('')

    def eliminarFilaAFila(self):
        actores = session.query(Actor).all()
        for actor in actores:
            session.delete(actor)
        session.commit()

    def eliminarFilaSQL(self):
        sentencia = "DELETE  from actores"
        try:
            data_source = session.execute(sentencia)
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            print("Tabla actores")
            print("Nro de registros borrados : ", data_source.rowcount)


    def dar_id(self, id):
        return session.query(Actor).get(id)