from django.db import models
from cms.models.pluginmodel import CMSPlugin


class Sprint(CMSPlugin):
    RL = "Real Life Sprint"
    sprint_number_choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (RL, "Real Life Sprint"),
    )
    sprint_number = models.CharField(max_length=16, choices=sprint_number_choices, default='1')