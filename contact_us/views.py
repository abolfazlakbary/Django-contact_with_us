from django.shortcuts import render
from rest_framework import generics

import contact_us.permissions
from contact_us.models import Contact, Feedback
from contact_us.serializers import ContactSerializer, FeedbackSerializer
from rest_framework import permissions
class FeedbackCreate(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

class FeedbackRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated,
                          contact_us.permissions.IsObjectOwner,]

class FeedbackList(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAdminUser]

class SelectedFeedback(generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAdminUser]