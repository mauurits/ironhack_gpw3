# Project overview
In our group project in week 3 we chose to take a closer look at a topic which concerns us all: The qualty of the air we breathe everyday (in europe). Due to its significant nature there were many sources to choose datasets from and it took a while until we found a fitting one. After this step was accomplished we spent the following days to have a closer look at the data, familiarize us with the topic at hand, brainstorm ideas and formulate hypotheses, clean the adapt the dateset and finally represent it in a graphical format in order to draw visual conclusions for our hypotheses.

# Questions 
After having selected our dataset we came up with three questions/hypotheses we wanted to check for:
1. Has the air quality depreciated over the last years?
2. Has the rate of air pollution been higher in larger populated areas than in smaller ones?
3. Are there more premature deaths linked to areas with higher air pollution?
4. A general comparison of the 10 biggest cities in the EU

# Dataset 
The dataset we worked with was from the European Environment Agency 

## Main dataset issues
- redundant columns
- NaN-values
- Understanding the columns correctly
- not everything included in the data what we wanted to present

## Solutions for the dataset issues
- Necessary to create additional columns
- substitution of NaN-values with median values of the column but grouped to the respective year and city
- made use of an API to determine the geo coordinates in order to create heat maps

# Conclussions
- Hypo 1 → proven not to be correct, air pollution has actually decreased over the last years
- Hypo 2 → was proven to be generally correct, with some exceptions like e.g Barcelona where the air pollution is over proportionally high for its population density, or the netherlands which have a relatively high population density but comparably low air pollution levels
- Hypo 3 → proven to be right, strong correlation of the trends of premature deaths and air pollution levels


# Next steps
...
