import bcd


weight_ones = bcd.BCD(22, 27, 17, 4)
weight_tens = bcd.BCD(25, 8, 7, 1)


temp_ones = bcd.BCD(12, 16, 20, 21)
temp_tens = bcd.BCD(14, 15, 23, 24)
temp_hundreds = bcd.BCD(26, 19, 13, 6)
print("Weight Selection: ", weight_tens.value(), weight_ones.value())
print("Temp Selection: ", temp_hundreds.value(), temp_tens.value(), temp_ones.value())
