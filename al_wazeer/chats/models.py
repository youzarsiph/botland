""" Data Models for al_wazeer.chats """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Chat(models.Model):
    """AlWazeer Chats"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="chats",
        help_text="User",
    )
    assistant = models.ForeignKey(
        "assistants.Assistant",
        on_delete=models.CASCADE,
        related_name="chats",
        help_text="Assistant (Chat LLM)",
    )
    title = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Chat title",
    )
    is_pinned = models.BooleanField(
        default=False,
        help_text="Designates if the chat is pinned",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    @property
    def message_count(self) -> int:
        """Number of a messages of a chat"""

        return self.messages.count()

    @property
    def unread_message_count(self) -> int:
        """Number of a unread messages of a chat"""

        return self.messages.filter(is_read=False).count()

    def __str__(self) -> str:
        return f"{self.user}-{self.assistant}: {self.title}"
