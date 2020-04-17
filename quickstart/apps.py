from django.apps import AppConfig

import joblib 
from django.conf import settings
import os
from tensorflow.keras.models import load_model

class QuickstartConfig(AppConfig):
    name = 'quickstart'
class Predictator(AppConfig):
  
    model_name='malaria_detector.h5'

    
    model_path = os.path.join(settings.MODEL_ROOT, model_name)
    
    model=load_model(model_path)


