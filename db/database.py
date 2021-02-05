from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import sessionmaker, Session, Query
from sqlalchemy import desc
from db.exceptions import DBIntegrityException, DBDataException
from db.models import BaseModel, DBAds


class DBSession:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def query(self, *args, **kwargs) -> Query:
        return self._session.query(*args, **kwargs)

    def get_ad_by_id(self, ad_id: int):
        return self.query(DBAds).filter(DBAds.id == ad_id).first()

    def get_ads(self):
        return self.query(DBAds)

    def get_lst_descend_price(self, start, end):
        return self.get_ads().order_by(desc("price")).slice(start, end)

    def get_lst_ascend_price(self, start, end):
        return self.get_ads().order_by("price").slice(start, end)

    def get_lst_ascend_date_old(self, start, end):
        return self.get_ads().order_by("created_at").slice(start, end)

    def get_lst_descend_date_new(self, start, end):
        return self.get_ads().order_by(desc("created_at")).slice(start, end)

    def add_model(self, model: BaseModel):
        try:
            self._session.add(model)
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException(e)

    def commit_session(self, need_close: bool = False):
        try:
            self._session.commit()
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException(e)

        if need_close:
            self.close_session()

    def close_session(self):
        self._session.close()


class DataBase:
    connection: Engine
    session_factory: sessionmaker
    _test_query = 'SELECT 1'

    def __init__(self, connection: Engine):
        self.connection = connection
        self.session_factory = sessionmaker(bind=self.connection)

    def check_connection(self):
        self.connection.execute(self._test_query).fetchone()

    def make_session(self) -> DBSession:
        session = self.session_factory()
        return DBSession(session)
