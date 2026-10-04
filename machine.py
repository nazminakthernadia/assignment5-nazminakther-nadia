from machine import Pin, PWM
from time import sleep

# Motor A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# PWM frequency
e1.freq(1000)
e2.freq(1000)


def stop():
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(0.5)


def move_forward(t):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(32767)
    e2.duty_u16(32767)
    sleep(t)
    stop()


def reverse(t):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(32767)
    e2.duty_u16(32767)
    sleep(t)
    stop()


def turn_left(t):
    m1.value(0)
    m2.value(1)
    e1.duty_u16(32767)
    e2.duty_u16(32767)
    sleep(t)
    stop()


def turn_right(t):
    m1.value(1)
    m2.value(0)
    e1.duty_u16(32767)
    e2.duty_u16(32767)
    sleep(t)
    stop()


# Wait 2 seconds before starting
sleep(2)

# Read the route from file and follow it
with open("route.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        command, value = line.split()
        t = float(value)

        if command == "FORWARD":
            move_forward(t)
        elif command == "REVERSE":
            reverse(t)
        elif command == "LEFT":
            turn_left(t)
        elif command == "RIGHT":
            turn_right(t)