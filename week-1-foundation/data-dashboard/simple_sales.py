import numpy as np

def create_simple_sales():
    daily_sales=np.array([1500, 2500, 1600, 2100, 1900])
    return daily_sales

def basic_calculations(sales_data):
    avg_sales = np.mean(sales_data)
    print(f'average sales - {avg_sales}')

    max_sales  = np.max(sales_data)
    min_sales = np.min(sales_data)
    print(f'max sales - {max_sales}, min sales - {min_sales}')

    total_sales = np.sum(sales_data)
    print(f'total sales - {total_sales}')

    best_day_index = np.argmax(sales_data)  #np.argmax - return the index of the maximum value
    worst_day_index = np.argmin(sales_data)
    print(f'best day - {best_day_index + 1}, worst day - {worst_day_index + 1}')

def array_operation(sales_data):
    # percentage, with bonus, commission rate
    total_sales = np.sum(sales_data)
    total_percentage = (sales_data / total_sales) * 100

    for perc in total_percentage:
        print(f'total percentage - {perc}')

    withBonus = 500
