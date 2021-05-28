from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
# Create your views here.
df3=pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')

def index(request):
    #contryNames = ["Francistown","Gaborone ","Kanye","Kasane","Tsabong","Serowe"]
       
    pedestrianData=pd.read_csv("firstUI/RegionData.csv")
    ciityName=request.POST.get('ciityName')
    head = pedestrianData.head()
    cityName = list(head.City)

    context={"ciityName":ciityName,"cityName":cityName}

    return render(request,'index.html',context)
    
def drillDownACountry(request):
    ciityName=request.POST.get('ciityName')
    pedestrianData=pd.read_csv("firstUI/RegionData.csv")
    head = pedestrianData.head()
    cityName = list(head.City)

    pedestrianData.set_index("City", inplace = True)
    pdata = pedestrianData.loc[ciityName]
    print(pdata)
    print(cityName)
    context={"ciityName":ciityName,"cityName":cityName,"pdata":list(pdata)}

    return render(request,'index2.html',context)

