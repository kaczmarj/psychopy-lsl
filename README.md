Event markers with Enobio EEG caps
==================================

Included in this repository is an example PsychoPy script demonstrating the use of the Python interface of the Lab Streaming Layer (LSL) to send event markers with Enobio EEG caps.


General steps
-------------

1. Install `pylsl` (the Python interface of LSL).
1. Include code in your Python script to send markers.
1. Connect the LSL stream to Coregui.


Install LabStreamingLayer
-------------------------

See the [PyPi page](https://pypi.python.org/pypi/pylsl).

```
pip install pylsl
```


In your PsychoPy code
---------------------

Refer to [pylsl.py](https://github.com/sccn/labstreaminglayer/blob/master/LSL/liblsl-Python/pylsl/pylsl.py) for documentation on the following functions.

```python
# ...
from pylsl import StreamInfo, StreamOutlet
info = StreamInfo(name='my_stream_name', type='Markers', channel_count=1,
                  channel_format='int32', source_id='uniqueid12345')
# Initialize the stream.
outlet = StreamOutlet(info)
# ...
```
- Include triggers wherever you need them.
```python
# ...
outlet.push_sample(x=[100])
# ...
```
- In the example above, 100 is the name of the trigger. `x` must be a list with a length equal to `channel_count` (specified in `StreamInfo`). It is easiest to use integers as trigger names.
- You can also include dynamic trigger names. If you are using a trial loop in PsychoPy, include your trigger values in a column in the spreadsheet you use for the loop. If the column header is "trigger", the code would be `outlet.push_sample(x=[trigger])`.


Connect LSL stream to Coregui
-----------------------------

1. Open Coregui and connect your EEG device.
1. Navigate to EEG Setup > Settings.
1. In "Markers from Lab Streaming Layer 1" enter the name of your marker stream (`name` argument of `StreamInfo()`).
![Screenshot of Coregui software](coregui_screenshot.png?raw=true "Coregui Software")
1. When the stream is active and when Coregui is connected to it, the bar next to "Markers from Lab Streaming Layer 1" will turn yellow. Everytime a marker is received, this bar will flash green.


Note: "Outlet for Lab Streaming Layer" allows you to specify a name for a LSL stream of EEG data. The user can connect to this stream (with `pylsl.StreamInlet`) to access the EEG data in real-time. See this [GitHub repo](https://github.com/kaczmarj/rteeg).


Verifying communication between LSL and Coregui
-----------------------------------------------

If you are running your PsychoPy experiment fullscreen (which you should, because it improves framerate) on the same computer as you are running Coregui, it will not be possible to verify that Coregui is recording the triggers in your experiment. To get around this issue, I like to setup LSL immediately after the `import` statements in the experiment code and send a few triggers before the PsychoPy dialog opens. In the case of the code below, you would enter "test_stream" in "Markers from Lab Streaming Layer 1."

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

# Send a few triggers to test communication.
print("Sending triggers...")
for _ in range(5):
	outlet.push_sample(x=[1])
	core.wait(0.5)
# ...
```
