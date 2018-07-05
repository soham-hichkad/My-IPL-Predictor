	
#importing required packages
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import dm_decisiontree
from . import dm_navierbayes
from . import dm_kmeans
from pandas import *
 
#disabling csrf (cross site request forgery)
@csrf_exempt
def decision(request):
    #if post request came 
    if request.method == 'POST':
        #getting values from post
        over = request.POST.get('over')
        ball = request.POST.get('ball')
        strike = request.POST.get('strike')
        name = request.POST.get('name')
        #adding the values in a context variable 
        context = {
            'over': over,
            'ball': ball,
            'strike': strike,
            'name': name 
        }
        
        ans = dm_decisiontree.Dmmain(context)

        ans1 = {
        	'pred' : ans
        }
        #getting our showdata template
        template = loader.get_template('home.html')
        
        #returing the template 
        return HttpResponse(template.render(ans1, request))
    else:
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('home.html')
        return HttpResponse(template.render())

@csrf_exempt
def navie(request):
    #if post request came 
    if request.method == 'POST':
        #getting values from post
        team1 = request.POST.get('team1')
        team2 = request.POST.get('team2')
        venue = request.POST.get('venue')
        #adding the values in a context variable 
        context = {
            'team1': team1,
            'team2': team2,
            'venue': venue,
        }
        
        ans = dm_navierbayes.Nbmain(context)

        ans1 = {
            'pred1' : ans
        }
        #getting our showdata template
        template = loader.get_template('home.html')
        
        #returing the template 
        return HttpResponse(template.render(ans1, request))
    else:
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('home.html')
        return HttpResponse(template.render())

@csrf_exempt
def kmean(request):
    #if post request came 
    if request.method == 'POST':
        #getting values from post
        player = request.POST.get('player')
        #adding the values in a context variable 
        context = {
            'player': player,
        }
        
        ans = dm_kmeans.Kmain(context)

        print(ans)
        
        ans1 = {
            'pred2' : ans
        }
        #getting our showdata template
        template = loader.get_template('home.html')
        
        #returing the template 
        return HttpResponse(template.render(ans1, request))
    else:
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('home.html')
        return HttpResponse(template.render())



