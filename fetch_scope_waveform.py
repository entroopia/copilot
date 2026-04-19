import pyvisa
import numpy as np
import matplotlib.pyplot as plt

OSC_IP = '192.168.1.82'
CHANNEL = 3

# VISA resource string for LAN connection
resource_str = f'TCPIP0::{OSC_IP}::inst0::INSTR'

rm = pyvisa.ResourceManager()
print('Connecting to oscilloscope...')
osc = rm.open_resource(resource_str, timeout=10000)
print('IDN:', osc.query('*IDN?'))

# Set data source to channel 3
osc.write(f':WAV:SOUR CHAN{CHANNEL}')
osc.write(':WAV:FORM BYTE')
osc.write(':WAV:MODE NORM')

# Get preamble for scaling
preamble = osc.query(':WAV:PRE?').split(',')
x_increment = float(preamble[4])
x_origin = float(preamble[5])
y_increment = float(preamble[7])
y_origin = float(preamble[8])
y_reference = float(preamble[9])

# Request waveform data
osc.write(':WAV:DATA?')
data = osc.read_raw()
# Remove header (first 11 bytes for Keysight)
header_len = 2 + int(data[1:2])
raw = data[header_len:]

# Convert to numpy array
wave = np.frombuffer(raw, dtype=np.uint8)
voltages = (wave - y_reference) * y_increment + y_origin

# Time axis
times = np.arange(len(voltages)) * x_increment + x_origin

# Plot waveform and FFT
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Time-domain waveform
ax1.plot(times, voltages)
ax1.set_title(f'Channel {CHANNEL} Waveform from Keysight MSOX3024G')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)')
ax1.grid(True)

# FFT (magnitude spectrum)
N = len(voltages)
dt = x_increment
fft_vals = np.fft.fft(voltages)
fft_freqs = np.fft.fftfreq(N, dt)
fft_magnitude = np.abs(fft_vals) / N

# Only plot the positive frequencies
pos_mask = fft_freqs >= 0

ax2.plot(fft_freqs[pos_mask], fft_magnitude[pos_mask])
ax2.set_title('FFT Spectral Magnitude')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Magnitude')
ax2.set_xlim(0, 100_000)  # Limit to 100 kHz
ax2.grid(True)

plt.tight_layout()
plt.show()

osc.close()
