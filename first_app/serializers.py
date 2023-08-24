from rest_framework import serializers
from .import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'

class StudentSerilizers(serializers.ModelSerializer):
    # course = CourseSerializer(many=True, read_only=True)
    # course = serializers.StringRelatedField(many=True)
    # course = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    course = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='course_details'
    )
    class Meta:
        model = models.StudentData
        fields = '__all__'