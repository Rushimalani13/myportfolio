import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class Contactdb(DjangoCassandraModel):
    id=columns.UUID(primary_key=True,default=uuid.uuid4)
    email=columns.Text(required=False)
    name=columns.Text(required=False)
    concern=columns.Text(required=False)
    city=columns.Text(required=False)
    state=columns.Text(required=False)
    zip=columns.Text(required=False)
    