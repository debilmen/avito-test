from sqlalchemy import Column, VARCHAR, BOOLEAN, INT, LargeBinary

from db.models import BaseModel


class DBAds(BaseModel):

    __tablename__ = 'Ads'

    name = Column(VARCHAR(200), nullable=False)
    description = Column(VARCHAR(1000))
    photo = Column(VARCHAR(50), nullable=False)
    price = Column(VARCHAR(50))
    all_photo = Column(VARCHAR(1000), nullable=False)

