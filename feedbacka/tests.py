import datetime

from django.test import TestCase, Client
from django.core import mail

from .models import SubmitFeedback


class SubmitFeedbackView(TestCase):
    def test_right_template_used_for_getting_feedback_form(self):
        '''
        'templates/submit_feedback.html' should be the template
         rendered for getting the feedback form.
        '''                
        response = self.client.get("/feedback/submit_feedback/")
        self.assertTemplateUsed(response, "feedback/submit_feedback.html")
        
    def test_right_template_used_for_submitting_feedback_form(self):
        '''
        'templates/submit_feedback.html' should be the template
         rendered for submitting the feedback form.
        '''
        post_data = {"your_name" : "fred", "your_feedback" : "a test",
                     "your_subject" : "test subject"}                
        response = self.client.post("/feedback/submit_feedback/", post_data, 
                                   follow = True)
        # A redirect occurs becore the template is rendered                           
        self.assertRedirects(response, '/feedback/submit_feedback/')                             
        self.assertTemplateUsed(response, "feedback/submit_feedback.html")
        
    def test_success_message_displayed_after_submitting_form(self):
        '''
        After submitting feedback, the user should be redirected
        to a page containing a success message.
        '''
        post_data = {"your_name" : "fred", "your_feedback" : "a test",
                    "your_subject" : "test subject"}                
        response = self.client.post("/feedback/submit_feedback/", post_data,
                                    follow = True) 
        self.assertContains(response, "Thank you for your feedback, fred")
            
    def test_required_fields_not_submitted(self):
        '''
        Required fields, if not submitted, should display errors
        on the form.
        '''
        post_data = {}                
        response = self.client.post("/feedback/submit_feedback/", post_data,
                                    follow = True) 
        self.assertFormError(response, "form", "your_name", 
                            "This field is required.")
        self.assertFormError(response, "form", "your_feedback", 
                            "This field is required.")
        
    def test_email_sent_if_email_provided(self):
        '''
        An email should be sent to the email address if it's provided
        '''
        post_data = {"your_name" : "fred", "your_feedback" : "a test",
                     "your_email" : "jared@gmail.com", 
                     "your_subject" : "test subject",}                
        response = self.client.post("/feedback/submit_feedback/", post_data,
                                    follow = True)                               
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('fred', mail.outbox[0].body)
       
       
class SubmitFeedbackModel(TestCase):
    '''
    The tests defined in here test for the correctness
    of the data in the database.
    '''
    
    def test_name_and_feedback_in_database_after_being_submitted(self):
        '''
        The name and feedback should be put into the database if they are 
        submitted. 
        '''   
        post_data = {"your_name" : "fred", "your_feedback" : "a test",
                    "your_subject" : "test subject"}                
        response = self.client.post("/feedback/submit_feedback/", post_data,
                                    follow = True)
                                    
        # Now let's make sure that the name and feedback are in the database                                                           
        submissions = SubmitFeedback.objects.all()
        # There should be one submission in the datbase
        self.assertEqual(1, len(submissions))
        # It should have a name
        self.assertEqual(submissions[0].your_name, "fred")
        # It should have feedback
        self.assertEqual(submissions[0].your_feedback, "a test")
        # It should have a date 
        self.assertIsInstance(submissions[0].date, datetime.datetime)
        
        

        
   
                               
        
       
