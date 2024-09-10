import matplotlib.pyplot as plt
import numpy as np

print("Python script has started.")
print("Creating a simple plot...")
plt.figure()
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9],	# list of x-values to plot
	[1, 4, 2, 5, 6, 4, 4, 8, 10],  		# list of y-values to plot
	color="blue",        	#  Line color
	linestyle=":",     	#  Line style
	marker="*",         	#  Symbol used at data point
	markeredgecolor="red"  # Symbol color
	)
plt.xlabel('Time')
plt.ylabel('Growth')
plt.title("HW1Plot")

x = np.arange(0,2*np.pi, .1) #making x an array from 0 to 2pi, incrementing by .1
y = np.sin(x) #making y an array of sine of x from the previous function.

plt.plot(
    x,y,
	color = "black"
)

plt.legend(["Random Points", "Sine Graph"])

print("Showing plot window.")
print("Nothing else will happen until you close the plot window!")
plt.savefig("RobertoRamil_hw01-p1_image.pdf")
plt.show()
print("Python script is done.")