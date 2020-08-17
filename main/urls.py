from rest_framework.routers import SimpleRouter
from main import views


router = SimpleRouter()

router.register(r'languagemodel', views.LanguageModelViewSet)
router.register(r'skillmodel', views.SkillModelViewSet)
router.register(r'educationmodel', views.EducationModelViewSet)
router.register(r'coursemodel', views.CourseModelViewSet)
router.register(r'experiencemodel', views.ExperienceModelViewSet)
router.register(r'statementmodel', views.StatementModelViewSet)
router.register(r'lettermodel', views.LetterModelViewSet)
router.register(r'certificationmodel', views.CertificationModelViewSet)
router.register(r'interestmodel', views.InterestModelViewSet)
router.register(r'personmodel', views.PersonModelViewSet)

urlpatterns = router.urls
