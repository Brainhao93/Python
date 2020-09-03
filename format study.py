x = 'nice'
y = 'bute'
# output = 'hello' + x + ' ' + y
# output = 'hello,{} {}'.format(x,y)
output = 'hello, {1} {0}'.format(x,y)#注意0，1转换位置
# output =f'hello,{x} \n {y}'
print(output)
