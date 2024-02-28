from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_admin']  # 필요한 필드를 추가합니다.
        # 비밀번호와 같은 민감한 정보는 포함시키지 않도록 주의합니다.
