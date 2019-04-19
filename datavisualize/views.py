from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from django.http import HttpResponse
from .models import DataSet
from matplotlib import pyplot as plt
import io

# Create your views here.
def index(request):
	return render(request,'data/data.html',{})

def get_data(request):
	data={
	"Name": 'Aakash Dhakal',
	"Campus":'Pulchowk Engineering Campus',
	"Age":22,
	"users":User.objects.all()
	}
	return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        datasets=DataSet.objects.all()
        labels=[]
        values=[]
        for x in datasets:
        	labels.append(x.label)
        	values.append(x.value)
        prevdata={
			"Name": 'Aakash Dhakal',
			"Campus":'Pulchowk Engineering Campus',
			"Age":22,
			"usercount":User.objects.all().count()
		}
        data={
            "labels": labels,
            "values": values,
        }
        usernames = [user.username for user in User.objects.all()]
        return Response(data)

def Ajax(request):
	return render(request,'data/ajax.html',{})

def Record(request):
	if request.method=='POST':
		DataSet.objects.create(user=User.objects.get(id=1),label=request.POST['label'],value=request.POST['value'])
	return render(request,'data/ajax.html',{})

def PyImage(request):
	x=[4,5,2]
	y=[5,9,8]
	buf=io.BytesIO()
	plt.plot(x,y)
	fig=plt.savefig(buf,format='png')
	#return render(request,'data/py.html',{'fig':buf.getvalue()})
	return HttpResponse(buf.getvalue(),content_type='image/png')

def FetchData(request):
	pass