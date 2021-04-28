from rest_framework import serializers

from socialapp.models import TripComment


class TripCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripComment
        fields = ["id", "author", "content", "added_at", "trip", "score"]


class TripCommentRetrieveSerializer(TripCommentSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = TripCommentSerializer.Meta.model
        fields = TripCommentSerializer.Meta.fields + ["photos"]

    # todo unify this method via mixin?
    def get_photos(self, obj):
        rq = self.context.get("request")
        return [
            {
                "id": photo.id,
                "thumb_url": rq.build_absolute_uri(photo.image_thumb.url),
                "url": rq.build_absolute_uri(photo.image.url),
                # todo maybe unify objects_with_lists_of_photos as well
            }
            for photo in obj.photos.all()
        ]
