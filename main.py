# Property of Umar Faruque
# See readme for documentation

import matplotlib.pyplot as plt
import pandas as pd


def tutorial():
    print("*********************\nTutorial\n*********************")
    print("This program will allow you to select a county in New York State. Upon selection, it will allow you to see "
          "statistical information about the selected county. All the necessary user inputs will be done through the "
          "console.")
    print("")
    viewInput = input("")


def fastfacts():
    pass
    # print("The highest population " + + "is", population[county].min())
    # print("The maximum number of []s in the" + + "is", population[county].max())
    # print("The average number of []s in the" + + "is", population[county].mean())
    # print("The median number of [] in the" + + "is", population[county].median())
    # print("The standard deviation of [] in the" + county + "is", population[county].std())


if __name__ == '__main__':
    print("                                         State of New York                        ")
    print("                                    Population Analysis Program                   ")
    print("************************************************************************************************\n         "
          "                   This program was created by: Umar Faruque                            "
          "\n************************************************************************************************\n")
    county = input("Please enter a county: ")
    county = county.title()
    # outputFile = input("Please enter output name: ")
    population = pd.read_csv('annualpopulation.csv', skiprows=0)
    countyPop = population.groupby().get_group(county)
    population.plot(x='Date of Interest', y='Fraction')

    # fig = plt.gcf()
    # fig.savefig(outputFile)
