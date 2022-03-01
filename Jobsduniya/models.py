from django.db import models

# Create your models here.
INDUSTRY = (
        ('Printing','Printing'),
        ('Digital', 'Digital'),
        ('Flexo', 'Flexo'),
        ('Offset', 'Offset'),
        ('Rotogravure', 'Rotogravure'),
        ('Screen', 'Screen'),
        ('Packaging','Packaging'),
        ('Flexible', 'Flexible'),
        ('Rigid', 'Rigid'),
        ('Publishing','Publishing'),
        ('Books', 'Books'),
        ('Magazines', 'Magazines'),
        ('Newspaper', 'Newspaper'),
        ('Online', 'Online'),
        ('Substrater-Paper&film','Substrater-Paper&film'),
        ('Film', 'Film'),
        ('Paper', 'Paper'),
        ('Board', 'Board'),
        ('Others', 'Others'),
        ('Chemicals','Chemicals'),
        ('Adhesives', 'Adhesives'),
        ('Coatings', 'Coatings'),
        ('Printing Inks', 'Printing Inks'),
        ('Others', 'Others'),
        
)

JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelancer'),
)


class Vacancy(models.Model):

    jobid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    industryy = models.CharField(choices=INDUSTRY, max_length=30)
    Designation = models.CharField(max_length=30)
    Responsibility = models.CharField(max_length=200)
    Experience = models.CharField(max_length=30)
    Education_Qualification = models.CharField(max_length=100)
    Employer_name = models.CharField(max_length=30)
    Employer_phone = models.CharField(max_length=90)
    Employer_email = models.EmailField(max_length=90)
    Employer_website = models.CharField(max_length=90)
    Ctc = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=20)
    JobType = models.CharField(choices=JOB_TYPE, max_length=10)
    apply_link = models.URLField(max_length=200)
    post_or_not = models.BooleanField(default=False)

    def __str__(self):
        return(self.title)


class Contact(models.Model):
    msg_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100, default = '')
    phone = models.CharField(max_length = 20, default = '')
    desc = models.CharField(max_length = 200, default = '')

    def __str__(self):
        return self.name

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    fb_text = models.CharField(max_length=500)

    def __str__(self):
        return self.name