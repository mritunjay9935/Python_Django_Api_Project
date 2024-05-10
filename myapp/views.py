from django.db.models import Q
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response


class UserListCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()

        # Filtering
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

        # Sorting
        sort = self.request.query_params.get('sort', None)
        if sort is not None:
            if sort.startswith('-'):
                queryset = queryset.order_by(sort)
            else:
                queryset = queryset.order_by('-' + sort)

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({}, status=status.HTTP_201_CREATED, headers=headers)


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()

        # Filtering
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

        # Sorting
        sort = self.request.query_params.get('sort', None)
        if sort is not None:
            if sort.startswith('-'):
                queryset = queryset.order_by(sort)
            else:
                queryset = queryset.order_by('-' + sort)

        return querysetzer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({}, status=status.HTTP_200_OK)
