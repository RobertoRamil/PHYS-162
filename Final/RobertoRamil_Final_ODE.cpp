#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <iomanip>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::ofstream;
using std::vector;

const double PI = std::acos(-1);

// Constants
const double R = 1000.0;              // Resistance (Ohms)
const double C = 0.5e-9;             // Capacitance (Farads)
const double L = 20e-3;              // Inductance (Henries)
const double Vd0 = 3.0;              // Driving voltage (Volts)
const double f_min = 20000.0;        // Minimum frequency (Hz)
const double f_max = 75000.0;        // Maximum frequency (Hz)
const double f_step = 500.0;         // Frequency step (Hz)
const int steps_per_period = 100;    // Time steps per period
const double dt_factor = 100;        // Time step factor (1/100 of the period)

double drivingVoltage(double t, double f) {
    return Vd0 * sin(2.0 * PI * f * t);
}

void calcAmpAandPhaseShift(const std::vector<double>& time, const std::vector<double>& VR, double f, double& amplitude, double& phase_shift){
    size_t start_index = time.size() * .9;
    vector<double> time_steady(time.begin() + start_index, time.end());
    vector<double> VR_steady(VR.begin() + start_index, VR.end());

    double maxVR = *max(VR_steady.begin(), VR_steady.end());
    double minVR = *min(VR_steady.begin(), VR_steady.end());
    amplitude = (maxVR-minVR)/2.0;

    double delta_t = 0.0;
    for (size_t i = 1; i < VR_steady.size(); ++i) {
        if ((VR_steady[i-1] <= 0 && VR_steady[i] > 0) || (VR_steady[i-1] >= 0 && VR_steady[i] < 0)) {
            delta_t = time_steady[i];
            break;
        }
    }
    phase_shift = 2.0 * PI * f * delta_t;
}

int main() {

    for (double f = f_min; f <= f_max; f += f_step) {
        double T = 1.0 / f;                 // Period (seconds)
        double dt = T / dt_factor;          // Time step (1/100 of the period)
        int steps = 60 * steps_per_period;  // Total steps (60 periods)

        // Initial conditions
        double q = 0.0;
        double i = 0.0;

        vector<double> time, Vd, VR, VL, VC;

        for (int n = 0; n <= steps; n++) {
            double t = n * dt;
            double vd = drivingVoltage(t, f);

            // Update rules
            double di = (vd - q / C - R * i) * (dt / L);
            double dq = i * dt;

            i += di;
            q += dq;

            // Collect data for steady-state (last 5 periods)
            if ((t >=0 && t<= 6*T)||(t >= 55 * T && t <= 60 * T)) {
                time.push_back(t);
                Vd.push_back(vd);
                VR.push_back(R * i);
                VL.push_back(L * di /dt);
                VC.push_back(q / C);
            }
        }

        double amplitude, phase_shift;
        calcAmpAandPhaseShift(time, VR, f, amplitude, phase_shift);

        ofstream output("freq" + std::to_string(int(f/1000))+ "_data.txt");
        output <<"Amp, Phaseshift, Time, Vd, Vr, VL, VC\n";

        for (size_t i = 0; i < time.size(); i++){
            output << amplitude << "," << phase_shift << ","
                   << time.at(i) << "," << Vd.at(i) << "," << VR.at(i) << ","
                   << VL.at(i) << "," << VC.at(i) << endl;
        }

        output.close();
        cout << "data saved to freq" << int(f/1000) << "_data.txt." << endl;
        
    }

    


    return EXIT_SUCCESS;
}