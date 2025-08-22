import numpy as np


def generate_simple_random_sales():
    
    np.random.seed(40)

    sales = np.random.normal(loc=5000, scale=800, size=10)

    for i, amount in enumerate(sales):
        print(f'day {i+1} sales is ${amount}')

    average = sales.mean()
    print(f'average sales is {average}') 

    # to calculate distance from the mean (sales > 4200) & (sales < 5800)
    close_to_avg = np.abs(sales - 5000) < 800 
    num_close = np.sum(close_to_avg)
    print(f"Days within $800 of $5000: {num_close} out of {len(sales)}")

def main():
    generate_simple_random_sales()

if __name__ == '__main__':
    main()
