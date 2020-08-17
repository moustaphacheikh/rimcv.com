from rest_framework.viewsets import ModelViewSet
from main.serializers import LanguageModelSerializer, SkillModelSerializer, EducationModelSerializer, CourseModelSerializer, ExperienceModelSerializer, StatementModelSerializer, LetterModelSerializer, CertificationModelSerializer, InterestModelSerializer, PersonModelSerializer
from main.models import LanguageModel, SkillModel, EducationModel, CourseModel, ExperienceModel, StatementModel, LetterModel, CertificationModel, InterestModel, PersonModel


class LanguageModelViewSet(ModelViewSet):
    queryset = LanguageModel.objects.order_by('pk')
    serializer_class = LanguageModelSerializer


class SkillModelViewSet(ModelViewSet):
    queryset = SkillModel.objects.order_by('pk')
    serializer_class = SkillModelSerializer


class EducationModelViewSet(ModelViewSet):
    queryset = EducationModel.objects.order_by('pk')
    serializer_class = EducationModelSerializer


class CourseModelViewSet(ModelViewSet):
    queryset = CourseModel.objects.order_by('pk')
    serializer_class = CourseModelSerializer


class ExperienceModelViewSet(ModelViewSet):
    queryset = ExperienceModel.objects.order_by('pk')
    serializer_class = ExperienceModelSerializer


class StatementModelViewSet(ModelViewSet):
    queryset = StatementModel.objects.order_by('pk')
    serializer_class = StatementModelSerializer


class LetterModelViewSet(ModelViewSet):
    queryset = LetterModel.objects.order_by('pk')
    serializer_class = LetterModelSerializer


class CertificationModelViewSet(ModelViewSet):
    queryset = CertificationModel.objects.order_by('pk')
    serializer_class = CertificationModelSerializer


class InterestModelViewSet(ModelViewSet):
    queryset = InterestModel.objects.order_by('pk')
    serializer_class = InterestModelSerializer


class PersonModelViewSet(ModelViewSet):
    queryset = PersonModel.objects.order_by('pk')
    serializer_class = PersonModelSerializer
