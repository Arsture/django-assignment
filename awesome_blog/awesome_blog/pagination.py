from rest_framework.pagination import CursorPagination


class CustomCursorPagination(CursorPagination):
    page_size = 10  # 한 페이지에 표시할 아이템 수
    ordering = '-created_at'  # 생성 역순 정렬
