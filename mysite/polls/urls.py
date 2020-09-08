from django.urls import path

from . import views

# Create an app_name to namespace our URLs in our templates.
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    # using angle brackets captures part of the URL and sends it as a keyworrd argument to the view function.
    # the <int: is a converter to determin what patterns should match.
    # the :question_id> defines the name that will be used to identify the matched pattern.
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]
