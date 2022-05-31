# Property of Umar Faruque
# See readme for documentation
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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


def fastFacts():
    maxYear = sortcounty.loc[sortcounty['Population'].idxmax(), 'Year']
    minYear = sortcounty.loc[sortcounty['Population'].idxmin(), 'Year']
    print("The highest population was", sortcounty['Population'].max(), "in",
          maxYear)
    print("The lowest population was", sortcounty['Population'].min(), "in", minYear)
    percent = sortcounty.values_count
    print("Based off the last 10 years, this population is set to be increasing by: ", percent)


def printCountries():
    truthvar = 0
    while truthvar == 0:
        listCounty = input("Would you like to see the list of counties available in this dataset? y/n: ")
        if listCounty == 'y':
            truthvar = 1
            print('\n'.join(map(str, population['Geography'].unique().tolist())))
            print("\nPrinting county list complete. Please scroll up to see the list.\n")
        elif listCounty == 'n':
            truthvar = 1
            pass
        else:
            print("Invalid input.")


def askTutorial():
    truthvar = 1
    while truthvar > 0:
        tutorialinput = input("Tutorial? y/n: ")
        if tutorialinput == 'y':
            tutorial()
            truthvar = 0
        elif tutorialinput == 'n':
            truthvar = 0
            pass
        else:
            print("Invalid input. Enter y or n.")


def getValidCounty():
    truthvar = 1
    while truthvar == 1:
        county = input(
            "Please enter a valid county: ").title()  # get user input and capitalize it in case user submits lowercase characters
        with open("annualpopulation.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Geography'] == county:
                    truthvar = 0
                    return county
                    break


def askCompareCounty(county):
    truthvar = 1
    while (truthvar == 1):
        # useroption = input("Would you like to compare this county to others?\nPlease enter y/n: ")
        useroption = 'y'
        if useroption == 'y':
            truthvar = 0
            # county2 = getValidCounty()
            county2 = 'Albany County'
            beforeCompareCounty(county, county2)
        elif useroption == 'n':
            truthvar = 0
        else:
            print("Invalid entry. Please try again.")


def beforeCompareCounty(county1, county2):
    truthvar = 0
    while truthvar == 0:
        # askinterval = input(
        #    "Would you like to compare these two counties within a specific time interval?\nPlease enter y/n: ")
        askinterval = 'y'
        if askinterval == 'y':
            truthvar = 1
            #start = int(input("Enter starting year: "))
            start = 1998
            while start < 1970 or start > 2020:
                print("Invalid starting year. Must be between 1970 and 2020.")
                start = input("Enter starting year: ")
            #end = int(input("Enter ending year: "))
            end = 2005
            while end < 1970 or end > 2020:
                print("Invalid ending year. Must be between 1970 and 2020.")
                end = input("Enter ending year: ")
            compareCounty(county1, county2, start, end)
        elif askinterval == 'n':
            truthvar = 1
            break
        else:
            print("Invalid response. Please try again.")


def compareCounty(county1, county2, startperiod, endperiod): # enables us to compare counties
    outputfile = input("Please enter the name of the output file: ")
    sortcounty1 = population.groupby('Geography').get_group(county1)
    plt.plot('Year','Population', 'b', label = county1, data=sortcounty1)
    sortcounty2 = population.groupby('Geography').get_group(county2)
    plt.plot('Year','Population', 'r', label = county2, data=sortcounty2)
    plt.xlim(startperiod, endperiod) # this allows us to graph the starting-end period
    plt.title('Population between ' + county1 + ' and ' + county2 + ' from ' + str(startperiod) + ' to ' + str(endperiod),
              color='black') # the title of the graph
    plt.legend(loc='best') # places the legend indicator best found suitable
    graph = plt.gcf()
    graph.savefig(outputfile)


if __name__ == '__main__':
    population = pd.read_csv('annualpopulation.csv', skiprows=0)
    print("                                         State of New York                        ")
    print("                                    Population Analysis Program                   ")
    print("************************************************************************************************\n         "
          "                   This program was created by: Umar Faruque                            "
          "\n************************************************************************************************\n")
    askTutorial()
    printCountries()
    county = getValidCounty()
    print("In order to see graphs, you must enter an output file, otherwise you will only see statistical information "
          "in the console.\nPlease note: if you would like to create a PDF then append your file with .pdf. The same "
          "logic applies for other file types.")
    # outputfile = input("Please enter the name of the output file: ")
    outputfile = 'file.png'
    sortcounty = population.groupby('Geography').get_group(county)
    sortcounty.plot(x='Year', y='Population')
    plt.title('Population in ' + county + " from 1970 to 2020", color='black')
    graph = plt.gcf()
    graph.savefig(outputfile)
    print("\n********************\nSUCCESS. YOUR FILE HAS BEEN SAVED IN THE LOCAL DIRECTORY.\nPopulation Data for: ",
          county)
    fastFacts()
    askCompareCounty(county)
    print("Thank you for using my program!")
