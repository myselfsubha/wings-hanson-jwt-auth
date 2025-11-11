from rest_framework import serializers
from .models import StreamPlatform, WatchList, Review

class ReviewSerializer(serializers.ModelSerializer):
    reviewed_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Review
        # fields='__all__'
        exclude = ['watchlist']

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model=WatchList        
        # fields=['id', 'title', 'storyline', 'platform', 'active']
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist= WatchListSerializer(many=True)
    
    class Meta:
        model=StreamPlatform
        fields=['id', 'name', 'about', 'website','watchlist']
    
