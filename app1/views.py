from django.shortcuts import render
from django.http import HttpResponse


#simple request
'''
from django.http import HttpResponse
def page1(request):
	return HttpResponse("Hello World")
'''

#template request tip 1
'''
from django.template import loader
def page2(request):
	template=loader.get_template('index1.html')
	return  HttpResponse(template.render())
'''

# the simple template request tip 2
'''
from django.shortcuts import render
def page3(request):
	return render(request,'index1.html',{'page3':page3})
'''