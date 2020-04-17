
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tensorflow.keras.preprocessing import image
from django.shortcuts import render
from .apps import Predictator
import numpy as np
from rest_framework.parsers import MultiPartParser
# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views


# Create your views here.
class predict(views.APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        im= request.data['file']
        if im:
            image_shape = (130,130,3)
            my_image = image.load_img(im,target_size=image_shape)
            my_image = image.img_to_array(my_image)
            my_image = np.expand_dims(my_image, axis=0)
            res=Predictator.model.predict(my_image)
            return Response(int(res[0]),status=200)
        
        else:
            return Response({"message":"file is not recieved"},status=400)


