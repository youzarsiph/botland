""" Serializers for botland.bots """

from rest_framework.serializers import ModelSerializer
from botland.bots.models import Bot


# Create your serializers here.
class BotSerializer(ModelSerializer):
    """Serialize bots"""

    class Meta:
        """Meta data"""

        model = Bot
        fields = (
            "id",
            "url",
            "name",
            "model",
            "description",
            "chat_count",
            "created_at",
            "updated_at",
        )
