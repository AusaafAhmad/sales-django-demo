from django.urls import path
from .views import sale_per_prod,summary_page,sales_per_state, analysis_page,sales_per_state_page,sales_per_product_page

urlpatterns = [
    path('summary/', summary_page, name='summary-page'),
    path('analysis/', analysis_page, name='analysis-page'),
    path('sales-per-state/', sales_per_state_page, name='salesperstate-page'),
    path('sales-per-product/', sales_per_product_page, name='salesperproduct-page'),

    path('api/sales_per_state/',sales_per_state, name='sales-page-state'),
    path('api/sales_per_product/',sale_per_prod, name='sale-page-prod')
]