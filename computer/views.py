from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict

from .models import ComputerModel


class ComputerListCreateView(APIView):
    def get(self, *args, **kwargs):
        computer = ComputerModel.objects.all().values()
        return Response(computer, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data.dict()
        computer = ComputerModel.objects.create(**data)
        return Response(model_to_dict(computer), status.HTTP_201_CREATED)


class ComputerRetrieveUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with this id is not exist', status.HTTP_404_NOT_FOUND)
        computer = ComputerModel.objects.get(pk=pk)
        return Response(model_to_dict(computer), status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with this id is not exist', status.HTTP_404_NOT_FOUND)
        data = self.request.data.dict()
        ComputerModel.objects.filter(pk=pk).update(**data)
        return Response('updated', status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with this id is not exist', status.HTTP_404_NOT_FOUND)
        car = ComputerModel.objects.get(pk=pk)
        car.delete()
        return Response(status.HTTP_204_NO_CONTENT)

# Create
# Retrieve
# Update
# Delete