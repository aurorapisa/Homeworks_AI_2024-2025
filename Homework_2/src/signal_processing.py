import numpy as np
import matplotlib.pyplot as plt

def analyze_signal(time_array, clean_signal, noisy_signal):

    # Signal statistics
    mean = np.mean(noisy_signal)
    std_dev = np.std(noisy_signal)
    min_val = np.min(noisy_signal)
    max_val = np.max(noisy_signal)
    snr = np.mean(clean_signal ** 2) / np.mean((noisy_signal - clean_signal) ** 2)  # Signal-to-Noise Ratio

    kernel = np.ones(5) / 5
    filtered_signal = np.convolve(noisy_signal, kernel, mode='same')

    # fft
    freqs = np.fft.fftfreq(len(time_array))
    noisy_fft = np.abs(np.fft.fft(noisy_signal))
    fft_magnitude = np.abs(noisy_fft)

    plt.figure(figsize=(12, 8))

    # Signal Analysis (first subplot)
    plt.subplot(2, 1, 1)
    plt.plot(time_array, clean_signal, label='Clean Signal', color='blue')
    plt.plot(time_array, noisy_signal, label='Noisy Signal', color='red', linestyle='--')
    plt.plot(time_array, filtered_signal, label='Filtered Signal', color='green')
    plt.title(f"Signal Analysis (mean={mean:.2f}, std={std_dev:.2f})")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()

    # Frequency Spectrum (second subplot)
    plt.subplot(2, 1, 2)
    plt.plot(freqs[:len(freqs) // 2], fft_magnitude[:len(fft_magnitude) // 2], color='blue')
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitudine")
    plt.grid()

    plt.tight_layout()
    plt.show()

    # Output for signal statistics
    print("\nSignal statistics:")
    print(f"Mean: {mean:.3f}")
    print(f"Standard Deviation: {std_dev:.3f}")
    print(f"Minimum Value: {min_val:.3f}")
    print(f"Maximum Value: {max_val:.3f}")
    print(f"Signal-to-Noise Ratio (SNR): {snr:.3f}")