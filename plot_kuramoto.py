# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:28:07 2023

@author: OMISTAJA
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_kuramoto(t, theta):
    r = 1
    polarX = r * np.cos(theta)
    polarY = r * np.sin(theta)
    z = np.abs(1/theta.shape[1] * np.sum(np.exp(1j * theta), axis=1))
    aveX = np.mean(polarX, axis=1)
    aveY = np.mean(polarY, axis=1)
    
    plt.figure(figsize=(12, 6))
    
    for i in range(len(t)):
    
        # Polar plot
        ax1=plt.subplot(241)#, projection='polar'))
        plt.title('Polar')
        #plt.plot(np.linspace(-np.pi, np.pi, 100), r * np.sin(np.linspace(-np.pi, np.pi, 100)), 'k', linewidth=2)    
        plt.plot( r*np.cos(np.linspace(-np.pi,np.pi,100)),r*np.sin(np.linspace(-np.pi,np.pi,100)), 'k', linewidth=2)

        
        plt.scatter(polarX[i], polarY[i], s=40, c='k')
        plt.quiver(0, 0, aveX[i], aveY[i], linewidth=2, color='k')
        plt.xlim([-1.5, 1.5])
        plt.ylim([-1.5, 1.5])
    
        # Amplitude plot
        ax2=plt.subplot(2, 4, (2, 4))
        plt.title('Amplitude')
        plt.xlabel('Time / s')
        window = 50
        from_idx = max(0, i - window)
        to_idx = i
        plt.xlim([t[from_idx], t[to_idx + 10]])
        plt.ylim([-1.5, 1.5])
        for j in range(theta.shape[1]):
            plt.plot(t[from_idx:to_idx + 1], polarY[from_idx:to_idx + 1, j], 'k', linewidth=2)
        plt.scatter([t[to_idx]] * theta.shape[1], polarY[to_idx], s=40, c='k')
    
        # Order parameter plot
        ax3=plt.subplot(2, 4, (6, 8))
        plt.title('Order parameter κ')
        plt.xlabel('Time / s')
        plt.xlim([t[from_idx], t[to_idx + 10]])
        plt.ylim([0, 1.2])
        plt.plot(t[from_idx:to_idx + 1], z[from_idx:to_idx + 1], 'k', linewidth=2)
        plt.scatter(t[to_idx], z[to_idx], s=40, c='k')
    
        plt.show()
        plt.pause(0.1)  # Add a pause between frames
        ax1.clear()
        ax2.clear()
        ax3.clear()
