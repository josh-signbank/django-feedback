from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib import messages

from .forms import SubmitFeedbackForm
from .models import SubmitFeedback

def submit_feedback(request):
    # POST request -- save the submitted feedback if it's valid
    if request.method == "POST":
        form = SubmitFeedbackForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['your_email']:
                send_email(form.cleaned_data)
            messages.success(request, "Thank you for your feedback, %s."
                                %(form.cleaned_data["your_name"].split()[0]))                                    
            form = form.save(commit=False)
            form.date = timezone.now() 
            form.save()
            return HttpResponseRedirect(reverse('feedback:submit_feedback'))
                           
   # Any other kind of request -- create the empty feedback form        
    else:
        form = SubmitFeedbackForm()
   
    # Serve the empty feedback form to the user     
    return render(request, "feedback/submit_feedback.html", {"form": form})

def view_feedback_list(request):
    feedback = SubmitFeedback.objects.order_by('-date')
    
    return render(request, 'feedback/view_feedback_list.html', {'feedback': feedback})

def view_feedback(request, feedback_id):
    feedback = get_object_or_404(SubmitFeedback, pk=feedback_id)
    feedback.has_been_read = True
    feedback.save()
    
    return render(request, 'feedback/view_feedback.html', {'feedback': feedback})
    
        

def send_email(form_data):
    subject = 'Thank you for your feedback'
    message = '''Hi %s, 
Thank you for your feedback. We may
contact you for more information with regard to your feedback. 
For your convenience, we have reproduced your feedback below: 

%s'''%(form_data['your_name'], form_data['your_feedback'])
    sender = 'joshgoddard@gmail.com'
    receiver = (form_data['your_email'],)            
    send_mail(subject, message, sender, receiver)
        
