from django.urls import path
from .views import cpu_summary, cpu_graph_data, cpu_bar_chart_page, cpu_scatter_plot_page,cpu_dashboard_page,cpu_summary_page

urlpatterns = [
    path('api/cpu/summary/', cpu_summary, name='cpu-summary'),
    path('api/cpu/graph-data/', cpu_graph_data, name='cpu-graph-data'),
    path('cpu/bar-chart/', cpu_bar_chart_page, name='cpu-bar-chart'),
    path('cpu/scatter-plot/', cpu_scatter_plot_page, name='cpu-scatter-plot'),
    path('cpu/dashboard/', cpu_dashboard_page, name='cpu-dashboard'),
    path('cpu/summary/', cpu_summary_page, name='cpu-summary-page'),
]