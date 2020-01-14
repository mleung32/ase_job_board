from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

# Create your models here.

class Posting(models.Model): 
    """An ASE job posting."""

    #CHOICE VARIABLES

    #semester
    FALL_2019 = "Fall 2019"
    SPRING_2020 = "Spring 2020"

    #positions
    GSI = "GSI"
    HEAD_GSI = "Head GSI"
    GSR = "GSR"
    TUTOR = "Tutor"
    READER = "Reader"
    COURSE_ASST = "Course Asst"

    #school
    INFORMATION = "Information"
    ECONOMICS = "Economics"
    COG_SCI = "Cognitive Science"
    SOCIOLOGY = "Sociology"
    ENV_SCI_MGMT = "Environmental, Science, Policy, and Management"

    #CHOICE FIELDS
    semester_choices = (
        (FALL_2019, "Fall 2019"),
        (SPRING_2020, "Spring 2020"),
    )

    position_choices = (
        (GSI, "GSI"),
        (HEAD_GSI, "Head GSI"), 
        (GSR, "GSR"), 
        (TUTOR, "Tutor"), 
        (READER, "Reader"),
        (COURSE_ASST, "Course Assistant"),
    )

    school_choices = (
        (INFORMATION, "Information"), 
        (ECONOMICS, "Economics"), 
        (COG_SCI, "Cognitive Science"),
        (SOCIOLOGY, "Sociology"),
        (ENV_SCI_MGMT, "Environmental, Science, Policy, and Management"),
    )

    percent_choices = (
        (15, "15%"),
        (25, "25%"),
        (40, "40%"), 
        (50, "50%"), 
        (75, "75%"),
    )

    posting_id = models.AutoField(primary_key=True)
    class_code = models.CharField("Class Code", max_length=15)
    class_name = models.CharField("Class Name", max_length=80)
    class_desc = models.TextField("Class Description")
    semester = models.CharField("Semester", max_length=50, choices=semester_choices, blank=True)
    position = models.CharField("Position", max_length=25, choices=position_choices, blank=True)
    school = models.CharField("School", max_length=80, choices=school_choices, blank=True)  
    percent_time = models.IntegerField("Percent Time", choices=percent_choices, null=True, blank=True)
    hours_per_wk = models.IntegerField("Hours Per Week") 
    fee_remission = models.BooleanField("Fee Remission", default=True)
    instructor = models.CharField("Instructor", max_length=200)
    mode = models.CharField("Mode", max_length=80)
    instructor_bio = models.URLField("Instructor Bio")
    class_days = models.CharField("Class Days", max_length=20, null=True, blank=True)
    class_start_time = models.CharField("Class Start Time", max_length=15, null=True, blank=True)
    class_end_time = models.CharField("Class End Time", max_length=15, null=True, blank=True) 
    num_positions = models.IntegerField("Number of Positions", null=True, blank=True)
    position_notes = models.TextField("Notes", blank=True) 
    app_due_date = models.CharField("App Due Date", max_length=50)
    app_url = models.URLField("App URL", null=True) 
    content_search = SearchVectorField(blank=True)
    
    class Meta(object):
        indexes = [GinIndex(fields=["content_search"])]

    def __str__(self):
        """Returns string representation of the model."""
        return f"{self.semester} | {self.school} | {self.position} | {self.class_name}"
