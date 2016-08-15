from django.conf.urls import url

from . import views

app_name = "feedback"
urlpatterns = [
    # ex: /submit_feedback/
    url(r"^submit_feedback/$", views.submit_feedback, 
       name="submit_feedback"),
    # ex: /view_feedback_list/
    url(r"^view_feedback_list/$", views.view_feedback_list, 
        name="view_feedback_list"),       
   # ex: /view_feedback/1/
    url(r"^view_feedback/(?P<feedback_id>[0-9]+)/$",
       views.view_feedback, name = "view_feedback"),
]    
