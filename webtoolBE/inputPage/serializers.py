# for converting to JSON object
from rest_framework import serializers
from .models import Input

# An InputSerializer class with fields that get serialized/deserialized
class InputSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Input # your model
        field = ('input','inputFile','created')

    #id = serializers.IntegerField(read_only=True)
    unit = serializers.CharField()
    inputFile = serializers.CharField()

    def create(self, validated_data):
            """
            Create and return a new `Input` instance, given the validated data.
            """
            return Input.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Input` instance, given the validated data.
        """
        instance.unit= validated_data.get('unit', instance.unit)
        instance.inputFile = validated_data.get('inputFile', instance.inputFile)
        instance.save()
        return instance

