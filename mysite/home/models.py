from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class HomePage(Page):
    first_name  = models.CharField(
        blank=True,
        max_length=255, help_text="Please enter your first name."
    )

    content_panels = Page.content_panels + [
                FieldPanel("first_name")
            ]
