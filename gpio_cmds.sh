# shows the gpiochip number and the line numbers and their pin names.
# This can match up with:
# https://docs.google.com/spreadsheets/d/1U3z0Gb8HUEfCIMkvqzmhMpJfzRqjPXq7mFLC-hvbKlE/edit#gid=0
gpioinfo

# get the input with setting the input to be a pullup resistor and active low
gpioget -B pull-up -l 1 92
