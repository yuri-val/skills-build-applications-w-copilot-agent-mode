from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    # Додаткові поля за потреби

    def __str__(self):
        return self.email

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # у хвилинах
    points = models.IntegerField()
    date = models.DateTimeField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    total_points = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
