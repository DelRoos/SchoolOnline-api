from .models import Speciality, Level, Classe, Matter
from .serializers import SpecialitySerializer, LevelSerializer, ClasseSerializer, MatterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class SpecialityList(generics.ListCreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class LevelList(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    
class ClasseList(generics.ListCreateAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    
class MatterList(generics.ListCreateAPIView):
    queryset = Matter.objects.all()
    serializer_class = MatterSerializer
    
class SpecialityAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class LevelAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class ClasseAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    
class MatterAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matter.objects.all()
    serializer_class = MatterSerializer