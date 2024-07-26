from django.db import models


from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)


class User(models.Model):
    username = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Indicator(models.Model):
    date_valid_until = models.DateField()
    article_name = models.CharField(max_length=255)
    article_code = models.CharField(max_length=255, null=True)
    order = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Header(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Line(models.Model):
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    header = models.ForeignKey(Header, on_delete=models.CASCADE)
    distribution_count = models.IntegerField()
    targeted_distribution_count = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

