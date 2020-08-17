from rest_framework.serializers import ModelSerializer
from main.models import LanguageModel, SkillModel, EducationModel, CourseModel, ExperienceModel, StatementModel, LetterModel, CertificationModel, InterestModel, PersonModel


class LanguageModelSerializer(ModelSerializer):

    class Meta:
        model = LanguageModel
        fields = '__all__'


class SkillModelSerializer(ModelSerializer):

    class Meta:
        model = SkillModel
        fields = '__all__'


class EducationModelSerializer(ModelSerializer):

    class Meta:
        model = EducationModel
        fields = '__all__'


class CourseModelSerializer(ModelSerializer):

    class Meta:
        model = CourseModel
        fields = '__all__'


class ExperienceModelSerializer(ModelSerializer):

    class Meta:
        model = ExperienceModel
        fields = '__all__'


class StatementModelSerializer(ModelSerializer):

    class Meta:
        model = StatementModel
        fields = '__all__'


class LetterModelSerializer(ModelSerializer):

    class Meta:
        model = LetterModel
        fields = '__all__'


class CertificationModelSerializer(ModelSerializer):

    class Meta:
        model = CertificationModel
        fields = '__all__'


class InterestModelSerializer(ModelSerializer):

    class Meta:
        model = InterestModel
        fields = '__all__'


class PersonModelSerializer(ModelSerializer):

    class Meta:
        model = PersonModel
        fields = '__all__'
