from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
 
    def validate_title(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Title 200 tadan kam bolishi kerak")
        return value

    def validate_description(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError("Description 1000 tadan kam bolishi kerak")
        return value