import bcd


weight_ones = bcd.BCD(22, 27, 17, 4)
weight_tens = bcd.BCD(25, 8, 7, 1)


temp_ones = bcd.BCD(12, 16, 20, 21)
temp_tens = bcd.BCD(0, 5, 24, 23)
temp_hundreds = bcd.BCD(26, 19, 13, 6)
print("current value: ", weight_tens.value(), weight_ones.value())
