from machine import Pin
import time

txVcc = Pin(28, Pin.OUT)
txVcc.on()
tx = Pin(27, Pin.OUT)

rxVcc = Pin(8, Pin.OUT)
rxVcc.on()
rx = Pin(7, Pin.IN)


# Function to send a sequence of bits
def send_data(data):
    for bit in data:
        if bit == 1:
            tx.on()  # Turn on the transmitter
        else:
            tx.off()  # Turn off the transmitter
        time.sleep(1)
    tx.off()  # Ensure the transmitter is off after sending


def test(data):
    rxData = []
    for bit in data:
        if bit == 1:
            tx.on()  # Turn on the transmitter
        else:
            tx.off()  # Turn off the transmitter
        time.sleep(0.2)

        rxBit = rx.value()
        rxData.append(rxBit)
        print(rxBit)
        time.sleep(0.2)
    tx.off()  # Ensure the transmitter is off after sending
    return rxData


# Example: Send "1010"
while True:
    # send_data([1, 1, 0, 1, 0, 0])
    sent = [1, 1, 0, 1, 0, 0]
    received = test(sent)
    print(sent)
    print(received)
