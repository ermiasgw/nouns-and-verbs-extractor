from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PdfSerializer, ExtractedDataSerializer
from .models import ExtractedData
from django.shortcuts import render


class UploadView(APIView):
    def post(self, request):
        serializer = PdfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()            
            return Response({'message': 'content extracted'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        extracted_data_instance = ExtractedDataSerializer(ExtractedData.objects.all(), many=True)
        return Response(extracted_data_instance.data, status=status.HTTP_200_OK)
    

def extractedDataView(request):
    return render(request, 'extracted_data.html')