from rest_framework import viewset
from .models import Member
from .serializers import MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
		queryset = Member.objects.all()
		serializer_class = MemberSerializer
