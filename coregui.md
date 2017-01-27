# Receiving LSL markers in Coregui

This page demonstrates how to receive markers in Coregui from LSL. See [this page](/README.md) to learn how to stream event markers in Python using LSL.


Connect LSL stream to Coregui
-----------------------------

1. Open Coregui and connect your EEG device.
1. Navigate to EEG Setup > Settings.
1. In "Markers from Lab Streaming Layer 1" enter the name of your marker stream (`name` argument of `StreamInfo()`).
![Screenshot of Coregui software](/images/coregui_screenshot.png?raw=true "Screenshot of Coregui Software")
1. When the stream is active and Coregui is connected to it, the bar next to "Markers from Lab Streaming Layer 1" will turn yellow. Every time a marker is received, this bar will flash green.


Note: "Outlet for Lab Streaming Layer" allows a user to stream the _EEG data_ via LSL. The user can connect to this stream (with `pylsl.StreamInlet`) to access the EEG data in real-time. See this [GitHub repo](https://github.com/kaczmarj/rteeg).


Verifying communication between LSL and Coregui
-----------------------------------------------

If you are running your PsychoPy experiment fullscreen (which you should, because it improves framerate) on the same computer as you are running Coregui, it will be difficult to verify that Coregui is recording the markers in your experiment. To get around this issue, I like to set up LSL immediately after the `import` statements in the experiment code and send a few markers before the PsychoPy dialog opens.

```python
# ... other import statements above
from pylsl import StreamInfo, StreamOutlet
info = StreamInfo(name='test_stream', type='Markers', channel_count=1,
		  channel_format='int32', source_id='test_stream_001')
outlet = StreamOutlet(info)

# MARKER--> DESCRIPTION
# 1     --> testing communication
# 2     --> description of marker 2
# 3     --> description of marker 3

# Send a few markers to test communication.
print("Sending markers...")
for _ in range(5):
	outlet.push_sample(x=[1])
	core.wait(0.5)  # ``psychopy.core``
# ...
```
