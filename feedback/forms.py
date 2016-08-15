from django.forms import ModelForm, TextInput, Textarea, EmailInput, FileInput


from .models import SubmitFeedback

class SubmitFeedbackForm(ModelForm):
    class Meta:
        model = SubmitFeedback
        fields = ["your_subject", "your_feedback", "your_name",
                 "your_email", "your_file",         
        ]
        
        labels = {
            "your_subject" : ("Subject"),
            "your_feedback": ("Feedback"),
            "your_name"    : ("Name"),
            "your_email"   : ("Email"),
            "your_file"    : ("File"),
        }
         
        widgets = {
            'your_subject': TextInput(attrs={
                'placeholder': 'Subject',
                'class': 'form-control',
            }),
            
            'your_feedback': Textarea(attrs={
                'placeholder': 'Feedback',
                'class': 'form-control',
            }),
            
            'your_name': TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-control',
            }),
            
            'your_email': EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control',
            }),   
        }
        

