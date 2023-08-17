import gpiod
import sys

if __name__ == '__main__':
    button_pin = 92
    chip_num = 1
    with gpiod.Chip('gpiochip'+str(chip_num)) as chip:
      lines = chip.get_line(button_pin)
      #request locks the gpio pin for this program. To let go of it do lines.release()
      lines.request(consumer=sys.argv[0], type=gpiod.LINE_REQ_DIR_IN, flags=gpiod.LINE_REQ_FLAG_BIAS_PULL_UP | gpiod.LINE_REQ_FLAG_ACTIVE_LOW)
     #lines.set_config(gpiod.LINE_REQ_DIR_IN, lines.BIAS_PULL_UP) 
      val = lines.get_value()
      print(val)
      print(lines.bias())
      print(lines.active_state())


