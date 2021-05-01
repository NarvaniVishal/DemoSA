from django.shortcuts import render

from app1.models import Student
from app1.models import Course
# Create your views here.
from django.http import JsonResponse

def loginAction(request):
	return render(request,"menu_v1.html")

def home(request):
	# data = [{'name': 'Peter', 'email': 'peter@example.org'},
            # {'name': 'Julia', 'email': 'julia@example.org'}]
	stuData=Student.objects.all()

	lst=[]

	for s in stuData:
		lst.append(s.name)
	return JsonResponse(lst, safe=False)
	# lst=Student.objects.all()
	# dictData={"data":lst}
	# print(dictData)
	# return render(request,"menu_v1.html",dictData)


def index(request):
	lst=Course.objects.all()
	dictData={"data":lst}
	return render(request,"form.html")