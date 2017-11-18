#encoding:utf-8
#!/user/bin/python

'''

python 控制流程 
if语句 1

 @Author ：JAYDENCHAN
 @github : https://github.com/MoseChan

 @MAIL : jaydenchan.work@gmail.com
         or
         2564845837@qq.com

'''

num1 = 10
num2 = 20
num3 = 30


'''
如果 num1 = num2
输出num1 == num2

如果 num1 = num3
输出num1 == num3

不能满足以上两个条件任意一个
则执行 else 的代码块
即为 $ print("num1 = ",num1)

'''
if num1 == num2:
    print('num1 == num2')
elif num1 == num3:
    print('num1 == num3')
else:
    print("num1 = ",num1)


'''自己可以尝试修改一下变量的数值'''