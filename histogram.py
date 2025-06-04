import matplotlib.pyplot as plt
import numpy as np

def create_histogram(data, title, xlabel, ylabel, bins=10):
    """
    Creates and displays a graphical histogram using matplotlib.

    Args:
        data (list or numpy.array): The numerical data to plot.
        title (str): The title of the histogram.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis (frequency/count).
        bins (int): The number of bins to use for the histogram.
    """
    plt.figure(figsize=(10, 6)) # Set the figure size for better readability
    plt.hist(data, bins=bins, edgecolor='black', alpha=0.7) # Create the histogram
    plt.title(title, fontsize=16) # Set title with larger font
    plt.xlabel(xlabel, fontsize=12) # Set x-axis label
    plt.ylabel(ylabel, fontsize=12) # Set y-axis label
    plt.grid(axis='y', alpha=0.75) # Add a grid for better readability
    plt.xticks(fontsize=10) # Adjust x-tick font size
    plt.yticks(fontsize=10) # Adjust y-tick font size
    plt.tight_layout() # Adjust layout to prevent labels from overlapping
    plt.show() # Display the plot

if __name__ == "__main__":
    # --- Sample Dataset: Distribution of Ages in a Population ---
    # This is a hypothetical dataset. For real-world data, you would load it
    # from a CSV, database, or API (like the World Bank data).
    # We'll generate some random age data that roughly follows a normal distribution
    # to simulate a population's age structure.
    np.random.seed(42) # for reproducibility
    population_ages = np.random.normal(loc=35, scale=15, size=1000)
    # Ensure ages are positive and within a reasonable range (e.g., 0 to 90)
    population_ages = np.clip(population_ages, 0, 90)

    # Define the parameters for the histogram
    histogram_title = "Distribution of Ages in a Sample Population"
    x_axis_label = "Age Group"
    y_axis_label = "Number of People"
    number_of_bins = 15 # You can adjust this to see different distributions

    # Call the function to create and display the histogram
    create_histogram(population_ages, histogram_title, x_axis_label, y_axis_label, bins=number_of_bins)

    # --- Another example: Categorical data (simulated with counts) ---
    # While histograms are typically for continuous data, you can visualize
    # categorical distributions using bar charts. Matplotlib's `bar` function
    # is more appropriate for truly categorical data.
    # For demonstration, let's simulate a 'gender' distribution as counts.
    # If you had raw categorical data like ['Male', 'Female', 'Male', ...],
    # you would first count the occurrences of each category.

    # Example of categorical counts (similar to the Java example)
    gender_categories = ['Male', 'Female', 'Non-binary', 'Prefer not to say']
    gender_counts = [450, 520, 30, 10]

    plt.figure(figsize=(8, 5))
    plt.bar(gender_categories, gender_counts, color=['skyblue', 'lightcoral', 'lightgreen', 'lightgray'], edgecolor='black')
    plt.title("Distribution of Genders in a Sample Population", fontsize=16)
    plt.xlabel("Gender Category", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.grid(axis='y', alpha=0.75)
    plt.xticks(rotation=45, ha='right', fontsize=10) # Rotate labels for better readability
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()
