import mne
import os
import defusedxml


# Make sure your MFF folder ends with `.mff`
mff_dir = 'AB_20160923_024726.mff'  # Replace with your renamed folder path

# Load using generic loader (auto-detects MFF)
raw = mne.io.read_raw(mff_dir, preload=True)

# View info
print(raw.info)

# Check channel names and types
print("Channel names:", raw.ch_names)
print("Channel types:", raw.get_channel_types())

# Handle the 'Vertex Reference' channel before setting montage
# Option 1: Set it as a reference channel (not EEG)
# if 'Vertex Reference' in raw.ch_names:
#     raw.set_channel_types({'Vertex Reference': 'misc'})
#     print("Set 'Vertex Reference' as misc channel type")

# # Optionally, set montage (now it should work)
# raw.set_montage('GSN-HydroCel-32', on_missing='warn')

# # Extract events
# events, event_id = mne.events_from_annotations(raw)
# print("Event mapping:", event_id)

# Plot raw signal with event markers
# raw.plot(events=events, title='EEG with events', block=True)
raw.plot(title='EEG Signal', block=True)
