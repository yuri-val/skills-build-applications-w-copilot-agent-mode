from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value) if isinstance(value, ObjectId) else value
    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    class Meta:
        model = User
        fields = ['_id', 'email', 'name', 'password']

class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['_id', 'name', 'members']

class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        pk_field=ObjectIdField()
    )
    class Meta:
        model = Activity
        fields = ['_id', 'user', 'activity_type', 'duration', 'points', 'date']

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    team = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        pk_field=ObjectIdField()
    )
    class Meta:
        model = Leaderboard
        fields = ['_id', 'team', 'total_points']

class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'suggested_for']
