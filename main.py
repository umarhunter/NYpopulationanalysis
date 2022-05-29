# Property of Umar Faruque
# See readme for documentation
import csv

import matplotlib.pyplot as plt
import pandas as pd


def tutorial():
    print("*********************\nTutorial\n*********************")
    print(
        "This program will allow you to select a county in New York State. The years supported are 1970 to 2020. Upon "
        "selection, it will allow you to see "
        "statistical information about the selected county. All the necessary user inputs will be done through the "
        "console.")
    print("If you are not familiar with New York State counties, then you will be given the choice to view a list "
          "of available counties. Newly registered counties after 2020 are not supported.\n*****************************************************")


def fastfacts():
    maxYear = sortCounty.loc[sortCounty['Population'].idxmax(), 'Year']
    minYear = sortCounty.loc[sortCounty['Population'].idxmin(), 'Year']
    print("The highest population was", sortCounty['Population'].max(), "in", maxYear)
    print("The lowest population was", sortCounty['Population'].min(), "in", minYear)


def printCountries():
    print('\n'.join(map(str, population['Geography'].unique().tolist())))


if __name__ == '__main__':
    population = pd.read_csv('annualpopulation.csv', skiprows=0)
    print("                                         State of New York                        ")
    print("                                    Population Analysis Program                   ")
    print("************************************************************************************************\n         "
          "                   This program was created by: Umar Faruque                            "
          "\n************************************************************************************************\n")
    truthVar = 1
    while truthVar > 0:
        tutorialInput = input("Tutorial? y/n: ")
        if tutorialInput == 'y':
            tutorial()
            truthVar = 0
        elif tutorialInput == 'n':
            truthVar = 0
            pass
        else:
            print("Invalid input. Enter y or n.")

    while truthVar == 0:
        listCounty = input("Would you like to see the list of counties available in this dataset? y/n: ")
        if listCounty == 'y':
            truthVar = 1
            printCountries()
            print("\nPrinting county list complete. Please scroll up to see the list.\n")
        elif listCounty == 'n':
            truthVar = 1
            pass
        else:
            print("Invalid input.")

    #while truthVar == 1:
    #    county = input("Please enter a valid county: ").title() #get user input and capitalize it in case user submits lowercase characters
    #    county = county.title()  # capitalizes input so that lower case works
    #    with open("annualpopulation.csv") as csvfile:
    #        reader = csv.DictReader(csvfile)
    #        for row in reader:
    #            if row['Geography'] == county:
    #                truthVar = 0
    #                break

    county = 'Queens County'.title()  # used for speeding through test
    print("In order to see graphs, you must enter an output file, otherwise you will only see statistical information "
          "in the console.\nPlease note: if you would like to create a PDF then append your file with .pdf. The same "
          "logic applies for other file types.")
    outputFile = input("Please enter the name of the output file: ")

    sortCounty = population.groupby('Geography').get_group(county)
    sortCounty.plot(x='Year', y='Population')
    graph = plt.gcf()
    graph.savefig(outputFile)
    print("Population Data for: ", county)
    fastfacts()

