from rest_framework.pagination import LimitOffsetPagination


class LimitOffSetPaginationWithUpperBound(LimitOffsetPagination):
    max_limit = 8
