'''
[编程题] 构造回文
时间限制：1秒
空间限制：32768K
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。

输入描述:

输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.
  


输出描述:

对于每组数据，输出一个整数，代表最少需要删除的字符个数。

输入例子1:
abcda
google

输出例子1:
2
2
'''

'''
解题思路：动态规划检测最长公共子序列
  这道题的本质是找出该字符串和该字符串的逆序字符串的最长公共子序列的长度。
  我们用string表示该字符串，用string_reverse表示它的逆序字符串。
  用dp[i][j]表示该字符串前i个字符和逆序字符串前j个字符的最长公共子序列的长度。
  更新公式：
        如果string[i] == string_reverse[j]：dp[i][j+1] = dp[i-1][j] + 1
        如果string[i] != string_reverse[j]：max(dp[i][j], dp[i-1][j+1])
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

while True:
    try:
        string = input().strip()
        string_reverse = string[::-1]

        length = len(string)
        dp = [0] * (length + 1)

        for i in range(length):
            dp_new = [0] * (length + 1)
            for j in range(length):
                if string[i] == string_reverse[j]:
                    dp_new[j+1] = dp[j] + 1
                else:
                    dp_new[j+1] = max(dp_new[j], dp[j+1])
            dp = dp_new

        print(length - dp[length])
    except:
        break
