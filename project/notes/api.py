from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')
    
    def create(self, validated_data):
        #import pdb; pdb.set_trace()
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        user = self.request.user
        #import pdb; pdb.set_trace()
        if user.is_anonymous:
            return PersonalNote.objects.none()
        elif str(user) == 'admin':
            return PersonalNote.objects.all()
        else:
            return PersonalNote.objects.filter(user=user)