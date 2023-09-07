import numpy as np
from scipy.integrate import solve_ivp

def setup_kuramoto(N, w, K, tspan):
    def ode(t, theta):
        theta_dot = w + K/N * np.sum(np.sin(theta - theta[:, np.newaxis]), axis=1)
        return theta_dot

    thetaI = (np.arange(1, N+1) / N) * 2 * np.pi  # Initial phase starts uniform around unit circle

    sol = solve_ivp(ode,(tspan[0],tspan[-1]),thetaI,t_eval=tspan)

    t = sol.t
    theta = sol.y
    complexform = np.exp(1j * theta)
    order = np.abs(1/N * np.sum(np.exp(1j * theta), axis=0))
    theta = np.transpose(theta)

    return t, theta, complexform, order



