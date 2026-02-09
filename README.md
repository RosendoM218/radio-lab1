# Installation and Verification Instructions
This section explains how to install the radio_lab1 package and verify it works in both terminal and Jupyter Notebook. These instructions are tested on Windows, but the workflow is similar for macOS/Linux.

### 1️⃣ Clone the repository
```bash 
git clone https://github.com/RosendoM218/radio-lab1.git
cd radio-lab1
```
Note: If Git is not available, you can download the repository as a ZIP file and extract it.

### 2️⃣ Create a clean virtual environment
Creating a virtual environment ensures the package is installed in an isolated Python environment.

Windows (Command Prompt recommended):

```bash
python -m venv venv
venv\Scripts\activate.bat
macOS/Linux:

python3 -m venv venv
source venv/bin/activate
The prompt should now show (venv) indicating the virtual environment is active.
```

### 3️⃣ Upgrade pip (optional but recommended)
```bash
python -m pip install --upgrade pip
```

### 4️⃣ Install the package
```bash
pip install .
This installs the radio_lab1 package in the current environment.
```
### 5️⃣ Verify the installation in the terminal
```bash
python -c "import radio_lab1; print(radio_lab1.__file__)"
python -c "from radio_lab1.sdr_tools import compute_power_spectrum; print(compute_power_spectrum)"
```
Expected output:

The first line shows a path ending in radio_lab1\__init__.py in your site-packages.

The second line shows something like <function compute_power_spectrum at 0x...>.

### 6️⃣ Optional: Verify in Jupyter Notebook
Install Jupyter support:
```bash
pip install ipykernel notebook
```
Register the virtual environment as a kernel:
```bash
python -m ipykernel install --user --name radio_lab1_test --display-name "Python (radio_lab1)"
```
Launch Jupyter Notebook:
```bash
jupyter notebook
```
In the notebook interface, select Kernel → Python (radio_lab1).

Test the package in a cell:
```bash
import radio_lab1
from radio_lab1.sdr_tools import compute_power_spectrum, load_sdr_data

print(radio_lab1.__file__)         # Shows the package location
print(compute_power_spectrum)      # Prints the function object
```

### 7️⃣ Uninstall the package (if needed)
```bash
pip uninstall radio_lab1 -y
```

### 8️⃣ Quick Start Example
```bash
import numpy as np
from radio_lab1.sdr_tools import compute_power_spectrum, normalize_signal

# Create a dummy signal (replace with real data when available)
signal = np.random.randn(1024)

# Normalize the signal
signal_norm = normalize_signal(signal)

# Compute the power spectrum
spectrum = compute_power_spectrum(signal_norm)

# Print a preview of the spectrum
print("First 10 values of the power spectrum:")
print(spectrum[:10])
```
This example runs immediately after installation and shows that the core functions are working.