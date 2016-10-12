LSL, PsychoPy, and Enobio
=========================

The LabStreamingLayer GitHub can be found at https://github.com/sccn/labstreaminglayer

 Included in this repository is an example PsychoPy script demonstrating the use of LabStreamingLayer to send triggers.

Download LabStreamingLayer
--------------------------
1. Go to ftp://sccn.ucsd.edu/pub/software/LSL/SDK/
2. Download the most recent Python API.

You must include the following files in the same directory as your PsychoPy experiment:
- pylsl.py and \_\_init\_\_.py
- Windows: liblsl32.dll OR liblsl64.dll
- Mac OS X: liblsl32.dylib OR libilsl64.dylib
- Linux: liblsl32.so OR liblsl64.so


In your PsychoPy Code
---------------------

Refer to pylsl.py for documentation of the following functions.

```python
# ... other import statements above
from pylsl import StreamInfo, StreamOutlet
# Enter stream info
info = StreamInfo(name='trigger_name', type='Markers', channel_count=1,
                  channel_format='int32', source_id='<source_id>')
# Initialize stream
outlet = StreamOutlet(info)
# ...
```
- Include triggers wherever you need them.
```python
# ...
outlet.push_sample(x=[100])
# ...
```
  - In the example above, 100 is the name of the trigger. It is easiest to use integers as trigger names. The length of x must be equal to `channel_count`, specified in `StreamInfo()`.
  - You can also include dynamic trigger names. If you are using a trial loop in PsychoPy, include your trigger values in a column in the spreadsheet you use for the loop. If the column header is "trigger", the code would be `outlet.push_sample(x=[trigger])`.


Getting Enobio software to record LSL triggers
----------------------------------------------
1. Open Coregui and connect your EEG device.
2. Navigate to EEG Setup > Settings.
3. In "Markers from Lab Streaming Layer 1" enter the name of your marker stream. This is the `name` parameter of `StreamInfo()`.
![Alt text](https://github.mit.edu/storage/user/6987/files/5ca30998-8596-11e6-90c9-adf3c1f8217c "Coregui Software")
4. When the stream is active and when Coregui is connected to it, the bar next to "Markers from Lab Streaming Layer 1" will turn yellow. Everytime a marker is received, this bar will turn green.
5. If you are curious about "Outlet for Lab Streaming Layer," stay tuned for another GitHub repository! That textbox gives a name to an LSL stream of the raw EEG values from Coregui. This is useful if you want to stream EEG data into Python, say, for a brain-computer interface!


Verifying communication between LSL and Coregui
-----------------------------------------------
If you are running your PsychoPy experiment fullscreen (which you should, because it improves framerate) on the same computer as you are running Coregui, it will not be possible to verify that Coregui is recording the triggers in your experiment. To get around this issue, I like to setup LSL immediately after the `import` statements in the experiment code and send a few triggers before the PsychoPy dialog opens. Using the code below, you would enter "test_stream" in "Markers from Lab Streaming Layer 1."

```python 
# ...
from pylsl import StreamInfo, StreamOutlet
info = StreamInfo(name='test_stream', type='Markers', channel_count=1,
		  channel_format='int32', source_id='test_stream_001')
outlet = StreamOutlet(info)  # initialize the stream

# MARKER--> DESCRIPTION
# 1     --> testing communication
# 2     --> description of marker 2
# 3     --> description of marker 3

# Send a few triggers to test communication.
print("Sending triggers...")
for count in range(5):
	outlet.push_sample(x=[1])
	core.wait(0.5)
# ...
```
