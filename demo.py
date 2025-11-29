import mne
import os
import defusedxml


# Make sure your MFF folder ends with `.mff`
mff_dir = 'AA_20160922_113850.mff'  # Replace with your renamed folder path

# Load using generic loader (auto-detects MFF)
raw = mne.io.read_raw(mff_dir, preload=True)

# View info
print(raw.info)

# Check channel names and types
print("Channel names:", raw.ch_names)
print("Channel types:", raw.get_channel_types())


raw.plot(title='EEG Signal', block=True);
