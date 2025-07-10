from django import forms
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('message',)
        widgets = {
            'content': forms.Textarea(attrs={
                    'class':'w-full py-4 px-6 rounded-xl border'})
        }
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Type your message...'}),
        max_length=2000,
        label='Message'
    )