import uuid
from django.shortcuts import get_object_or_404
from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveAPIView

from rest_framework.decorators import action
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ViewSet
from rest_framework import status


"""
    Docs:
        - https://testdriven.io/blog/drf-views-part-1/
        - https://testdriven.io/blog/drf-views-part-2/
        - https://testdriven.io/blog/drf-views-part-3/

    Paginator:
        - https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html

    Exceptions:
        - https://www.programiz.com/python-programming/user-defined-exception

    Docs:
        - https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
"""


class ProjectModelViewSet(ModelViewSet):
    """
        Paginação nativa.
        Methodos Implementados:
            CreateModelMixin,
            RetrieveModelMixin,
            UpdateModelMixin,
            DestroyModelMixin,
            ListModelMixin,
            GenericViewSet

    """
    # authentication_classes = (UserFirebaseAuthentication,)
    queryset = Project.objects.all().order_by("-created_at")
    serializer_class = ProjectSerializer
    tracker_id = Profilling().tracker_id

    @action(detail=False, methods=['get'])
    def another(self, request):
        project_count = Project.objects.count()

        return Response({'count': project_count})

    @action(detail=False, methods=['get'])
    def error(self, request):
        raise ProjectAPINotFoundError()


class ProjectModelMixinViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    """
        Paginação nativa.
        Methodos Implementados apenas os selecionados
            - ListModelMixin,
            - RetrieveModelMixin,

    """
    # authentication_classes = (UserFirebaseAuthentication,)
    queryset = Project.objects.all().order_by("-created_at")
    serializer_class = ProjectSerializer
    tracker_id = Profilling().tracker_id

    @action(detail=False, methods=['get'])
    def another(self, request):
        project_count = Project.objects.count()

        return Response({'count': project_count})

    @action(detail=False, methods=['get'])
    def error(self, request):
        raise ProjectAPINotFoundError()


class ProjectAPIView(
    ListAPIView,
    RetrieveAPIView,
    GenericViewSet
):
    """
        Paginação nativa.
        Methodos Implementados apenas os selecionados
            - ListAPIView,
            - RetrieveAPIView,

    """
    # authentication_classes = (UserFirebaseAuthentication,)
    queryset = Project.objects.all().order_by("-created_at")
    serializer_class = ProjectSerializer
    tracker_id = Profilling().tracker_id

    @action(detail=False, methods=['get'])
    def another(self, request):
        project_count = Project.objects.count()

        return Response({'count': project_count})

    @action(detail=False, methods=['get'])
    def error(self, request):
        raise ProjectAPINotFoundError()


class ProjectViewSet(ViewSet):
    """
        Paginação não nativa.
        Methodos devem ser Implementados.
        https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions

    """
    # authentication_classes = (UserFirebaseAuthentication,)
    queryset = Project.objects.all().order_by("-created_at")
    serializer_class = ProjectSerializer
    tracker_id = Profilling().tracker_id

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(item)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def another(self, request):
        project_count = Project.objects.count()

        return Response({'count': project_count})

    @action(detail=False, methods=['get'])
    def error(self, request):
        raise ProjectAPINotFoundError()
