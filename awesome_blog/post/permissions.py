from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    객체의 소유자만이 객체를 수정할 수 있게 하는 사용자 정의 권한.
    """

    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모두에게 허용됨. 따라서, 안전한 메서드(GET, HEAD, OPTIONS)는 항상 허용됨.
        if request.method in SAFE_METHODS:
            return True

        # 쓰기 권한은 객체의 소유자에게만 허용됨.
        return obj.created_by == request.user