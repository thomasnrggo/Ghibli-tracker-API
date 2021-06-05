from rest_framework import serializers
from .models import Ratings


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.emoji_rating = validated_data.get('emoji_rating', instance.emoji_rating)
        instance.star_rating = validated_data.get('star_rating', instance.star_rating)
        instance.watched = validated_data.get('watched', instance.watched)
        instance.user = validated_data.get('user', instance.user)
        instance.movie = validated_data.get('movie', instance.movie)
        instance.save()
        return instance