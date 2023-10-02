
def rejective(dice1, dice2):
    # (1,1)-(1,3) = 12  (1,4)-(3,3) = 13  (3,4)-(5,2) = 14 (5,3)-(6,3) = 15 (6,4)-(6,6) = 16
    map12 = tuple([(1, i) for i in range(1, 4)])
    map13 = tuple([(1, i) for i in range(4, 7)] + [(2, i) for i in range(1, 7)] + [(3, i) for i in range(1, 4)])
    map14 = tuple([(3, i) for i in range(4, 7)] + [(4, i) for i in range(1, 7)] + [(5, i) for i in range(1, 3)])
    map15 = tuple([(5, i) for i in range(3, 7)] + [(6, i) for i in range(1, 4)])
    map16 = tuple([(6, i) for i in range(4, 7)])

    # 创建映射关系字典
    mapping = {map12: 12, map13: 13, map14: 14, map15: 15, map16: 16}

    # 返回根据骰子点数查找到的映射值
    return mapping.get((dice1, dice2), None)

# 测试函数
result = rejective(1, 6)
print(result)  # 应该输出 16
