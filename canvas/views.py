from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Canvas
from django.forms import ModelForm
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'canvas/index.html')

def canvas(request, name):
    return render(request, 'canvas/canvas.html',{'name':name})


def update(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST request required."}, status=400)

    data = json.loads(request.body)
    canvasName = data.get("canvasName","")
    canvas = Canvas.objects.get(name=canvasName).getUpdate()

    return JsonResponse(canvas)


def change(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST request required."}, status=400)
        
    data = json.loads(request.body)
    canvasName = data.get("canvasName","")
    sqId = data.get("sqId","")
    value = data.get("value","")

    canvas = Canvas.objects.get(name=canvasName)

    setattr(canvas, sqId, value)
    canvas.save()

    return JsonResponse({"message": "done"}, status=200)


class Create(ModelForm):
    class Meta:
        model = Canvas
        fields = ['name']

def create(request):
    form = Create()
    if request.method == "POST":
        form = Create(request.POST)
        if form.is_valid():
            canvasName = form.cleaned_data['name']
            canvasName = f"{canvasName}{Canvas.objects.all().count()}"

            exist = Canvas.objects.filter(name=canvasName).count()

            while exist != 0:
                canvasName = f"{canvasName}{Canvas.objects.all().count()}"
                exist = Canvas.objects.filter(name=canvasName).count()

            createIt = Canvas(name=canvasName)
            createIt.save()

            return redirect("canvas", name=canvasName)


    return render(request, 'canvas/new.html',{'form':form})

def search(request):
    if request.method =="GET":
        return render(request, 'canvas/search.html')

    if request.method == "POST":
        query1 = request.POST.get('query1','')

        if query1 != "":
            rows = Canvas.objects.filter(name__icontains=query1)

            return render(request, 'canvas/search.html',{"rows":rows,"query1":query1})
        else: 
            return render(request, 'canvas/search.html')
