# 1. 给你一个长度为n的数组，其中只有一个数字出现大于n/2次，问如何快速找到这个数字
# 求众数

def m_element(num_list):
    return sorted(num_list)[len(num_list)//2]

print(m_element([1,1,2,2,2,2]))

# def m_element(num_list):
#     for i in num_list:
#         num_list.count(i)
#             ...



# def m_element(num_list):
#     #{2:4,1:2}
#     num_dic = {}
#     for i in num_list:
#         if i in num_dic:
#             num_dic[i] += 1
#             if num_dic[i] > ((len(num_list) + 1) // 2):
#                 return i
#         else:
#             num_dic[i] = 1
#
#
# res = m_element([2,2,1,1,2,2])
# print(res)