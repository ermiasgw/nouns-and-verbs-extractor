from rest_framework import serializers
from .models import ExtractedData
from .utils import extract_nouns_verbs_from_text
import PyPDF2


class PdfSerializer(serializers.Serializer):
    email = serializers.EmailField()
    file = serializers.FileField()

    def validate_email(self, value):
        if ExtractedData.objects.filter(email=value):
            raise serializers.ValidationError("This email address is already in use.")
        return value
    
    def save(self):
        text = ""
        email = self.validated_data['email']
        file = self.validated_data['file']
        
        # extract text from pdf
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

        nouns, verbs = extract_nouns_verbs_from_text(text)

        # save to the database
        try:
            return ExtractedData.objects.create(email=email, nouns=nouns, verbs=verbs)
        except Exception as e:
            raise serializers.ValidationError(f"An error occurred while creating the object: {str(e)}")
        
class CustomField(serializers.Field):
    def to_representation(self, value):
        return list(value)
        
class ExtractedDataSerializer(serializers.ModelSerializer):
    nouns = CustomField()
    verbs = CustomField()
    class Meta:
        model = ExtractedData
        fields = ['id', 'email', 'nouns', 'verbs']