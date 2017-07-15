from django.db import models
from cms.models.pluginmodel import CMSPlugin
from datetime import date
from filer.fields.image import FilerImageField


class Sprint(CMSPlugin):
    RL = "Real Life Sprint"
    One = "1"
    Two = "2"
    Three = "3"
    Four = "4"
    Five = "5"
    Six = "6"
    Seven = "7"
    Eight = "8"
    Nine = "9"
    sprint_number_choices = (
        (One, "1"),
        (Two, "2"),
        (Three, "3"),
        (Four, "4"),
        (Five, "5"),
        (Six, "6"),
        (Seven, "7"),
        (Eight, "8"),
        (Nine, "9"),
        (RL, "Real Life Sprint"),
    )
    sprint_number = models.CharField(max_length=16, choices=sprint_number_choices, default="1")
    starting_date = models.DateField(default=date.today)
    ending_date = models.DateField(default=date.today)
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):

        return reverse('sprint-view', kwargs={'pk': self.id})


class Tester(CMSPlugin):
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    notes = models.TextField()


class Process(CMSPlugin):
    """
    Process plugin is designed to describe one company process and the state
    of the test cases. A process can have multiple testers.
    """
    TS = "To Start"
    ID = "In development"
    BR = "Being reviewed"
    RFT = "Ready for test"
    T = "Being tested"
    TF = "Tested, findings in progress"
    TFD = "Tested, findings solved"
    fase_test_cases_choices = (
        (TS, "To Start"),
        (ID, "In development"),
        (BR, "Being reviewed"),
        (RFT, "Ready for test"),
        (T, "Being tested"),
        (TF, "Tested, findings in progress"),
        (TFD, "Tested, findings solved"),
    )
    name = models.CharField(max_length=128, null=True, blank=True)
    number = models.CharField(max_length=12, null=True, blank=True)
    fase_test_cases = models.CharField(max_length=24, choices=fase_test_cases_choices, default="To Start")
    testers = models.ManyToManyField(Tester)
    process_model = FilerImageField(null=True, blank=True, related_name="process_model")
    notes = models.TextField()
