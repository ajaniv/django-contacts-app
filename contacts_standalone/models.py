from django.db import models
from core.models import meta
from core import fields
# Create your models here.
if __name__ == "__main__":
    class BaseModel(models.Model):
        class Meta:
            pass
    @meta(BaseModel.Meta, '_app_label')
    class ContactName(BaseModel):
        """
        Contact name details class.
        """
        family_name = fields.char_field(max_length=1024)
        given_name = fields.char_field(max_length=1024)