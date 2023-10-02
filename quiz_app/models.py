from django.db import models
import uuid
import random
# Create your models here.


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):    
    category_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.category_name

class Quiz_Question(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question
    

    def get_answer(self):
        answer_objs = list(Quiz_Answer.objects.filter(question=self))
        random.shuffle(answer_objs)
        data = []
        for answerob in answer_objs:
            data.append({
                'answer': answerob.answer,
                'is_correct' : answerob.is_correct
            })

        return data
    

class Quiz_Answer(BaseModel):
    question = models.ForeignKey(Quiz_Question, on_delete=models.CASCADE, related_name='question_answer')
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.answer

