import pandas as pd

# Sample dataset
data = {
    'square_footage': [1500, 1800, 2400, 3000, 3500],
    'bedrooms': [3, 4, 3, 5, 4],
    'bathrooms': [2, 3, 2, 4, 3],
    'location': ['A', 'B', 'A', 'B', 'A'],
    'price': [300000, 400000, 350000, 500000, 450000]
}

df = pd.DataFrame(data)

def predict_price(square_footage, bedrooms, bathrooms, location):
    # Base prices for different locations
    location_base_price = {
        'A': 300000,
        'B': 350000
    }
    
    # Adjustments based on features
    price = location_base_price.get(location, 0)
    price += (square_footage - 2000) * 50  # Adjust for square footage
    price += (bedrooms - 3) * 10000        # Adjust for number of bedrooms
    price += (bathrooms - 2) * 15000       # Adjust for number of bathrooms
    
    return price

# Sample inputs
inputs = [
    (2000, 4, 3, 'A'),
    (2500, 3, 2, 'B'),
    (1800, 3, 2, 'A'),
    (3000, 5, 4, 'B'),
    (3500, 4, 3, 'A')
]

# Predict prices
for inp in inputs:
    price = predict_price(*inp)
    print(f"Predicted price for house with {inp[0]} sqft, {inp[1]} bedrooms, {inp[2]} bathrooms in location {inp[3]}: ${price:.2f}")
