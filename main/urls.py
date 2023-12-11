from django.urls import path
from main.apps import MainConfig
from rest_framework.routers import DefaultRouter
from main.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentListAPIView, SubscriptionCreateAPIView, \
    SubscriptionDestroyAPIView, PaymentLessonCreateAPIView, PaymentCourseCreateAPIView


app_name = MainConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('subscribe/course/', SubscriptionCreateAPIView.as_view(), name='get-subscription'),
    path('subscribe/delete/<int:pk>', SubscriptionDestroyAPIView.as_view(), name='delete-subscription'),
    path('lesson/payment/<int:pk>/', PaymentLessonCreateAPIView.as_view(), name='payment_create'),
    path('course/payment/<int:pk>/', PaymentCourseCreateAPIView.as_view(), name='payment_create')
] + router.urls
