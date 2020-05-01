from .models import ChatMessage

class ChatMessageRepository:

    @staticmethod
    def get_chat_messages():
        """
        Returns a list of chatmessage objects.
        """
        return ChatMessage.objects.all()


    @staticmethod
    def create_chat_message(user, content, time):
        """
        Creates a new chatmessage record.
        """
        ChatMessage.objects.create(user=user, content=content, created_at_format=time)