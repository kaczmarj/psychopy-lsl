LSL, PsychoPy, and Enobio
=========================

The LabStreamingLayer GitHub can be found at https://github.com/sccn/labstreaminglayer

 Included in this repository is an example PsychoPy script demonstrating the use of LabStreamingLayer to send triggers.

Install LabStreamingLayer
-------------------------
1. Go to ftp://sccn.ucsd.edu/pub/software/LSL/SDK/ for the latest release or to [GitHub](https://github.com/sccn/labstreaminglayer) for the most recent version.
2. Download the most recent Python API.
3. Extract the zip file.
4. In a terminal, run `python setup.py install` to install the LabStreamingLayer Python package.

If you try `import pylsl` at this point, you will likely receive an error. Depending on your operating system, you must include the following files in the pylsl directory of Python (the error message should tell you exactly where). You can find these files on ftp://sccn.ucsd.edu/pub/software/LSL/SDK/ in any of the Python distros.
- Windows: liblsl32.dll or liblsl64.dll
- Mac OS X: liblsl32.dylib or libilsl64.dylib
- Linux: liblsl32.so or liblsl64.so

_Now_ you should be able to run `import pylsl` successfully.


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
![Screenshot of Coregui software](coregui_screenshot.png?raw=true "Coregui Software")
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
