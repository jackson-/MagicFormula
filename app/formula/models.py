from django.db import models

# Create your models here.
class QueryHistory(models.Model):
	symbols = models.CharField(max_length=300)
	created_at = models.DateTimeField(auto_now_add=True)