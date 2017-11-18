#!/user/bin/python
#encoding:UTF-8

'''
python 控制流程
if语句 3
 @author jaydenchan
 @mail:2564845837@qq.com

'''

real_username = '2564845837@qq.com'
real_passwd = '123321'

input_username = input('请输入你的账号(Please enter your username ) :')
input_passwd = input('请输入你的密码(Please enter your password) :')

#这里or 的作用是 当input_username == '' 或者 input_passwd == '' 其中一条表达式返回True时
#那么整条表达式都返回 True
if input_username == '' or input_passwd == '':
    print('账号或者密码不可为空')

# 这里and关键字的作用是 当input_username == real_username
# 和 input_passwd == real_passwd 两条表达式 都为True时
# input_username == real_username and input_passwd == real_passwd 这条表达式才为True
# 如果有一条表达式为 False 那么整条表达式最终返回 False
elif input_username == real_username and input_passwd == real_passwd:
    print('账号密码正确\n登录成功')

else:
    print('账号或者密码错误')



