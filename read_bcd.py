import temperature
import input_value
import relay


weight_pins = [[22, 27, 17, 4], [25, 8, 7, 1]]
temp_pins = [
    [12, 16, 20, 21],
    [14, 15, 24, 23],
    [26, 19],
]

weight_setting = input_value.InputValue(weight_pins)
temp_setting = input_value.InputValue(temp_pins)

curr_temp = temperature.Temperature()

heating_element = relay.Relay(6)

while True:
    if weight_setting.value() > 5:
        heating_element.on()
    else:
        heating_element.off()

    print("Weight Selection: ", weight_setting.value())
    print("Temp Selection: ", temp_setting.value())
    print("temperature: ", curr_temp.value())
    print("Heating Element: ", heating_element.status())
