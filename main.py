# Property of Umar Faruque
# See readme for documentation

import matplotlib.pyplot as plt
import pandas as pd


def tutorial():
    print("*********************\nTutorial\n*********************")
    print("This program will allow you to select a county in New York State. The years supported are 1970 to 2020. Upon selection, it will allow you to see "
          "statistical information about the selected county. All the necessary user inputs will be done through the "
          "console.")
    whileVar = 1
    while (whileVar > 0):
        viewInput = input("")


def fastfacts():
    pass
    # print("The highest population " + + "is", population[county].min())
    # print("The maximum number of []s in the" + + "is", population[county].max())
    # print("The average number of []s in the" + + "is", population[county].mean())
    # print("The median number of [] in the" + + "is", population[county].median())
    # print("The standard deviation of [] in the" + county + "is", population[county].std())


if __name__ == '__main__':
    population = pd.read_csv('annualpopulation.csv', skiprows=0)
    print("                                         State of New York                        ")
    print("                                    Population Analysis Program                   ")
    print("************************************************************************************************\n         "
          "                   This program was created by: Umar Faruque                            "
          "\n************************************************************************************************\n")
    tutorialWV = 1
    while tutorialWV > 0:
        tutorialInput = input("Tutorial? y/n: ")
        if tutorialInput == 'y':
            tutorial()
            tutorialWV = 0
        elif tutorialInput == 'n':
            tutorialWV = 0
            pass
        else:
            print("Invalid input. Enter y or n.")
    # maybe ask user if they need a list of the counties here
    county = input("Please enter a county: ")
    county = county.title()
    outputFile = file.pdf
    locationData = population.groupby('Geography')
    countyPop = population.groupby().get_group(county)
    population.plot(x=countyPop, y='Population')

    fig = plt.gcf()
    fig.savefig(outputFile)
