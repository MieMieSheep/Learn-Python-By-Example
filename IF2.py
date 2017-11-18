#encoding:utf-8
#!/user/bin/python

'''
流程控制
if语句 2

 @AUTHOR: JAYDENCHAN
 @MAIL: 2564845837@QQ.COM

'''

#input - 用于等待用户输入数据 并且将数据赋值到 等号左边的变量中，默认接受的数据为str类型
#float() - 把原本的 str类型 转换为 float类型数据 ， 方便待会的数字比较
inputNumber = float(input('请输入一个数字(Please enter a number)：'))


'''
猜数字 简单程序
'''

if inputNumber == 50:
    print('恭喜你猜对了')  
elif inputNumber > 50:
    print('输入的数字有点大。')
else:
    print('输入的数字有点小.')  