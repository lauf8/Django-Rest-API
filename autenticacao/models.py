from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth.models import User

class User(User, TrackingModel):
    
    pass
