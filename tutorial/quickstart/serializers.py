from django.contrib.auth.models import User
from models import  Course, Curriculum, Group, Implement, Subgroup, Room, Teacher
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'id','name', 'courseid','cr', 'code', 'teacher','lan','numberofgroup','roomid','groupid','teachingyear','curriculumid')
		
class CurriculumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('url', 'id','numberofgroup','courseid')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','id','code', 'degreeprogram','implementid')
		
class ImplementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Implement
        fields = ('url', 'id','p1','p2','p3','p4','p5','period','startdate','enddate','teacherid','courseid')
		
class SubgroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subgroup
        fields = ('url', 'id','code')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'id', 'roomseats', 'topic','courseid')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url','id','code','name')