# Kuramoto_model
Model coupled oscillators using Kuramoto model. Useful functions to setup, plot and extract Kuramoto model parameters.

Example:
[t,theta,complexform,order] = setup_kuramoto(5,rand(1,5)',.3,[0:.1:500]')
plot_kuramoto(t,theta)

User can define
N, number of coupled oscillators
w, corresponding intristic frequencies
c, coupling parameter [0 ,1]
t, time vector



Inspired by:
Cleve Moler (2023). Kuramoto's model of synchronizing oscillators (https://www.mathworks.com/matlabcentral/fileexchange/72534-kuramoto-s-model-of-synchronizing-oscillators), MATLAB Central File Exchange. Retrieved March 7, 2023.
https://www.complexity-explorables.org/explorables/ride-my-kuramotocycle/
