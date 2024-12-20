import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import glob


def sine_func(t, V0, phi):
    return V0 * np.sin(2 * np.pi * f * t-phi)

def calcAmpAndPhase(VR, time, f):
    start_index = int(len(time) * .9)
    time_steady = time[start_index:]
    VR_steady = VR[start_index:]
    
    popt, _ = curve_fit(sine_func, time_steady, VR_steady, p0=[3.0, 0.0])
    
    V0_fit, phi_fit = popt
    
    delta_t = phi_fit/(2*np.pi*f)
    return V0_fit, phi_fit, delta_t

files = glob.glob("freq*_data.txt") #Need since i decieded to create a new file per freq

calculated_amp = []
calculated_PS = []
freqencies = []
for file in files:
    frequency = int(file.split('freq')[1].split('_')[0])  

    data = np.loadtxt(file, delimiter=",", skiprows=1)

    amplitude = data[0, 0]  
    phase_shift = data[0, 1]
    time = data[:, 2]
    Vd = data[:, 3]
    VR = data[:, 4]
    VL = data[:, 5]
    VC = data[:, 6]

    freqencies.append(frequency)
    calculated_amp.append(amplitude)
    calculated_PS.append(phase_shift)
    
frequencies = np.array(freqencies)
amplitudes = np.array(calculated_amp)
phase_shift = np.array(calculated_PS)


for f in freqencies:
    V0, phi, delta_t = calcAmpAndPhase(VR, time, f)
    
    calculated_amp.append(V0)
    calculated_PS.append(phi)

plt.figure(figsize=(12,8))
plt.suptitle(r"$Driven LRC circuit, R = 1kΩ, C = .5 nF, L = 20 mH$")
#plot 1
plt.subplot(2,2,1)
plt.plot(time[:500], VC[:500], label = r"$V_C(t) [V]$", color = "red")
plt.plot(time[:500], VL[:500], label = r"$V_L(t) [V]$", color = "blue")
plt.plot(time[:500], VR[:500], label = r"$V_R(t) [V]$", color = "green")
plt.tick_params(axis="x", top = True, labeltop = True, bottom = True, labelbottom = False)
plt.ylabel("Voltage [V]")
#plot 2
plt.subplot(2,2,2)
plt.plot(time[600:], VC[600:], label = r"$V_C(t) [V]$", color = "red")              
plt.plot(time[600:], VL[600:], label = r"$V_L(t) [V]$", color = "blue")
plt.plot(time[600:], VR[600:], label = r"$V_R(t) [V]$", color = "green")
plt.tick_params(axis="x", top = True, labeltop = True, bottom = True, labelbottom = False)
plt.ylabel("Voltage [V]")
plt.gca().set_xticklabels([54, 55, 56, 57, 58, 59, 60])
plt.legend(loc = "upper right", bbox_to_anchor=(1,1))

plt.text(1.05, 0.5, f"Driving Voltage:\n$V_d0 = {Vd[0]:.1f} kHz$\nf = {frequency:.1f} kHz\n" +
         f"Initial Conditions:\n$q_0 = 0.0 C$\n" +
         f"$i_0 = 0.0 mA$", transform=plt.gca().transAxes,
         fontsize=12, verticalalignment='center', horizontalalignment='left',
         bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))
#plot 3
plt.subplot(2,2,3)
plt.plot(time[:600], VR[:600], label = r"$V_R(t) [V]$", color = "green")
plt.plot(time[:600], Vd[:600], label = r"$V_d(t) [V]$", color = "orange")
plt.ylabel("Voltage [V]")
#plot 4
plt.subplot(2,2,4)
plt.plot(time[600:], VR[600:], label = r"$V_R(t) [V]$", color = "green")
plt.plot(time[600:], Vd[600:], label = r"$V_d(t) [V]$", color = "orange")
plt.ylabel("Voltage [V]")
plt.legend(loc = "upper right", bbox_to_anchor=(1,1.1))

plt.text(1.05, 0.5, f"Resonance freq.:\n$f_0 = {frequency} kHz$\n" +
         f"Output voltage:\n$V_0 = {V0:.1f} V$\n" +
         f"Phase shift: \nΔT = {time[1]-time[0]} T", transform=plt.gca().transAxes,
         fontsize=12, verticalalignment='center', horizontalalignment='left',
         bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))


plt.tight_layout()
plt.savefig("RobertoRamil_Final_Fig1.pdf")  # Save figure as PDF
plt.show()


plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(frequencies, amplitudes, label="Amplitude", color="blue")
plt.title("Amplitude vs Frequency")
plt.tick_params(axis="x", top = True, labeltop = True, bottom = True, labelbottom = False)
plt.xlabel("f [kHz]")
plt.ylabel(r"$Amplitude of V_R [V]$")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(frequencies, phase_shift, label="Phase Shift", color="blue")
plt.title("Phase Shift vs Frequency")
plt.xlabel("f [kHz]")
plt.ylabel("phase shift Δt/T")
plt.legend()

plt.tight_layout()
plt.savefig("RobertoRamil_Final_Fig2.pdf")  # Save figure as PDF
plt.show()
