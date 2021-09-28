# Generated by Django 3.2.7 on 2021-09-28 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import oauth2_provider.generators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesstoken',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='expires',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='id_token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='access_token', to=settings.OAUTH2_PROVIDER_ID_TOKEN_MODEL),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='scope',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='source_refresh_token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='refreshed_access_token', to=settings.OAUTH2_PROVIDER_REFRESH_TOKEN_MODEL),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='token',
            field=models.CharField(default='123123', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_server_accesstoken', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application',
            name='algorithm',
            field=models.CharField(blank=True, choices=[('', 'No OIDC support'), ('RS256', 'RSA with SHA-2 256'), ('HS256', 'HMAC with SHA-2 256')], default='', max_length=5),
        ),
        migrations.AddField(
            model_name='application',
            name='authorization_grant_type',
            field=models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials'), ('openid-hybrid', 'OpenID connect hybrid')], default='authorization-code', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='client_id',
            field=models.CharField(db_index=True, default=oauth2_provider.generators.generate_client_id, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='application',
            name='client_secret',
            field=models.CharField(blank=True, db_index=True, default=oauth2_provider.generators.generate_client_secret, max_length=255),
        ),
        migrations.AddField(
            model_name='application',
            name='client_type',
            field=models.CharField(choices=[('confidential', 'Confidential'), ('public', 'Public')], default='confidential', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='application',
            name='redirect_uris',
            field=models.TextField(blank=True, help_text='Allowed URIs list, space separated'),
        ),
        migrations.AddField(
            model_name='application',
            name='skip_authorization',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_server_application', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grant',
            name='application',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api_server.application'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grant',
            name='claims',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='grant',
            name='code',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grant',
            name='code_challenge',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='grant',
            name='code_challenge_method',
            field=models.CharField(blank=True, choices=[('plain', 'plain'), ('S256', 'S256')], default='plain', max_length=10),
        ),
        migrations.AddField(
            model_name='grant',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grant',
            name='expires',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grant',
            name='nonce',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='grant',
            name='redirect_uri',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grant',
            name='scope',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='grant',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='grant',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='api_server_grant', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idtoken',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ),
        migrations.AddField(
            model_name='idtoken',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idtoken',
            name='expires',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idtoken',
            name='jti',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='JWT Token ID'),
        ),
        migrations.AddField(
            model_name='idtoken',
            name='scope',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='idtoken',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='idtoken',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_server_idtoken', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='refreshtoken',
            name='access_token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='refresh_token', to=settings.OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL),
        ),
        migrations.AddField(
            model_name='refreshtoken',
            name='application',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api_server.application'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refreshtoken',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refreshtoken',
            name='revoked',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='refreshtoken',
            name='token',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refreshtoken',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='refreshtoken',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='api_server_refreshtoken', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accesstoken',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='grant',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='idtoken',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
