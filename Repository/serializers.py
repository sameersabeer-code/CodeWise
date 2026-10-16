from rest_framework import serializers
from Repository.models import QuestionDb

class QuestionSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=200)
    language=serializers.ChoiceField(choices=QuestionDb.LANGUAGE_CHOICES,default="python")
    Difficalty_level=serializers.ChoiceField(choices=QuestionDb.DIFFICULTY_CHOICES,default="easy")
    topic=serializers.CharField(max_length=100)
    note=serializers.CharField(max_length=100)
    published_date=serializers.DateTimeField(read_only=True)
    sample_input=serializers.CharField(max_length=100)
    sample_output=serializers.CharField(max_length=100)
    is_active=serializers.BooleanField(default=True)  
