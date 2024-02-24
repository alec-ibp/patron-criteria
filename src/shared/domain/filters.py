from enum import Enum


class Filter:
    def __init__(self, field: str, value: str, operator: str):
        self.field: str = field
        self.value: str = value
        self.operator: str = operator


class Ordering:
    class OrderingType(Enum):
        ASC: str = "asc"
        DESC: str = "desc"

    def __init__(self, field: str):
        if field.startswith("-"):
            self.order_by: str = field[1:]
            self.order_type: str = Ordering.OrderingType.DESC.value
        else:
            self.order_by: str = field
            self.order_type: str = Ordering.OrderingType.ASC.value


class Criteria:
    def __init__(self, filters: list[Filter], ordering: Ordering, limit: int | None = None, offset: int | None = None):
        self.filters: list[Filter] = filters
        self.ordering: Ordering = ordering
        self.limit: int | None = limit
        self.offset: int | None = offset
