from django.db import models
from cms.models.pluginmodel import CMSPlugin
from datetime import date


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


class Tester(CMSPlugin):
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    notes = models.TextField()
