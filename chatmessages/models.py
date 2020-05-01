from django.db import models

class ChatMessage(models.Model):
    # id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    created_at_format = models.CharField(max_length=20)
    content = models.CharField(max_length=255)
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        super(ChatMessage, self).save(*args, **kwargs)
        if ChatMessage.objects.all().count() > 10:
            ChatMessage.objects.order_by('created_at').first().delete()
