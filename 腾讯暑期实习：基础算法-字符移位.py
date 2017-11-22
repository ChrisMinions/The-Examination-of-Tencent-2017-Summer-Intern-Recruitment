'''
[编程题] 算法基础-字符移位
时间限制：1秒
空间限制：32768K
小Q最近遇到了一个难题：把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。
你能帮帮小Q吗？


输入描述:

输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.
  


输出描述:

对于每组数据，输出移位后的字符串。

输入例子1:
AkleBiCeilD

输出例子1:
kleieilABCD
'''

'''
解题思路：偷鸡 或 利用filter
  偷鸡：
    遍历两次字符串，第一次先输出小写字母，第二次输出大写字母，不需要申请额外空间
  利用filter：
    利用filter过滤出小写字母和大写字母，把它们重新组合后放入元字符串的位置，其实还是申请了额外的空间的，
    不过python内置的函数内存回收机制会把定时清理这些额外空间
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

# 方法一：偷鸡
# while True:
#     try:
#         string = input()
#
#         for each in string:
#             if each.islower():
#                 print(each, end='')
#
#         for each in string:
#             if each.isupper():
#                 print(each, end='')
#         print()
#     except:
#         break

# 方法一：利用filter
while True:
    try:
        string = input()
        string = ''.join(filter(lambda k: k if k.islower() else '', string)) + ''.join(filter(lambda k: k if k.isupper() else '', string))
        print(string)
    except:
        break