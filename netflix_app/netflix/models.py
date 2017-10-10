from django.db import models

# Create your models here.
class User(models.Model):
    """
    User Model
    Defines the attributes of an user
    """
    user_id = models.IntegerField(primary_key = True)
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    zip_id = models.ForeignKey('Zip', on_delete = models.CASCADE)
    user_country = models.CharField(max_length=255)
    user_phone = models.IntegerField()
    plan_id = models.ForeignKey('Plans', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def get_breed(self):
    #     return self.name + ' belongs to ' + self.breed + ' breed.'
    #
    # def __repr__(self):
    #     return self.name + ' is added.'


class Zip(models.Model):
    """
    Zip Model
    Defines the attributes of a zip code
    """
    zip_id = models.IntegerField(primary_key = True)
    state = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


class Access(models.Model):
    """
    Access Model
    Defines the attributes of an access type
    """
    access_id = models.IntegerField(primary_key = True)
    user_name = models.CharField(max_length=255)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    user_pass = models.CharField(max_length=255)


class Plans(models.Model):
    """
    Plans Model
    Defines the attributes of a plan
    """
    plan_id = models.IntegerField(primary_key = True)
    plan_desc = models.CharField(max_length=255)
    plan_price = models.IntegerField()


class Payment(models.Model):
    """
    Payments Model
    Defines the attributes of a payment
    """
    payment_id = models.IntegerField(primary_key = True)
    payment_date = models.DateTimeField(auto_now_add=True)
    plan_id = models.ForeignKey('Plans', on_delete = models.CASCADE)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)


class User_Rentals(models.Model):
    """
    User Rentals Model
    Defines the attributes of an user rental
    """
    user_rental_id = models.IntegerField(primary_key = True)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    rental_id = models.ForeignKey('Rentals', on_delete = models.CASCADE)


class Rentals(models.Model):
    """
    Rentals Model
    Defines the attributes of a rental
    """
    rental_id = models.IntegerField(primary_key = True)
    stream_date = models.DateTimeField(auto_now_add=True)
    stream_length = models.IntegerField()
    content_id = models.ForeignKey('Content', on_delete = models.CASCADE)


class Content(models.Model):
    """
    Content Model
    Defines the attributes of a movie/tv show/any other content
    """
    content_id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255)
    release_year = models.IntegerField()
    director_id = models.ForeignKey('Director', on_delete = models.CASCADE)
    cast_id = models.ForeignKey('Cast', on_delete = models.CASCADE)
    genre_id = models.ForeignKey('Genre', on_delete = models.CASCADE)
    type_id = models.ForeignKey('Type', on_delete = models.CASCADE)


class Type(models.Model):
    """
    Type Model
    Defines the attributes of content type - PG recommended etc
    """
    type_id = models.IntegerField(primary_key = True)
    type_desc = models.CharField(max_length=255)


class Genre(models.Model):
    """
    Genre Model
    Defines the attributes of a genre
    """
    genre_id = models.IntegerField(primary_key = True)
    genre_desc = models.CharField(max_length=255)


class Ratings(models.Model):
    """
    Ratings Model
    Defines the attributes of ratings
    """
    ratings_id = models.IntegerField(primary_key = True)
    video_quality = models.IntegerField(default = 0)
    audio_quality = models.IntegerField(default = 0)
    subtitle_quality = models.IntegerField(default = 0)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    content_id = models.ForeignKey('Content', on_delete = models.CASCADE)


class Director(models.Model):
    """
    Directors Model
    Defines the attributes of a director
    """
    director_id = models.IntegerField(primary_key = True)
    director_name = models.CharField(max_length=255)


class Cast(models.Model):
    """
    Cast Model
    Defines the attributes of a cast member
    """
    cast_id = models.IntegerField(primary_key = True)
    cast_name = models.CharField(max_length=255)
