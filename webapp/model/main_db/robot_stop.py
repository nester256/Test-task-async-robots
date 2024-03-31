from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from webapp.model.meta import DEFAULT_SCHEMA, Base


class Robot_stop(Base):
    __tablename__ = 'robot_stop'
    __table_args__ = ({'schema': DEFAULT_SCHEMA},)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    num: Mapped[int] = mapped_column(Integer)
