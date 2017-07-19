from datetime import date

from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField

real_life_sprint = "Real Life Sprint"
sprint_number_choices = tuple([(str(n), str(n)) for n in range(1, 10)] + [(real_life_sprint, real_life_sprint)])

test_case_fases = (
    "To Start", "In development", "Being reviewed", "Ready for test", "Being tested", "Tested, findings in progress",
    "Tested, findings solved")

fase_test_cases_choices = ((option, option) for option in test_case_fases)


class Sprint(CMSPlugin):
    sprint_number = models.CharField(max_length=16, choices=sprint_number_choices, default="1")
    starting_date = models.DateField(default=date.today)
    ending_date = models.DateField(default=date.today)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Sprint: %s" % self.sprint_number

    def get_absolute_url(self):
        return reverse('sprint-view', kwargs={'pk': self.id})


class Tester(CMSPlugin):
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    notes = models.TextField()

    def __str__(self):
        return "Tester: {} {}".format(self.first_name, self.last_name)


class Process(CMSPlugin):
    """
    Process plugin is designed to describe one company process and the state
    of the test cases. A process can have multiple testers.
    """
    name = models.CharField(max_length=128, null=True, blank=True)
    number = models.CharField(max_length=12, null=True, blank=True)
    fase_test_cases = models.CharField(max_length=24, choices=fase_test_cases_choices, default="To Start")
    testers = models.ManyToManyField(Tester)
    process_model = FilerImageField(null=True, blank=True, related_name="process_model")
    notes = models.TextField()

    def __str__(self):
        return self.name
