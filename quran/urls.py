    from django.urls import path
    from .views import VerseList

    urlpatterns = [
        path('verses/', VerseList.as_view(), name='verse-list'),
    ]
    