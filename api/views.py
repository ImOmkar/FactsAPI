import random
import requests
import re
from django.http import HttpResponse
from bs4 import BeautifulSoup
from .serializers import FactSerializer
from rest_framework.views import APIView
from .models import Facts
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class FactsView(APIView):
    
    def get(self, request):
        facts = list(Facts.objects.all())
        random_item = random.choice(facts)
        serialize = FactSerializer(random_item)  
        fact = serialize.data.get('fact')
        return Response(fact)
    
def delete_data(request):
    Facts.objects.all().delete()
    return HttpResponse('all removed')

def scrap(request):   
    pattern = re.compile(r'(\d+\)|\(Interesting facts in Marathi\))')
    URL = "https://www.talksmarathi.in/intresting-facts-in-marathi/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "lxml")
    p = soup.find_all("p", class_="")
    facts = p[1:188]
    for each in facts:
        cleaned_data = re.sub(pattern, '', each.get_text())
        Facts.objects.create(fact=cleaned_data.strip())
        print("entry added")
    return HttpResponse('test')
