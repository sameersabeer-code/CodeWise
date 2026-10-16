from django.db import models

# Create your models here.
"""

Schema   :QuestionsDb
Fields   :title,language,notes,difficulty_level,sample_input,sample_output,
          topic,published_date,is_active
"""

class QuestionDb(models.Model):
    title=models.CharField(max_length=100)
    LANGUAGE_CHOICES=(
        ("python","Python"),("java","Java"),("c++","c++"),("javascript","javascript")
    )
    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default="pyton")
    DIFFICULTY_CHOICES=(
        ("easy","easy"),("hard","hard"),("veryhard","veryhard")
    )
    Difficalty_level=models.CharField(max_length=100,choices=DIFFICULTY_CHOICES,default="easy")
    topic=models.CharField(max_length=100)
    published_date=models.DateTimeField(auto_now_add=True)
    note=models.TextField()
    sample_input=models.TextField()
    sample_output=models.TextField()
    is_active=models.BooleanField(default=True)