from django.shortcuts import render
from django.views import View
import pandas as pd
from django.http import JsonResponse
import os

def cpu_summary(request):
    csv = "/home/metal/Desktop/ml/cpu_data.csv"
    df = pd.read_csv(csv)

    df = df.dropna(subset=['price', 'cpuMark', 'cpuValue', 'threadMark', 'powerPerf'])
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['cpuMark'] = pd.to_numeric(df['cpuMark'], errors='coerce')
    df['cpuValue'] = pd.to_numeric(df['cpuValue'], errors='coerce')
    df['threadMark'] = pd.to_numeric(df['threadMark'], errors='coerce')
    df['powerPerf'] = pd.to_numeric(df['powerPerf'], errors='coerce')
    top_cpu = df.loc[df['cpuMark'].idxmax()]['cpuName']
    best_value_cpu = df.loc[df['cpuValue'].idxmax()]['cpuName']
    best_thread_cpu = df.loc[df['threadMark'].idxmax()]['cpuName']
    best_power_cpu = df.loc[df['powerPerf'].idxmax()]['cpuName']
    median_price = df['price'].median()
    budget_df = df[df['price'] <= median_price]
    best_budget_cpu = budget_df.loc[budget_df['cpuMark'].idxmax()]['cpuName']

    summary = {
        "top_cpu": top_cpu,
        "most_price_efficient_cpu": best_value_cpu,
        "best_multithreaded_cpu": best_thread_cpu,
        "most_power_efficient_cpu": best_power_cpu,
        "best_budget_cpu": best_budget_cpu
    }

    return JsonResponse(summary)


def cpu_graph_data(request):
    csv = "/home/metal/Desktop/ml/cpu_data.csv"
    df = pd.read_csv(csv)

    df = df.dropna(subset=['price', 'cpuMark', 'cpuValue'])
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['cpuMark'] = pd.to_numeric(df['cpuMark'], errors='coerce')
    df['cpuValue'] = pd.to_numeric(df['cpuValue'], errors='coerce')
    top10 = df.nlargest(10, 'cpuMark')[['cpuName', 'cpuMark']].to_dict(orient='records')
    scatter_data = df[['cpuName', 'price', 'cpuMark', 'cpuValue']].to_dict(orient='records')

    return JsonResponse({
        "bar_chart_top10": top10,
        "scatter_plot_data": scatter_data
    })
def cpu_dashboard_page(request):
    return render(request, 'descriptive/cpu_dashboard.html')

def cpu_bar_chart_page(request):
    return render(request, 'descriptive/cpu_bar_chart.html')

def cpu_scatter_plot_page(request):
    return render(request, 'descriptive/cpu_scatter_plot.html')

def cpu_summary_page(request):
    return render(request, 'descriptive/cpu_summary.html')
