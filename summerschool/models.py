from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

SCHOOL_LEVELS = (
    ("GradeSchool", "GradeSchool"),
    ("PreSchool", "PreSchool"),
    ("Kindergarten", "Kindergarten")
)

GRADE_LEVEL = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ('7', '7'),
    ("8", "8"),
)


class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    fullname = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to="kids_grade_school_photos", blank=True, default="kid.jpg")
    contact_number = models.CharField(max_length=30, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail = output_size
            img.save(self.photo.path)


class Student(models.Model):
    student_email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_email


class SchoolKid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    school = models.CharField(choices=SCHOOL_LEVELS, max_length=20)
    grade = models.CharField(choices=GRADE_LEVEL, max_length=10, blank=True, help_text="Use this field only if child's school is GradeSchool")
    photo = models.ImageField(upload_to="kids_photos", blank=True, default="kid.jpg")
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} added a new kid"

    def get_absolute_kid(self):
        return reverse("kids_detail",args={self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail = output_size
            img.save(self.photo.path)


class SchoolLoginCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} logged in at {self.date_logged}"