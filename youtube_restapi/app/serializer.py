from rest_framework import serializers
from app.models import Videos


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = (
            "id",
            "title",
            "desc",
            "publishing_date",
            "url_for_thumnail",
            "link",
        )
