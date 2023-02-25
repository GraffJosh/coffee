import bcd


weight_ones = bcd.BCD(pin_bit_1=22, pin_bit_2=27, pin_bit_4=17, pin_bit_8=4)
weight_tens = bcd.BCD(pin_bit_1=25, pin_bit_2=8, pin_bit_4=7, pin_bit_8=1)


temp_ones = bcd.BCD(pin_bit_1=12, pin_bit_2=16, pin_bit_4=20, pin_bit_8=21)
temp_tens = bcd.BCD(pin_bit_1=14, pin_bit_2=15, pin_bit_4=24, pin_bit_8=23)
temp_hundreds = bcd.BCD(pin_bit_1=26, pin_bit_2=19, pin_bit_4=13, pin_bit_8=6)
print("Weight Selection: ", weight_tens.value(), weight_ones.value())
print("Temp Selection: ", temp_hundreds.value(), temp_tens.value(), temp_ones.value())
