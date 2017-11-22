'''
[编程题] 有趣的数字
时间限制：1秒
空间限制：32768K
小Q今天在上厕所时想到了这个问题：有n个数，两两组成二元组，差最小的有多少对呢？差最大呢？


输入描述:

 输入包含多组测试数据。

 对于每组测试数据：

 N - 本组测试数据有n个数

 a1,a2...an - 需要计算的数据

 保证:

 1<=N<=100000,0<=ai<=INT_MAX.
  


输出描述:

对于每组数据，输出两个数，第一个数表示差最小的对数，第二个数表示差最大的对数。

输入例子1:
6
45 12 45 32 5 6

输出例子1:
1 2
'''

'''
解题思路：考虑细节
  拿到这道题目想了一会，马上得到了方案：
  首先，把序列排序，然后对相邻元素两两相减，在n-1个差值中找到最小差值，然后输出差值中有多少最小差值就是差最小的对数。
  其次，输出序列中最小数的个数和最大数的个数，把它们相乘就是差最大的对数。
  后来发现自己天真了，比如 2 2 2 2 这个序列，按照上述方法会输出 1， 16， 显然不对， 考虑到组合，应该输出 6， 6。
  新思路：
  首先判断序列里数字是否都相同，如果相同，直接输出 n*(n-1)//2， 
  如果不相同，则需要判断序列中有无重复元素，如果有重复元素，数出所有重复元素的个数same_count，算出它们same_count*(same_count-1)//2的和
  如果没有重复元素，则可以用上述求差最小的对数的方法求解
  差最大的对数仍可以用上述的方法
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

while True:
    try:
        n = int(input())
        nums = sorted([each for each in map(int, input().split())])
        if nums.count(nums[0]) == n:  # 列表中的所有数字都一样
            print(' '.join([str(n*(n-1)//2), str(n*(n-1)//2)]))
        else:  # 列表中有数字不一样
            same_count = 1
            same_count_list = []
            for i in range(n-1):
                if nums[i] == nums[i+1]:
                    same_count += 1
                else:
                    same_count_list.append(same_count)
                    same_count = 1
            if same_count > 1:
                same_count_list.append(same_count)
            combination = 0
            for each in same_count_list:
                if each > 1:
                    combination += each * (each-1) // 2
            if combination:
                minimum_count = combination
            else:
                diffs = [abs(nums[i] - nums[i+1]) for i in range(n-1)]
                minimum_count = diffs.count(min(diffs))
            maximum_count = nums.count(nums[0]) * nums.count(nums[n-1])

            print(' '.join([str(minimum_count), str(maximum_count)]))
    except:
        break
