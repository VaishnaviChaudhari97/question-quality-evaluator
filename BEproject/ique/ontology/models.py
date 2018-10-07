from django.db import models

class Document(models.Model):
    course = models.CharField(max_length=50)
    owl = models.FileField(upload_to='files/owl')
    los = models.FileField(upload_to='files/los')
    ai = models.FileField(upload_to='files/ai')

    def __str__(self):
        return self.course
