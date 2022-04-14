from django.shortcuts import render
from django.http import HttpResponse
from myApp.machinelearning import pipeline_model
from .forms import FaceRecognitionForm
from django.conf import settings
from myApp.models import FaceRecognition
import os

# Create your views here.
def home(request):
    form = FaceRecognitionForm()

    if request.method == 'POST':
        form = FaceRecognitionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            saved = form.save(commit=True)

            # Extract the image object from database
            imgobj = FaceRecognition.objects.get(pk=saved.pk)
            fileroot = str(imgobj.image)
            filepath = os.path.join(settings.MEDIA_ROOT, fileroot)
            result = pipeline_model(filepath)
            print(result)

            return render(request, "Index.html", {'form': form, 'upload': True, 'result': result})

    context = {
        'form': form,
        'upload': False,
    }
    return render(request, "Index.html", context)