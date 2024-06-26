from django.conf import settings
from django.utils.translation import gettext_lazy as _

use = False
if "cms" in settings.INSTALLED_APPS and "filer" in settings.INSTALLED_APPS:
    use = True

CKEDITOR_LINK_USE_CMS_FILER = getattr(settings, "CKEDITOR_LINK_USE_CMS_FILER", use)

CKEDITOR_LINK_MODEL_USE_FILER_ADDONS = getattr(
    settings,
    "CKEDITOR_LINK_MODEL_USE_FILER_ADDONS",
    False,
)

CKEDITOR_LINK_STYLE_CHOICES = getattr(
    settings,
    "CKEDITOR_LINK_STYLE_CHOICES",
    (
        ("", _("Default")),
        ("button", _("Button")),
    ),
)

if CKEDITOR_LINK_USE_CMS_FILER:
    CKEDITOR_LINK_TYPE_CHOICES = getattr(
        settings,
        "CKEDITOR_LINK_TYPE_CHOICES",
        (
            ("", _("None")),
            ("cms_page", _("Page")),
            ("file", _("File")),
            ("free", _("Other / Free")),
            ("external", _("External URL")),
            ("mailto", _("E-Mail")),
            ("phone", _("Phone")),
        ),
    )
else:
    CKEDITOR_LINK_TYPE_CHOICES = getattr(
        settings,
        "CKEDITOR_LINK_TYPE_CHOICES",
        (
            ("", _("None")),
            ("free", _("Other / Free")),
            ("external", _("External URL")),
            ("mailto", _("E-Mail")),
            ("phone", _("Phone")),
        ),
    )
