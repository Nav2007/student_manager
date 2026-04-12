from django.db import models
from django.core.exceptions import ValidationError#for semester limits
class Enrollment(models.Model):
    COURSE_CHOICES = (
        ('bca', 'BCA'),
        ('btech', 'B.Tech'),
        ('mca', 'MCA'),
    )
    SEMESTER_LIMITS = {
    'bca': 6,
    'btech': 8,
    'mca': 4,
    }
    name = models.CharField(max_length=20, choices=COURSE_CHOICES)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    semester = models.IntegerField()
    def clean(self):
        max_sem = self.SEMESTER_LIMITS.get(self.name)

        if max_sem is not None:
            if self.semester < 1 or self.semester > max_sem:
                raise ValidationError(
                    f"{self.get_name_display()} has only {max_sem} semesters."#get variable display is created automatically in python method that displays its value
                )
    def save(self, *args, **kwargs):#override save method here , then call the parent/super class method to save the changes to database
        self.clean()#args kwargs forward everything to original save
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.student} - {self.name} (Sem {self.semester})"

