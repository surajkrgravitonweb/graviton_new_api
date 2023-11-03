from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
# Create your views here.


class WebinarViewList(generics.ListCreateAPIView):
    queryset=WebinarContact.objects.all()
    serializer_class=WebinarSerializers
    permission_classes = [IsAuthenticated]


class WebinarDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=WebinarContact.objects.all()
    serializer_class=WebinarSerializers
    permission_classes = [IsAuthenticated]


class FeedBack2List(generics.ListCreateAPIView):
    queryset=FeedBack2.objects.all()
    serializer_class=FeedBack2Serializer
    permission_classes = [IsAuthenticated]

    

class FeedBack2Details(generics.RetrieveUpdateDestroyAPIView):
    queryset=FeedBack2.objects.all()
    serializer_class=FeedBack2Serializer
    permission_classes = [IsAuthenticated]


class Feedback1List(generics.ListCreateAPIView):
    queryset=Feedback1.objects.all()
    serializer_class=FeedBack1Serializer
    permission_classes = [IsAuthenticated]


class Feedback1Details(generics.RetrieveUpdateDestroyAPIView):
    queryset=Feedback1.objects.all()
    serializer_class=FeedBack1Serializer
    permission_classes = [IsAuthenticated]
    

