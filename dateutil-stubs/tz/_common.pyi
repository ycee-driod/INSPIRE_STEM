import abc
from datetime import datetime, timedelta, tzinfo
from typing import ClassVar

def tzname_in_python2(namefunc): ...
def enfold(dt: datetime, fold: int = 1): ...

class _DatetimeWithFold(datetime):
    @property
    def fold(self): ...

# Doesn't actually have ABCMeta as the metaclass at runtime,
# but mypy complains if we don't have it in the stub.
# See discussion in #8908
class _tzinfo(tzinfo, metaclass=abc.ABCMeta):
    def is_ambiguous(self, dt: datetime) -> bool: ...
    def fromutc(self, dt: datetime) -> datetime: ...

class tzrangebase(_tzinfo):
    def __init__(self) -> None: ...
    def utcoffset(self, dt: datetime | None) -> timedelta | None: ...
    def dst(self, dt: datetime | None) -> timedelta | None: ...
    def tzname(self, dt: datetime | None) -> str: ...
    def fromutc(self, dt: datetime) -> datetime: ...
    def is_ambiguous(self, dt: datetime) -> bool: ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __ne__(self, other): ...
    __reduce__ = object.__reduce__
