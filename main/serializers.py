from rest_framework import serializers
from main.models import Course, Lesson, Payment, Subscription
from main.validators import YoutubeValidator
from rest_framework.fields import SerializerMethodField
from main.management.utils import get_stripe_link


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YoutubeValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.IntegerField(source='lesson_set.all.count', read_only=True)
    lessons = LessonSerializer(source='lesson_set', many=True)

    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user, course=obj).exists()


class PaymentSerializer(serializers.ModelSerializer):
    payment_link = SerializerMethodField()  # Ссылка на оплату

    def get_payment_link(self, payment):
        """Метод для получения ссылки на оплату"""
        payment_link = get_stripe_link(payment)

        return payment_link

    class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'