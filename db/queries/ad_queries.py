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
    new_ad.status_code = 201
    return new_ad


def get_ad(session: DBSession, ad_id: int) -> DBAds:
    db_ad = session.get_ad_by_id(ad_id)
    if db_ad is None:
        raise DBAdNotExistException("Ad not exist")
    return db_ad


def get_list(session: DBSession, page_n: int, ascend_price, ascend_date) -> List[DBAds]:
    page_n -= 1
    start = int(f"{page_n}0")
    end = start + 10
    if ascend_date:
        lst = session.get_lst_ascend_date_old(start, end)
    elif ascend_date is False:
        lst = session.get_lst_descend_date_new(start, end)
    else:
        lst = session.get_lst_descend_date_new(start, end)  # по умолчанию сортировка по дате "с нового"
    if ascend_price:
        lst = session.get_lst_ascend_price(start, end)
    elif ascend_price is False:
        lst = session.get_lst_descend_price(start, end)

    return lst
