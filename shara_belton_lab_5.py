"""
Python command line menu-driven application that allows a user to load one of two CSV files
and then perform histogram analysis and plots for select variables on the datasets. The first
dataset represents the population change for specific dates for U.S. regions. The second dataset
represents Housing data over an extended period of time describing home age, number of bedrooms
and other variables. 
"""
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Upload the population data to python application.
pop_data = pd.read_csv('csv_file/PopChange.csv')
population = np.array(pop_data)
print(population)
# Upload the housing data to python application.
house_data = pd.read_csv('csv_file/Housing.csv')
housing = np.array(house_data)
print(housing)
def population_data():
    """
    Uploads csv file of population data then displays the menu
    """
    col_choice = -1
    while col_choice != 5:
        print("\n\nYou have entered Population Data."
          "Select the Column you want to analyze: "
              "[Enter 1, 2, 3, or 4]\n")
        # Try except to make sure entering a word does not crash the program
        try:
            col_choice = int(input("\n(1) Pop Apr 1"
                                     "\n(2) Pop Jul 1"
                                     "\n(3) Change Pop"
                                   "\n(4) Exit Column\n"))
            match col_choice:
                case 1:
                    analysis_of_pop_data(4)
                case 2:
                    analysis_of_pop_data(5)
                case 3:
                    analysis_of_pop_data(6)
                case 4:
                    print("\nYou selected to exit the column menu\n")
                    return
                case _:
                    print("ERROR: Please enter a valid number."
                          "You must enter the number 1, 2, 3, or 4")
        except ValueError:
            print("Sorry, please only enter numbers.")
def analysis_of_pop_data(col_number):
    """
    Calculations and analysis of data using pandas.Displays histogram, performs
    histogram analysis and plots for chosen column from the population data.
    """
    # initialize analysis variables
    col_number = int(col_number)
    data_count = 0
    data_mean = 0
    data_sdev = 0
    data_min = float(population[data_count][col_number])
    data_max = float(population[data_count][col_number])
    # pandas to get stats from column using col number starting from 0.
    # ex. april 1 is col 4
    data_count = len(pop_data.iloc[:,col_number])
    data_mean = round(pop_data.iloc[:,col_number].mean(),1)
    data_sdev = round(pop_data.iloc[:,col_number].std(),1)
    data_min = round(pop_data.iloc[:,col_number].min(),1)
    data_max = round(pop_data.iloc[:,col_number].max(),1)
    print("The statistics for this column are: \n"
          "Count: "+ str(data_count) + "\n"
          "Mean: "+ str(data_mean) + "\n"
          "Standard Deviation: "+ str(data_sdev) + "\n"
          "Min: "+ str(data_min) + "\n"
          "Max: "+ str(data_max) + "\n"
          "The Histogram of this column is now displayed.\n")
    # Define new variable names for n, bins, and patches
    hist_counts, hist_bins, hist_patches = plt.hist(population[:,col_number],
                                                    bins = 50,
                                                    density = True,
                                                    edgecolor = 'black',
                                                    facecolor = "r",
                                                    alpha = 0.75)
    plt.grid(True)
    print("More info: \n"
          f"The histogram counts are: {hist_counts}\n"
          f"The histogram bins are: {hist_bins}\n"
          f"The histogram patches are: {hist_patches}\n")
    plt.show()
def housing_data():
    """Uploads csv file of housing data then displays the menu"""
    col_choice_2 = -1
    while col_choice_2 != 6:
        print("\n\nYou have entered Housing Data."
          "Select the Column you want to analyze: "
              "[Enter 1, 2, 3, 4, 5, or 6]\n")
        # Try except to make sure entering a word does not crash the program
        try:
            col_choice_2 = int(input("\n(1) AGE"
                                    "\n(2) BEDRMS"
                                    "\n(3) BUILT"
                                    "\n(4) ROOMS"
                                    "\n(5) UTILITY"
                                    "\n(6) Exit Column\n"))
            match col_choice_2:
                case 1:
                    analysis_of_house_data(0)
                case 2:
                    analysis_of_house_data(1)
                case 3:
                    analysis_of_house_data(2)
                case 4:
                    analysis_of_house_data(4)
                case 5:
                    analysis_of_house_data(6)
                case 6:
                    print("\nYou selected to exit the column menu\n")
                    return
                case _:
                    print("ERROR: Please enter a valid number."
                          "You must enter the number 1, 2, 4, 5, or 6")
        except ValueError:
            print("Sorry, please only enter numbers.")
def analysis_of_house_data(col_number_2):
    """
    Displays histogram, performs histogram analysis and plots for
    the chosen column from the housing data.
    """
    # initialize variables
    col_number_2 = int(col_number_2)
    data_count = 0
    data_mean = 0
    data_sdev = 0
    data_min = float(housing[data_count][col_number_2])
    data_max = float(housing[data_count][col_number_2])
    # pandas to get stats from column using col number starting from 0.
    # ex. april 1 is col 4
    data_count = len(house_data.iloc[:,col_number_2])
    data_mean = round(house_data.iloc[:,col_number_2].mean(),1)
    data_sdev = round(house_data.iloc[:,col_number_2].std(),1)
    data_min = round(house_data.iloc[:,col_number_2].min(),1)
    data_max = round(house_data.iloc[:,col_number_2].max(),1)
    print("The statistics for this column are: \n"
          "Count: "+ str(data_count) + "\n"
          "Mean: "+ str(data_mean) + "\n"
          "Standard Deviation: "+ str(data_sdev) + "\n"
          "Min: "+ str(data_min) + "\n"
          "Max: "+ str(data_max) + "\n"
          "The Histogram of this column is now displayed.\n")
    hist_counts, hist_bins, hist_patches = plt.hist(housing[:,col_number_2],
                                                    bins = 50,
                                                    density = True,
                                                    edgecolor = 'black',
                                                    facecolor = "r",
                                                    alpha = 0.75)
    plt.grid(True)
    # Added because pylint detected unused variables
    print("More info: \n"
          f"The histogram counts are: {hist_counts}\n"
          f"The histogram bins are: {hist_bins}\n"
          f"The histogram patches are: {hist_patches}\n")
    plt.show()
def main():
    """
    Main Function to call all other functions in the program.
    """
    user_choice = -1
    while user_choice != 3:
        print("\n\n***************** Welcome to the Python "
              "Data Analysis App ********** \n"
          "Select the file you want to analyze: "
              "[Enter 1, 2, or 3]\n")
        # Try except to make sure entering a word does not crash the program
        try:
            user_choice = int(input("\n(1) Population Data"
                                     "\n(2) Housing Data"
                                     "\n(3) Exit the Program"))
            match user_choice:
                case 1:
                    population_data()
                case 2:
                    housing_data()
                case 3:
                    print("Thank you for using the Python Data Analysis App!")
                    sys.exit(0)
                case _:
                    print("ERROR: Please enter a valid number."
                          "You must enter the number 1, 2, or 3")
        except ValueError:
            print("Sorry, please only enter numbers.")
# End -- Shara Belton SDEV300/7380
main()
