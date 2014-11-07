from django.shortcuts import render
from django.views.generic import View
from bs4 import BeautifulSoup as bs4
import requests as r


# Create your views here.
class IndexView(View):
	template_name = 'index.html'

	def get(self, request):
		url = r.get("http://www.gurufocus.com/term/ROC_JOEL/GOOG/Return%252Bon%252BCapital%252B%252B-%252BJoel%252BGreenblatt/Google%2BInc")
		soup = bs4(url.text)
		self.output = []
		for div in soup.select('.data_value'):
			self.output.append(div.get_text())
		print(self.output)
		return render(request, self.template_name, {'output':self.output})