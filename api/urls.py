from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register(r'accounts', views.AccountViewSet)
router.register(r'goals', views.GoalViewSet)
router.register(r'monthly_expenses', views.MonthlyExpenseViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('public', views.public),
    path('private', views.private),
    path('private-scoped', views.private_scoped),
]
