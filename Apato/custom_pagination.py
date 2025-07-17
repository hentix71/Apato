from rest_framework.pagination import CursorPagination

class CustomCursorPagination(CursorPagination):
    page_size = 5 # 10 Datas per page
    ordering = "id" # Ordered Based on id ( Default = Created)