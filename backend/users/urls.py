from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter
from knox import views as knox_views

from . import views
from .views import ( DoctorsAPIView,
                    PatientsAPIView,
                    UsersAPI,
                    LoginAPI,
                    SingleUserAPI, 
                    AppointmentsAPI,
                    AppointmentUpdateAPI,
                    AppointmentDeleteAPI,
                    ChatsAPI,
                    HealthRecordsAPI,
                    )

# router = DefaultRouter()
# router.register("", UserViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('users/', UsersAPI.as_view(), name='users'),
    path('users/doctors/', DoctorsAPIView.as_view(), name='doctors'),
    path('users/patients/', PatientsAPIView.as_view(), name='patients'),
    path('users/profile/', SingleUserAPI.as_view(), name='user'),
    path('users/appointments/', AppointmentsAPI.as_view(), name='appointments'),
    path('users/appointments/<int:pk>/', AppointmentUpdateAPI.as_view(), name='appointments'),
    path('users/appointments/<int:pk>/delete/', AppointmentDeleteAPI.as_view(), name='appointments'),
    path('users/records/', HealthRecordsAPI.as_view(), name='records'),
    path('users/chats/', ChatsAPI.as_view(), name='chats'),
    path('users/chats/messages/', ChatsAPI.as_view(), name='messages'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('users/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('users/', views.all_users),
    # path('users/<str:id>/', views.all_users),
    # path('users/uploads/', views.all_users),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += router.urls