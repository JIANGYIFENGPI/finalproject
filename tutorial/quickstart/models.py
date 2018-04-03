# -*- coding: utf-8 -*-
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    courseid = models.IntegerField()
    cr = models.IntegerField()
    code = models.CharField(max_length=255)
    teacher = models.CharField(max_length=10)
    lan = models.CharField(max_length=255)
    numberofgroup = models.CharField(max_length=255)
    roomid =models.IntegerField()
    groupid = models.CharField(max_length=255)
    teachingyear= models.IntegerField()
    curriculumid = models.ForeignKey('Curriculum', models.DO_NOTHING, db_column='curriculumid')  # Field name made lowercase.
	

    class Meta:
        managed = False
        db_table = 'course'
		
		

class Curriculum(models.Model):
    numberofgroup= models.CharField(max_length=10)
    courseid = models.CharField(max_length=255)

	

    class Meta:
        managed = False
        db_table = 'curriculum'
		

class Group(models.Model):
	
    code = models.CharField(max_length=255)
    degreeprogram = models.CharField(max_length=255)
    implementid = models.ForeignKey('Implement', models.DO_NOTHING, db_column='implementid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'group'

		
class Implement(models.Model):
    p1 = models.IntegerField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
    p2 = models.IntegerField(db_column='P2', blank=True, null=True)  # Field name made lowercase.
    p3 = models.IntegerField(db_column='P3', blank=True, null=True)  # Field name made lowercase.
    p4 = models.IntegerField(db_column='P4', blank=True, null=True)  # Field name made lowercase.
    p5 = models.IntegerField(db_column='P5', blank=True, null=True)  # Field name made lowercase.
    period = models.IntegerField(db_column='period')
    startdate= models.CharField(max_length=255) # Field renamed to remove unsuitable characters.
    enddate= models.CharField(max_length=255)  # Field renamed to remove unsuitable characters.
    teacherid= models.IntegerField(db_column='teacherid', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    courseid = models.IntegerField(db_column='courseid', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'implement'




class Subgroup(models.Model):
    code = models.CharField(max_length=255)
    groupid = models.ForeignKey('Group', models.DO_NOTHING, db_column='groupid')
    
    class Meta:
        managed = False
        db_table = 'subgroup'
       



class Room(models.Model):
    roomseats = models.CharField(unique=True, max_length=255)
    topic = models.CharField(unique=True, max_length=255)
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'
		 


class Teacher(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'teacher'