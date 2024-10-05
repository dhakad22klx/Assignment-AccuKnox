""" 
By default, Signals in Django  works in synchronous mode.
To make it asynchronous, we need to use the asgiref library.

"""

# Here is the simple implementaton 

import time
from django.dispatch import Signal, receiver

# Creating an instance of custom signal
my_signal = Signal()

# defining a signal receiver
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler started")
    # Simulate some work with a delay
    time.sleep(2)
    print("Signal handler finished")

# Function for sending the signal
def send_signal():
    print("Sending signal...")
    my_signal.send(sender=None)
    print("Signal sent!")



send_signal()
