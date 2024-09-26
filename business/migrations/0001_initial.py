import uuid
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('social_name', models.CharField(max_length=500)),
                ('cnpj', models.CharField(max_length=14)),
                ('is_active', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address_street', models.CharField(blank=True, max_length=200, null=True)),
                ('address_number', models.CharField(blank=True, max_length=10, null=True)),
                ('address_neighborhood', models.CharField(blank=True, max_length=100, null=True)),
                ('address_city', models.CharField(blank=True, max_length=100, null=True)),
                ('address_state', models.CharField(blank=True, max_length=100, null=True)),
                ('address_zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'businesses',
            },
        ),
    ]
