# 정수
output_a = "{:d}".format(52)

#특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(-52)

#빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)

print("#특정 칸에 출력하기")
print(output_b)
print(output_c)

print("#빈칸을 0으로 채우기")
print(output_d)
print(output_e)

#기호와 함께 출력하기
output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)

#조합 하기
output_f = "{:+5d}".format(52)
output_g = "{:+5d}".format(-52)

print("#조합하기")
print(output_f)
print(output_g)

output_f = "{:=+5d}".format(52)
output_g = "{:=+5d}".format(-52)

print(output_f)
print(output_g)

output_f = "{:+05d}".format(52)
output_g = "{:+05d}".format(-52)

print(output_f)
print(output_g)
