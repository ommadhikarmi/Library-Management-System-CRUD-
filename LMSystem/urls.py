
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from.views import CategoryView
from.views import AuthorsView
from.views import BookView
from.views import BookFileView
from.views import BookFileViewDetail

urlpatterns = [
    path('category/',CategoryView.as_view({'get':'list','post':'create'})),
    path('category/<int:pk>/',CategoryView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('authors/',AuthorsView.as_view({'get':'list','post':'create'})),
    path('authors/<int:pk>/',AuthorsView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('book/',BookView.as_view({'get':'list','post':'create'})),
    path('book/<int:pk>/',BookView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('bookfile/',BookFileView.as_view()),
    path('bookfile/<int:pk>/',BookFileViewDetail.as_view(),name='bookfile-detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)