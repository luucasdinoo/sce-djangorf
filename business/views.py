from rest_framework import generics, viewsets
from business.models import Business
from business.serializers import BusinessSerializer

class BusinnesViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

# class BusinessCreateListView(generics.ListCreateAPIView):
#     queryset = Business.objects.all()
#     serializer_class = BusinessSerializer
#
# class BusinessRetrievelDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Business.objects.all()
#     serializer_class = BusinessSerializer
