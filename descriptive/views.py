from django.shortcuts import render
from django.views import View
import pandas as pd
from django.http import JsonResponse
import os

class SalesSummaryView(View):

    def get(self, request):
        # path =  os.path.join(os.path.dirname(os.path.dirname(__file__), 'sales_data.csv'))
        csv = "/home/metal/Desktop/ml/sales_data.csv"
        df = pd.read_csv(csv)
        summary =  {
            'total_sales': float(df['TotalPrice'].sum()),
            'total_quantity' : int(df['Quantity'].sum()),
            'average_unit_price': float(df['UnitPrice'].mean()),
            'products': df['ProductName'].nunique(),
            'states': df['State'].nunique()
        }

        return JsonResponse(summary)
    

    
    

    
def summary_page(request):
    return render(request, 'descriptive/summary.html')

def sales_per_state_page(request):
    return render(request, 'descriptive/sales_per_state.html')

def sales_per_product_page(request):
    return render(request, 'descriptive/sales_per_product.html')

def analysis_page(request):
    return render(request, 'descriptive/analysis.html')


def sales_per_state(req):
    csv = "/home/metal/Desktop/ml/sales_data.csv"
    df = pd.read_csv(csv)
    state_sales  =  df.groupby("State")["TotalPrice"].sum().reset_index()
    state_sales = state_sales.sort_values("TotalPrice",ascending=False)
    data =  state_sales.to_dict(orient="records")

    return JsonResponse({"sales_per_state": data})

def sale_per_prod(req):
    csv = "/home/metal/Desktop/ml/sales_data.csv"
    df = pd.read_csv(csv)
    prod_sales =  df.groupby("ProductName")["TotalPrice"].sum().reset_index()
    prod_sales = prod_sales.sort_values("TotalPrice",ascending=False)
    data =  prod_sales.to_dict(orient="records")

    return JsonResponse({"sales_per_product": data})