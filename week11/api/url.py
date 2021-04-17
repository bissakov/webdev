from django.urls import path

from api.views import company_list, company_detail
from api.views import vacancy_detail, vacancy_list
from api.views import vacancy_topten, from_company_vacancy


urlpatterns = [
    path('companies', company_list),
    path('companies/<int:company_id>/', company_detail),
    path('vacancies', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', vacancy_topten),
    path('companies/<int:company_id>/vacancies', from_company_vacancy)
]