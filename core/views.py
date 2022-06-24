from rest_framework.generics import ListAPIView
from .serializers import DoctorSerializer, DirectionSerializer, SpecificDoctorSerializer
from .models import Direction, Doctor
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class GetAllDirections(ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    pagination_class = None


class GetAllDoctors(ListAPIView):
    queryset = Doctor.objects.all().order_by('sort_number').order_by('name')
    serializer_class = DoctorSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('direction__name', 'experience')
    ordering_fields = ('birthday', 'experience')

    def get_queryset(self):
        queryset = Doctor.objects.all()
        if self.request.query_params.get('exp_from'):
            queryset = queryset.filter(
                experience__gte=self.request.query_params.get('exp_from'))
        elif self.request.query_params.get('exp_to'):
            queryset = queryset.filter(
                experience__lte=self.request.query_params.get('exp_to'))
        return queryset


class GetDoctor(ViewSet):

    def list(self, request, pk=None):
        queryset = Doctor.objects.get(pk=pk)
        serializer = SpecificDoctorSerializer(instance=queryset)
        return Response(serializer.data)
