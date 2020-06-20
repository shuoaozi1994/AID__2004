# 2. 假设有100层的阶梯，给你两个完全一样的鸡蛋，
# 请设计一种方法，能够试出从第几层阶梯开始往下仍鸡蛋鸡蛋会碎

# 5层  2个鸡蛋
# dp = [
#     [0,0,0,0,0,0]  #0个鸡蛋
#     [0,1,2,3,4,5]  #1个鸡蛋
#     [0,0,0,0,0,0]  #2个鸡蛋
# ]
# i 鸡蛋个数 step次数   dp[i][step]
# 当第step次扔鸡蛋时  鸡蛋破了  i+1 step+1
#   能确定 dp[i-1][step-1]层 (向下)
# 当第step次扔鸡蛋时  鸡蛋没破  i不变 step+1
#   能确定 dp[i][step-1]层 (向上)
# 当前还有1层
# dp[i][step] = dp[i-1][step-1]+dp[i][step-1]+1

def super_egg_drop(k, n):
    '''
    :param k: 鸡蛋个数
    :param n: 楼梯层数
    :return: 乐观估计 最少需要多少次能求出鸡蛋摔碎的层数
    '''
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    print(dp)
    for i in range(1, k + 1):
        for step in range(1, n + 1):
            dp[i][step] = dp[i - 1][step - 1] + dp[i][step - 1] + 1
            print(dp)
            if dp[k][step] >= n:
                return step


res = super_egg_drop(2, 5)
print(res)