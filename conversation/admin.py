from django.contrib import admin

from .models import Conversation, ConversationMessage

admin.site.register(ConversationMessage)
admin.site.register(Conversation)