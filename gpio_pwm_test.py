from periphery import PWM
import subprocess
import time

#need to run this with root privilege because of ldto enable/disable
def activate_pwm(pwm_name, pwm_chip_num):
    #you can get the pwm chip numbers in ldto list and:
    # https://hub.libre.computer/t/how-to-enable-and-control-pwm-on-aml-s905x-cc/243
    already_active = False
    for i in subprocess.getoutput('ldto status').split('\n'):
        if i == pwm_name:
            print(f"PWM name: {pwm_name} already set")
            already_active = True
    if not already_active:
        print(f"PWM name: {pwm_name} setting...")
        subprocess.getoutput(f'sudo ldto enable {pwm_name}')
        subprocess.getoutput(f'echo 1 > /sys/class/pwm/pwmchip{pwm_chip_num}/export')

def deactivate_pwm(pwm_name):
    already_active = False
    for i in subprocess.getoutput('ldto status').split('\n'):
        if i == pwm_name:
            print(f"PWM name: {pwm_name} set")
            already_active = True
    if already_active:
        print(f"PWM name: {pwm_name} disabling...")
        subprocess.getoutput(f'sudo ldto disable {pwm_name}')
    else:
        print(f"PWM name: {pwm_name} already not active")

def pwm_test(chip_num, pwm_num, period_ns=2400000, duty_cycle_ns=400000, step_ns=100000):
    pwm_here = PWM(0, 1)

    pwm_here.period_ns = period_ns
    pwm_here.duty_cycle_ns = duty_cycle_ns
    pwm_here.enable()
    i = duty_cycle_ns
    while i < period_ns:
        time.sleep(0.1)
        pwm_here.duty_cycle_ns = i
        i += step_ns
    while i >= duty_cycle_ns:
        time.sleep(0.1)
        pwm_here.duty_cycle_ns = i
        i -= step_ns
    pwm_here.close()

activate_pwm('pwm-ao-b-6', 1)
pwm_test(0, 1)
deactivate_pwm('pwm-ao-b-6')
