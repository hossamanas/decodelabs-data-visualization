import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_project_visualizations(data_path):
    # 1. Load cleaned master dataset
    print("Loading dataset for visual mapping...")
    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Set seaborn aesthetics
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({'font.size': 10, 'axes.labelsize': 11, 'axes.titlesize': 13})
    
    # -------------------------------------------------------------
    # CHART 1: Revenue by Product Category (Bar Chart)
    # -------------------------------------------------------------
    print("Generating Chart 1: Revenue by Product...")
    product_sales = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False).reset_index()
    
    plt.figure(figsize=(9, 5))
    barplot = sns.barplot(x='TotalPrice', y='Product', data=product_sales, palette='Blues_r')
    plt.title('Total Revenue Performance by Product Category')
    plt.xlabel('Total Revenue ($)')
    plt.ylabel('Product Category')
    plt.tight_layout()
    plt.savefig('chart1_product_revenue.png', dpi=300)
    plt.close()
    
    # -------------------------------------------------------------
    # CHART 2: Order Fulfillment Status (Pie Chart)
    # -------------------------------------------------------------
    print("Generating Chart 2: Order Fulfillment Proportions...")
    status_counts = df['OrderStatus'].value_counts()
    
    plt.figure(figsize=(6, 6))
    colors = ['#e74c3c', '#f39c12', '#f1c40f', '#3498db', '#2ecc71'] # clear distinct colors
    plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('Proportional Breakdown of Order Fulfillment Statuses')
    plt.tight_layout()
    plt.savefig('chart2_order_status.png', dpi=300)
    plt.close()
    
    # -------------------------------------------------------------
    # CHART 3: Timeline Sales Trend Analysis (Line Chart)
    # -------------------------------------------------------------
    print("Generating Chart 3: Historical Sales Trend Line...")
    df['YearMonth'] = df['Date'].dt.to_period('M')
    monthly_sales = df.groupby('YearMonth')['TotalPrice'].sum().reset_index()
    monthly_sales['YearMonth'] = monthly_sales['YearMonth'].astype(str)
    
    plt.figure(figsize=(11, 5))
    plt.plot(monthly_sales['YearMonth'], monthly_sales['TotalPrice'], marker='o', color='#2980b9', linewidth=2)
    plt.title('Historical Monthly Revenue Trend Analysis')
    plt.xlabel('Timeline (Year-Month)')
    plt.ylabel('Total Revenue ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('chart3_monthly_trend.png', dpi=300)
    plt.close()
    
    print("All project charts generated successfully and saved as image files.")

if __name__ == "__main__":
    generate_project_visualizations('حسام.xlsx - Sheet1.csv')
