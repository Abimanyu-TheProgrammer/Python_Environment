from rest_framework import serializers
from test_app.models import Lead

#Lead SSerializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'