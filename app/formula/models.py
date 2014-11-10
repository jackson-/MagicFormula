from django.db import models

# Create your models here.

class Symbols(models.Model):
	ticker = models.CharField(max_length=300)

class Entry(models.Model):
	id = models.AutoField(primary_key=True)

class History(models.Model):
	sym_id = models.ForeignKey(Symbols)
	entry_id = models.ForeignKey(Entry)
	magic_number = models.IntegerField(max_length=50)
	market_cap = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
