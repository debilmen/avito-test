from sqlalchemy import Column, VARCHAR, BOOLEAN, INT, LargeBinary

from db.models import BaseModel


class DBAds(BaseModel):

    __tablename__ = 'Ads'

    name = Column(VARCHAR(200), nullable=False)
    description = Column(VARCHAR(1000))
    photo = Column(VARCHAR(500), nullable=False)
    price = Column(INT())
    all_photo = Column(VARCHAR(1000), nullable=False)

