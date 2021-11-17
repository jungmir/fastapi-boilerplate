from datetime import datetime

from sqlalchemy import Column, DateTime
from server.database.connection import Base
from server.database.models.mixin.activerecord import ActiveRecordMixin
from server.database.models.mixin.repr import ReprMixin
from server.database.models.mixin.serialize import SerializeMixin
from server.database.models.mixin.smartquery import SmartQueryMixin
from server.database.models.mixin.timestamp import TimestampsMixin

class BaseMixin(
    Base,
    ActiveRecordMixin,
    ReprMixin,
    SerializeMixin,
    SmartQueryMixin,
    TimestampsMixin
):
    __abstract__ = True
    # created_at = Column(
    #     DateTime,
    #     default=datetime.now(),
    #     nullable=False
    # )
    # updated_at = Column(
    #     DateTime,
    #     default=datetime.now(),
    #     onupdate=datetime.now(),
    #     nullable=False
    # )
    pass