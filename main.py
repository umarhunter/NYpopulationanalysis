# Property of Umar Faruque
# See readme for documentation

import matplotlib.pyplot as plt
import pandas as pd
print("                            State of New York                        ")
print("                       Population Analysis Program                   ")
print("******************************\nThis program was created by: Umar Faruque\n***************************\n")

borough = input("Please enter a borough: ")
outputname = input("Please enter output name: ")

pop = pd.read_csv('annualpopulation.csv', skiprows=0)

pop['Fraction'] = pop[borough] / pop['Case Count']
pop.plot(x='Date of Interest', y='Fraction')

print("The minimum number of infections in the" + borough + "is", pop[borough].min())
print("The maximum number of infections in the" + borough + "is", pop[borough].max())
print("The average number of infections in the" + borough + "is", pop[borough].mean())
print("The median number of infections in the" + borough + "is", pop[borough].median())
print("The standard deviation of infections in the" + borough + "is", pop[borough].std())

fig = plt.gcf()
fig.savefig(outputname)
