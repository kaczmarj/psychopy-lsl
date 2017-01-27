"""Minimal example of how to send event triggers in PsychoPy with
LabStreamingLayer.

In this example, the words "hello" and "world" alternate on the screen, and
an event marker is sent with the appearance of each word.

TO RUN: open in PyschoPy Coder and press 'Run'. Or if you have the psychopy
Python package in your environment, run `python hello_world.py` in command line.

ID     EVENT
------------
1  --> hello
2  --> world
99 -->  test
------------
"""
from psychopy import core, visual, event
from pylsl import StreamInfo, StreamOutlet

def main():
    """Alternate printing 'Hello' and 'World' and send a trigger each time."""
    # Set up LabStreamingLayer stream.
    info = StreamInfo(name='example_stream', type='Markers', channel_count=1,
                      channel_format='int32', source_id='example_stream_001')
    outlet = StreamOutlet(info)  # Broadcast the stream.

    # This is not necessary but can be useful to keep track of markers and the
    # events they correspond to.
    markers = {
        'hello': [1],
        'world': [2],
        'test': [99],
    }

    # Send triggers to test communication.
    for _ in range(5):
        outlet.push_sample(markers['test'])
        core.wait(0.5)

    # Instantiate the PsychoPy window and stimuli.
    win = visual.Window([800, 600], allowGUI=False, monitor='testMonitor',
                        units='deg')
    hello = visual.TextStim(win, text="Hello")
    world = visual.TextStim(win, text="World")

    for i in range(10):
        if not i % 2:  # If i is even:
            hello.draw()
            # # Experiment with win.callOnFlip method. See Psychopy window docs.
            # win.callOnFlip(outlet.push_sample, markers['hello'])
            win.flip()
            outlet.push_sample(markers['hello'])
        else:
            world.draw()
            # win.callOnFlip(outlet.push_sample, markers['world'])
            win.flip()
            outlet.push_sample(markers['world'])
        if 'escape' in event.getKeys():  # Exit if user presses escape.
            break
        core.wait(1.0)  # Display text for 1.0 second.
        win.flip()
        core.wait(0.5)  # ISI of 0.5 seconds.

    win.close()
    core.quit()

if __name__ == "__main__":
    main()
