def learn(input):
    # 输入数组，元素是字，按文件顺序

    pi = {}
    # 初始概率
    a = {}
    # 转移概率
    all = []

    for i in range(len(input) - 1):
        if i == 0:
            pi[input[i]] = 1
        if input[i] not in a:
            a[input[i]] = {}
            all.append(input[i])
        if input[i + 1] not in a[input[i]]:
            a[input[i]][input[i + 1]] = 0
        a[input[i]][input[i + 1]] += 1
    for k in a:
        sum = 0
        for kk in a[k]:
            sum += a[k][kk]
        for kk in a[k]:
            a[k][kk] /= sum
    return a, pi, all


'''
a, pi, states_sum = learn(["我", "喜", "欢", "你", "呀", "我", "爱", "你"])
print(a)
print(pi)
print(states_sum)
'''
