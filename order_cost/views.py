from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.views import APIView


from .order_handler import OrderHandler

# class to fetch the final value 

class GetOrderValue(APIView):

    def get(self, request, *args, **kwargs):

        handler = OrderHandler()
        response = handler.get_order_value(request.data)

        return JsonResponse(response, status=status_codes.HTTP_200_OK)
