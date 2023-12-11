from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics

from main.models import Course, Lesson, Payment, Subscription
from main.paginators import CoursePaginator, LessonPaginator
from main.permissions import IsModerator, IsOwner, IsSubscriber
from main.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_permissions(self):
        if self.action == 'update' or self.action == 'partial_update' or self.action == 'retrieve':
            permission_classes = [IsModerator | IsOwner]
        elif self.action == 'delete':
            permission_classes = [~IsModerator]
        elif self.action == 'create':
            permission_classes = [~IsModerator]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [~IsModerator]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method')
    ordering_fields = ('payment_date',)


class PaymentLessonCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer, **kwargs):

        new_payment = serializer.save()
        new_payment.user = self.request.user
        new_payment.lesson = Lesson.objects.get(id=self.kwargs['pk'])
        new_payment.save()
        new_payment.payment_amount = Lesson.objects.get(id=self.kwargs['pk']).price
        new_payment.save()


class PaymentCourseCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer, **kwargs):

        new_payment = serializer.save()
        new_payment.user = self.request.user
        new_payment.course = Course.objects.get(id=self.kwargs['pk'])
        new_payment.payment_amount = Course.objects.get(id=self.kwargs['pk']).price
        new_payment.save()


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer, **kwargs):
        new_subscription = serializer.save()
        new_subscription.user = self.request.user
        new_subscription.save()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    permission_classes = [IsSubscriber]
