from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('member/', views.member, name='member'),
    path('lending/', views.lending),
    path('add_book/', views.add_book),
    path('add_member/', views.add_member),
    # path('update_member/<int:mem_id>/', views.update_member),
    path('member/<int:mem_id>/', views.mem_infor),
    path('add_request/', views.add_request),
    path('add_lending/', views.add_lending),
    path('add_return/', views.return_book),
    path('add_librarian/', views.add_librarian),
    path('add_card/', views.add_card),
    path('delete_book/<int:id>', views.delete_book),
    path('delete_member/<int:id>', views.delete_member),
    path('accounts/', include('django.contrib.auth.urls')),
    path('compact_view/', views.compact_view),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)