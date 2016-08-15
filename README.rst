=========
Feedback
=========

Feedback is a simple django app for managing feedback submission and viewing. 

Quick start
-----------

1. Add "feedback" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'feedback',
    ]

2. Include the feedback URLconf in your project urls.py like this::

    url(r'^feedback/', include('feedback.urls')),

3. Run `python manage.py migrate` to create the feedback models.



