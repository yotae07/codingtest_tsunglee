import jwt

from rest_framework            import(
    viewsets,
    status
)
from rest_framework.decorators import action
from rest_framework.response   import Response

from .models                   import User
from .serializers              import UserSerializer

from NF_codingtest.settings    import SECRET_KEY, ALGORITHM

class UserView(viewsets.ModelViewSet):
    queryset         = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def signin(self, request, name):
        user_qs = self.queryset.filter(name=name)
        token   = jwt.encode({'user': user_qs.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
        return Response(token, status=status.HTTP_200_OK)
