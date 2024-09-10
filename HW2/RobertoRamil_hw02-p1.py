import matplotlib.pyplot as plt
import numpy as np

print("Python script has started.")
print("Creating a simple plot...")
plt.figure()
pl1x = 1, 2, 3, 4, 5, 6, 7, 8, 9
pl1y = 1, 4, 2, 5, 6, 4, 4, 8, 10
plt.plot(pl1x, pl1y,  		# list of y-values to plot
	color="blue",        	#  Line color
	linestyle=":",     	#  Line style
	marker="*",         	#  Symbol used at data point
	markeredgecolor="red",  # Symbol color
	label = "points"
	)
plt.xlabel('Time')
plt.ylabel('Growth')
plt.title("HW2-p1 Plot")

x = np.arange(0,2*np.pi, .1) #making x an array from 0 to 2pi, incrementing by .1

#plotting x and sinx as the y values on the graph.
plt.plot(
    x, np.sin(x),
    linestyle = "-",
	color = "black",
	label = "Sine Graph"
)

#Plot that has x going from 0 to pi with .1 intervals and y = to the cos of x.
plt.plot(
	x, np.cos(x),
 linestyle = "--",
 color = "red",
 linewidth = 3,
 label = "Cosine Graph"
)

#making a function that returns the equeation using x as the main variable
def f(x):
    return (1/np.sqrt(2))*(np.sin(x)+np.cos(x))
    
    
#using x and the equation to make the new line.
plt.plot(x, f(x),
         linestyle = "-.",
		color = "green",
        label = "1/sqrt(2)*sinx+cosx"
)
    





plt.legend()

print("Showing plot window.")
print("Nothing else will happen until you close the plot window!")
plt.savefig("RobertoRamil_hw02-p1_image.pdf")
plt.show()
print("Python script is done.")