from django.shortcuts import render
#from . forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import satellite
from . serializers import satelliteSerializers
import pickle
#from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
import joblib


class SatelliteView(viewsets.ModelViewSet):
	queryset = satellite.objects.all()
	serializer_class = satelliteSerializers
		
@api_view(["POST"])
def approvereject(request):
	try:
		mdl=joblib.load("model_light.pkl")
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		mydata=request.data
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)

		
		y_pred=mdl.predict(unit)
		y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		#newdf=newdf.replace({True:'Approved', False:'Rejected'})
		return JsonResponse('Your Status is {}'.format(newdf), safe=False)

	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)