from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
# from django.forms.models import model_to_dict

@csrf_exempt
@api_view(['GET', 'POST'])

def getBlogInfo(request):
    projects = Project.objects.all().order_by('-created_on')
    tmpJson = serializers.serialize("json",projects)
    tmpObj = json.loads(tmpJson)

    return HttpResponse(json.dumps(tmpObj))
    # return JsonResponse( model_to_dict(projects) )
    
    # return JsonResponse(projects, safe=False)
    
    # context = {
    #     "posts": projects,
    # }
    # return Response(context)
@csrf_exempt
@api_view(['GET'])
def getProjectDetail(request, pk):
    project = Project.objects.get(pk=pk)
    obj = Project.objects.filter(pk=pk)
    datalist = list(obj.values())
    # datalist[0]["status"] = 200
    return JsonResponse(datalist, safe=False)

@csrf_exempt
@api_view(['POST'])
def fetchProjectDetail(request):
    pk = request.data["pk"]
    if Project.objects.filter(pk=pk).exists():
        obj = Project.objects.filter(pk=pk)
        datalist = list(obj.values())
        datalist[0]["status"] = 200
        return JsonResponse(datalist, safe=False)
    else:
        response = {
            "message": "User not found!", 'status': 404}
        return Response(response)
