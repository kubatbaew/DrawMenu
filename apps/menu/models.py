from django.db import models


class Menu(models.Model):
    title = models.CharField(
        max_length=120,
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        related_name="children",
        blank=True, null=True,
    )
    menu_name = models.CharField(
        max_length=120,
    )

    def __str__(self):
        return f"{self.title}"
