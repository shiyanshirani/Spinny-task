# Project imports
from boxes.models import Box
from boxes.checks import validation
from boxes.filters import BoxFilter
from boxes.serializers import BoxSerializer, BoxUpdateSerializer

# DRF imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Create your views here.


class BoxListAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        boxes = Box.objects.all()
        boxes_filtered = BoxFilter(request.GET, queryset=boxes).qs
        serializer = BoxSerializer(boxes_filtered, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BoxAddAPI(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        box = Box(created_by=request.user)
        serializer = BoxSerializer(box, data=request.data, partial=True)
        if serializer.is_valid() and validation(request.user):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class BoxDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        box = Box.objects.filter(created_by=user)
        serializer = BoxSerializer(box, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = request.user
        box = Box.objects.get(pk=pk)
        if user == box.created_by:
            box.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk):
        box = Box.objects.get(pk=pk)
        serializer = BoxUpdateSerializer(box, data=request.data)
        if serializer.is_valid() and validation(request.user):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BoxDeleteAPI(APIView):
#     permission_classes = [IsAuthenticated]

#     def delete(self, request, pk):
#         user = request.user
#         box = Box.objects.get(pk=pk)
#         if user == box.created_by:
#             box.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

#         return Response(status=status.HTTP_401_UNAUTHORIZED)


# class BoxUpdateAI(APIView):
#     permission_classes = [IsAdminUser]

#     def put(self, request, pk):
#         box = Box.objects.get(pk=pk)
#         serializer = BoxUpdateSerializer(box, data=request.data)
#         if serializer.is_valid() and validation(request.user):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
