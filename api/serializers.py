from rest_framework import serializers
from .models import *

class WebinarSerializers(serializers.ModelSerializer):
    class Meta:
        model=WebinarContact
        fields='__all__'

class FeedBack1Serializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback1
        fields='__all__'

class FeedBack2Serializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBack2
        fields='__all__'
