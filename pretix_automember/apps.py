from django.utils.translation import gettext_lazy

from . import __version__

try:
    from pretix.base.plugins import PluginConfig, PLUGIN_LEVEL_ORGANIZER
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    default = True
    name = "pretix_automember"
    verbose_name = gettext_lazy("Automember")

    class PretixPluginMeta:
        name = gettext_lazy("Automember")
        author = "activivan"
        description = gettext_lazy("Auto assign membership to customers on login")
        visible = True
        version = __version__
        category = "FEATURE"
        compatibility = "pretix>=2.7.0"
        plugin_level = PLUGIN_LEVEL_ORGANIZER
        settings_links = []
        navigation_links = []

    def ready(self):
        from . import signals  # NOQA
