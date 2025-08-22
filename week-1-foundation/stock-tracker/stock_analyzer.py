import numpy as np

def read_stock_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    dates = []
    opens = []
    highs = []
    lows = []
    closes = []
    volumes = []

    for line in lines[1:]:
        values = line.strip().split(',')

        dates.append(values[0])           # Date as string
        opens.append(float(values[1]))    # Convert to numbers
        highs.append(float(values[2]))
        lows.append(float(values[3]))
        closes.append(float(values[4]))
        volumes.append(int(values[5]))

    # Convert to NumPy arrays for analysis
    stock_data = {
        'dates': dates,  # Keep dates as strings for now
        'open': np.array(opens),
        'high': np.array(highs),
        'low': np.array(lows),
        'close': np.array(closes),
        'volume': np.array(volumes)
    }
    
    return stock_data

if __name__ == "__main__":
    try:
        data = read_stock_data('sample_stock_data.csv')
        print("\n✅ Data loaded successfully!")
        print(f"Close prices: {data['close']}")
        print(f"Price range: ${data['close'].min():.2f} - ${data['close'].max():.2f}")
    except FileNotFoundError:
        print("❌ Could not find sample_stock_data.csv")
        print("Make sure you created the CSV file first!")
    except Exception as e:
        print(f"❌ Error: {e}")
