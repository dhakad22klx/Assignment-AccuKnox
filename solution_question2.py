# Yes, Django signals runs in same thread as the caller.Code below showcase this : 

import threading
from django.dispatch import Signal, receiver

my_signal = Signal()

@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name} (ID: {threading.get_ident()})")

def send_signal():
    print(f"Sending signal from thread: {threading.current_thread().name} (ID: {threading.get_ident()})")
    my_signal.send(sender=None) 

thread = threading.Thread(target=send_signal, name='SignalSenderThread')
thread.start()  
thread.join() 


print(f"Back in main thread: {threading.current_thread().name} (ID: {threading.get_ident()})")
