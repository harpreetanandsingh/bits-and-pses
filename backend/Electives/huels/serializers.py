from rest_framework import serializers
from .models import Review
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["user","reviewed_course","sem","pr","experience","liteness","grade_sat","positives","negatives","tips"]
