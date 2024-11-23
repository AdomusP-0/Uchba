num_str = 125
print(type(num_str))

numstr = str(num_str)
print(type(numstr))

message = 'Hi, my name is Python!'
print(message)

message = message.replace('i', '1').replace('y', '0')
print(message)

split_test = 'This is split test'
print(split_test)

split_test = split_test.split()
print(split_test)

string_join = ' '.join(split_test)
print(string_join)

print(len(string_join))