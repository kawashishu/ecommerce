
from requests import Response
from ..models import Customer

from django.shortcuts import redirect, render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from ..serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # check if user is authenticated ==> display info
    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]

    # create duoc 5 cai ham API
    # list: lay toan bo danh sach ( GET )
    # create: Them ( POST )
    # retrieve : lay 1 doi tuong ( GET )
    # update : cap nhat ( PUT )
    # destroy: xoa ( DELETE )

    @action(methods=['POST'], detail=True, url_path = 'un_active', url_name='un_active')
    # /customer/{pk}/{url_path}
    def un_active(self, request, pk):
        try:
            # import pdb; pdb.set_trace();
            customer = Customer.objects.get(id=pk)
            customer.is_active = False
            customer.save()
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=CustomerSerializer(customer).data, 
                        status=status.HTTP_200_OK)
    
    @action(methods=['POST'], detail=True, url_path = 'active', url_name='active')
    # /customer/{pk}/{url_path}
    def active(self, request, pk):
        try:
            # import pdb; pdb.set_trace();
            customer = Customer.objects.get(id=pk)
            customer.is_active = True
            customer.save()
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=CustomerSerializer(customer).data, 
                        status=status.HTTP_200_OK)

