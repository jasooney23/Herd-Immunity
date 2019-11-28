# Herd-Immunity
Simple simulation of herd immunity, in predicting the spread of a particular disease. (has some minor issues with how the infection spreads)

Works on Mac and Windows.


To change the variables of the simulation, edit the variables in the herdImmunity.py file:

size (int): The size of the grid of people in the simulation. (The total people will be size^2)

immunity (int): The percentage of the population that is vaccinated (immune) to the vaccine. If this is set to 100% immunity,   
    one person is randomly selected to be infected. (I don't remember why this was implemented, probably so I would have to do 
    less exception handling)
    
contagion (int): The chance that an infected person will infect someone else per hour (in percentage).

days (int), hours (int): The time limit of the simulation in days and hours, respectively.

speed (int or float): The speed at which the simulation will run. (A speed of 1 is approximately 1 simulation hour per second)
