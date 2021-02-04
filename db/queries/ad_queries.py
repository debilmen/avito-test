from typing import List

from api.request import RequestCreateDto
from db.database import DBSession
from db.models import DBAds
from db.exceptions import DBAdNotExistException


def create_ad(session: DBSession, ad: RequestCreateDto) -> DBAds:
    new_ad = DBAds(
        name=ad.name,
        description=ad.description,
        photo=ad.photo[0],
        all_photo=[link for link in ad.photo],
        price=ad.price,
    )
    session.add_model(new_ad)

    return new_ad


def get_ad(session: DBSession, ad_id: int) -> DBAds:
    db_ad = session.get_ad_by_id(ad_id)
    if db_ad is None:
        raise DBAdNotExistException("Ad not exist")
    return db_ad


def get_list(session: DBSession) -> List[DBAds]:
    lst = session.get_lst()
    return lst
