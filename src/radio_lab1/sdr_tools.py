"""
Tools for loading and processing SDR data from Lab 1.
"""

import numpy as np

def load_sdr_data(filepath, block_idx = 0):
    """
    Load SDR data from a .npz file.
    
    Parameters
    ----------
    filepath : str
        Path to .npz file.
    block_idx : int, optional
        Index of the block to load (default 0).
    
    Returns
    -------
    signal : ndarray
        1D array of voltage samples.
    """
    data = np.load(filepath)
    # Assume data is stored under key 'arr_0'
    signal = data['arr_0'][block_idx].astype(float)
    
    return signal

def normalize_signal(signal):
    """
    Remove DC offset and scale to unit standard deviation.
    
    Parameters
    ----------
    signal : ndarray
        Input voltage array.
    
    Returns
    -------
    normalized : ndarray
        Zero-mean, unit-variance signal.
    """
    signal = signal - np.mean(signal)
    
    return signal / np.std(signal)

def compute_power_spectrum(signal, fs):
    """
    Compute the power spectrum of a signal.
    
    Parameters
    ----------
    signal : ndarray
        Time-domain voltage samples.
    fs : float
        Sampling frequency in Hz.
    
    Returns
    -------
    freqs : ndarray
        Frequency array (positive frequencies only, in Hz).
    power : ndarray
        Power spectral density.
    """
    N = len(signal)
    freqs = np.fft.fftfreq(N, d = 1/fs)
    spectrum = np.fft.fft(signal)
    power = np.abs(spectrum)**2 / N
    # Return only positive frequencies
    pos_mask = freqs >= 0
    
    return freqs[pos_mask], power[pos_mask]