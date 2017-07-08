from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Sprint

class SprintPlugin(CMSPluginBase):
    model = Sprint
    name = _("Sprint Plugin")
    render_template = "sprint_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(SprintPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(SprintPlugin)
