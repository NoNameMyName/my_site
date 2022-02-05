from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=1024)
    zip_code = models.CharField(("zip code"), max_length=5, default="49000", validators=[RegexValidator(
        regex=r"^\d{5}$")]
    )
    phone = models.CharField(("phone number"), max_length=5, default="+380xxxxxxxxx", validators=[RegexValidator(
        regex=r"^[+]\d{10,12}$")]
    )
