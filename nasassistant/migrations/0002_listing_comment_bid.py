# Generated by Django 4.0 on 2022-06-30 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nasassistant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('start_bid', models.FloatField()),
                ('actual_price', models.FloatField()),
                ('url_img', models.CharField(blank=True, max_length=1000)),
                ('category', models.CharField(choices=[('NO CATEGORY', 'NO CATEGORY'), ('MEN', 'MEN'), ('WOMEN', 'WOMEN'), ('HATS', 'HATS'), ('GIFTS', 'GIFTS')], default='No category', max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_listings', to='nasassistant.user')),
                ('watched_by', models.ManyToManyField(blank=True, related_name='watching', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('information', models.CharField(max_length=30000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_comments', to='nasassistant.user')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='nasassistant.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidding_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('price', models.FloatField()),
                ('bid_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_bids', to='nasassistant.user')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='l_bids', to='nasassistant.listing')),
            ],
        ),
    ]
