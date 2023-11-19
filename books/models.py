from django.db import models

# Create your models here.
import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_pdf_file(value):
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    valid_extensions = ['.pdf']

    if not ext.lower() in valid_extensions:
        raise ValidationError(_('The file must be a PDF.'))


class Book(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(max_length=5000)
    pdf = models.FileField(upload_to='books/pdfs/',validators=[validate_pdf_file])
    img = models.ImageField(upload_to="books/image",null=True)

    def __str__(self):
        return self.name

