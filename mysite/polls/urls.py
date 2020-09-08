from django.urls import path

from . import views

# Create an app_name to namespace our URLs in our templates.
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    # using angle brackets captures part of the URL and sends it as a
    # keyword argument to the view function.
    # the <int: is a converter to determin what patterns should match.
    # the :question_id> defines the name that will be used to identify the matched pattern.
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]
