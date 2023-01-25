from group.serializers import GroupSerializer
from group.models import Group
from rest_framework.viewsets import ModelViewSet

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    