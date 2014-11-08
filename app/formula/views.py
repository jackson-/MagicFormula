from django.shortcuts import render
from django.views.generic import View
from bs4 import BeautifulSoup as bs4
import requests as r
from formula.forms import FormulaForm
from django.http import HttpResponse, JsonResponse

# Create your views here.
class IndexView(View):
	template_name = 'index.html'
	form_class = FormulaForm

	def get(self, request):
		
		return render(request, self.template_name, {'form':self.form_class})

class MagicView(View):

	def post(self, request):
		print(request.POST)
		symbols = request.POST['symbols'].split(',')
		for value in range(len(symbols)):
			symbols[value] = symbols[value].strip()
		roc = []
		for value in symbols:
			url = r.get("http://www.gurufocus.com/term/ROC_JOEL/" + value + "/Return%252Bon%252BCapital%252B%252B-%252BJoel%252BGreenblatt/")
			soup = bs4(url.text)
			for div in soup.select('.data_value'):
				roc.append(div.get_text())
		print(self.output)
		return HttpResponse('test')