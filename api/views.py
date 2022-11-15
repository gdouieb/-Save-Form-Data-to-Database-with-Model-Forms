from rest_framework.response import Response
from rest_framework.decorators  import api_view
from base.models import Item
from .serializers import ItemSerializer
from django.shortcuts import render
from base.forms import UploadForm
from django.shortcuts import redirect
from django.http import HttpResponse
import collections

def home(request):
# listings/views.py
    _items = Item.objects.all().values
    return render(request, 'upload.html', {"items" : _items})



def upload(request):
    if request.POST:

        form = UploadForm(request.POST, request.FILES)
        print("reques file", request.FILES)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = UploadForm()
    return render(request,'home.html', {'form': form})
    
def getData(request):
    items = Item.objects.values()

    serializer = ItemSerializer(items, many = True)
    return Response(serializer.data)


def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
