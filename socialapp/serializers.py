from rest_framework import serializers

from socialapp.models import TripComment


class TripCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TripComment
        fields = ['id', 'author', 'content', 'added_at', 'trip', 'score']