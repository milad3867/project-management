from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_id = models.CharField(unique=True, max_length=256)
    phone_number = models.IntegerField(unique=True)

    def __str__(self):
        return (self.user.first_name + ' ' +  # pylint: disable=no-member
                self.user.last_name)  # pylint: disable=no-member


class Semester(models.Model):
    name = models.CharField(unique=True, max_length=256, blank=False)
    created_date = models.DateTimeField('date created', default=timezone.now)
    active = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return (self.name)

    def is_semester_active(self):
        return (self.is_active)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id_number = models.IntegerField(unique=True)
    phone_number = models.IntegerField(unique=True)
    research_subject = models.CharField(max_length=256, blank=True)
    pdf = models.FileField(upload_to='doc1', blank=True)
    doc = models.FileField(upload_to='doc2', blank=True)

    semester = models.ForeignKey(Semester, related_name='students',
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)

    guid_instructor = models.ForeignKey(Professor,
                                        related_name='students',
                                        on_delete=models.SET_NULL,
                                        blank=True, null=True)

    def __str__(self):
        return (self.user.first_name + ' ' +  # pylint: disable=no-member
                self.user.last_name)  # pylint: disable=no-member

    def get_absolute_url(self):
        return reverse('fileManagement:upload', kwargs={'pk': self.pk})


class Industry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(unique=True)
    company_name = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return (self.user.first_name + ' '  # pylint: disable=no-member
                + self.user.last_name)  # pylint: disable=no-member


class Grade(models.Model):
    GRADE_TYPE_CHOICES = [
        ('by student', 'by student'),
        ('by professor', 'by professor'),
        ('by industry', 'by industry'),
    ]
    value = models.FloatField(blank=False)

    grade_type = models.CharField(
        max_length=256, choices=GRADE_TYPE_CHOICES, blank=False)

    given_by = models.ForeignKey(
        User, related_name='grades_given',
        on_delete=models.CASCADE, blank=False)

    given_to = models.ForeignKey(
        User, related_name='grades', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return ('grade from ' +
                self.given_by.first_name + ' ' + self.given_by.last_name +
                ' to ' +
                self.given_to.first_name + ' ' + self.given_to.last_name)
