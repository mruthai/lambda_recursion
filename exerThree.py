
# Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...


# double_num = list(map(lambda x,y: (((x * 2) - 1),((y * 2) - 1)) if x > 0 and y > 0 else (x,y), numbers,more_nums))
# print(double_num)

# output = [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
# print(type(output))

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

 


city, particles = map(list, zip(*places))



change_temp=list(map(lambda city, particles : (city, float(particles) * (9/5) + float(32)), city,particles))

print(change_temp)


# def c_f(new_temp):
#     b = []
#     for b in output:
#         b.append(new_temp)

# print(c_f(b))

