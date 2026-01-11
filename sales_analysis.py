import csv

FILE_NAME = "sales_data.csv"

def load_sales_data():
    sales = []
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales.append(row)
    return sales

def calculate_total_sales(sales):
    total = 0
    for row in sales:
        total += float(row["Sales"])
    return total

def calculate_average_sales(sales):
    return calculate_total_sales(sales) / len(sales)

def calculate_monthly_sales(sales):
    monthly = {}
    for row in sales:
        month = row["Month"]
        amount = float(row["Sales"])
        if month in monthly:
            monthly[month] += amount
        else:
            monthly[month] = amount
    return monthly

def forecast_next_period_sales(sales):
    average = calculate_average_sales(sales)
    forecast = average * 1.05  # 5% growth assumption
    return forecast

def main():
    sales_data = load_sales_data()

    total_sales = calculate_total_sales(sales_data)
    average_sales = calculate_average_sales(sales_data)
    monthly_sales = calculate_monthly_sales(sales_data)
    forecast_sales = forecast_next_period_sales(sales_data)

    print("===== Sales Performance Analysis =====")
    print("Total Sales:", total_sales)
    print("Average Sales:", round(average_sales, 2))

    print("\nMonthly Sales Breakdown:")
    for month, amount in monthly_sales.items():
        print(month, ":", amount)

    print("\nForecasted Sales for Next Period:", round(forecast_sales, 2))

main()
