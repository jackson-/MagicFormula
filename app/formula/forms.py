from django import forms
from django.forms import ModelForm
from formula.models import QueryHistory

class FormulaForm(ModelForm):
	class Meta:
		model = QueryHistory
		fields = ['symbols']
	