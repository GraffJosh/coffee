import bcd


weight_ones = bcd.BCD(7, 23, 24, 25, 8)
weight_tens = bcd.BCD(1, 23, 24, 25, 8)


temp_ones = bcd.BCD(12, 23, 24, 25, 8)
temp_tens = bcd.BCD(16, 23, 24, 25, 8)
temp_hundreds = bcd.BCD(20, 23, 24, 25, 8)
print("current value: ", weight_tens.value(), weight_ones.value())
