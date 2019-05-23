from django.db import models

from django.db import models
from tenant_schemas.models import TenantMixin

class Client(TenantMixin):
    """
    TenantMixin has 2 fields
        - domain_url
        - schema_name
    """

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    auto_drop_schema = True
    
    def __str__(self):
        return self.name