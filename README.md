# PsychoPy event markers with LabStreamingLayer

This repository demonstrates how to send event markers in PsychoPy with [LabStreamingLayer](https://github.com/sccn/labstreaminglayer) (LSL).

See [coregui.md](/coregui.md) to learn how to receive markers in Coregui with LSL.

Example scripts
---------------

- [`example_coder.py`](/example_coder.py) is a minimal PsychoPy "experiment". Two words alternate on the screen, and a marker is sent whenever a word appears. This was coded manually.
- [`example_builder.py`](/example_builder.py) behaves in the same way as `example_coder.py`, but it was created in the builder and uses stimuli and markers defined in `example_builder.csv`


General steps
-------------

1. Install `pylsl` (the Python interface of LSL).
1. Include code in your Python script to send markers.


Install LabStreamingLayer
-------------------------

See the [PyPI page](https://pypi.python.org/pypi/pylsl).

```
pip install pylsl
```


In your PsychoPy code
---------------------

Refer to [pylsl.py](https://github.com/labstreaminglayer/liblsl-Python/blob/master/pylsl/pylsl.py) for documentation on `pylsl` functions.

```python
# ...
from pylsl import StreamInfo, StreamOutlet
info = StreamInfo(name='my_stream_name', type='Markers', channel_count=1,
                  channel_format='int32', source_id='uniqueid12345')
# Initialize the stream.
outlet = StreamOutlet(info)
# ...
```
- Include markers wherever you need them.
```python
# ...
outlet.push_sample(x=[100])
# ...
```
- The example above sends a marker 100. `x` must be a list with a length equal to `channel_count` (specified in `StreamInfo`). It is easiest to use integers as markers.
- You can also include dynamic marker names (see [example script](/example_builder.py)). If you are using a trial loop in PsychoPy, include marker values in a column in the spreadsheet used for the loop. If the column header is "marker", the code would be `outlet.push_sample(x=[marker])`.
