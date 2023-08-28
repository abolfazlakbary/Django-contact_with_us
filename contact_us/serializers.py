from rest_framework import serializers
from contact_us.models import Contact, Feedback

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'image', 'username', 'phone', 'email', 'password']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'contact', 'title', 'description']
