import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('GenericMedicines.csv')

# Basic info
print(data.info())
print(data.describe())

# Remove duplicates
data.drop_duplicates(inplace=True)

# Top locations
top_locations = data['Location'].value_counts().head(5)
print(top_locations)

# Plotting
top_locations.plot(kind='bar', title='Top 5 Supplier Locations')
plt.ylabel('Number of Products')
plt.xlabel('Location')
plt.show()
