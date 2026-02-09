"""
Basic unit tests for radio_lab1 package.
"""

import numpy as np
from radio_lab1.sdr_tools import normalize_signal, compute_power_spectrum

def test_normalize_signal():
    """Test that normalize_signal removes mean and gives unit variance."""
    
    sig = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    normed = normalize_signal(sig)
    
    assert np.abs(np.mean(normed)) < 1e-10, "Mean should be zero"
    assert np.abs(np.std(normed) - 1.0) < 1e-10, "Std should be 1"
    
    print("✓ normalize_signal test passed")

def test_compute_power_spectrum():
    """Test power spectrum on a simple sine wave."""
   
    fs = 1000  # 1 kHz sampling
    t = np.arange(0, 1, 1/fs)
    sig = np.sin(2 * np.pi * 100 * t)  # 100 Hz sine wave
    
    freqs, power = compute_power_spectrum(sig, fs)
    
    # Should have peak near 100 Hz
    peak_freq = freqs[np.argmax(power)]
    assert np.abs(peak_freq - 100) < 1, f"Peak should be near 100 Hz, got {peak_freq}"
    
    print("✓ compute_power_spectrum test passed")

if __name__ == "__main__":
    test_normalize_signal()
    test_compute_power_spectrum()
    print("\nAll tests passed!")