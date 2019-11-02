import numpy as np


#   根据观测序列、发射概率、状态转移矩阵、发射概率
#   返回最佳路径
def compute(obs, states, start_p, trans_p, emit_p):
    #   max_p（3*2）每一列存储第一列不同隐状态的最大概率
    max_p = np.zeros((len(obs), len(states)))

    #   path（2*3）每一行存储上max_p对应列的路径
    path = np.zeros((len(states), len(obs)))

    #   初始化
    for i in range(len(states)):
        max_p[0][i] = start_p[i] * emit_p[i][obs[0]]
        path[i][0] = i

    for t in range(1, len(obs)):
        newpath = np.zeros((len(states), len(obs)))
        for y in range(len(states)):
            prob = -1
            for y0 in range(len(states)):
                nprob = max_p[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]]
                if nprob > prob:
                    prob = nprob
                    state = y0
                    #   记录路径
                    max_p[t][y] = prob
                    for m in range(t):
                        newpath[y][m] = path[state][m]
                    newpath[y][t] = y

        path = newpath

    max_prob = -1
    path_state = 0
    #   返回最大概率的路径
    for y in range(len(states)):
        if max_p[len(obs)-1][y] > max_prob:
            max_prob = max_p[len(obs)-1][y]
            path_state = y

    return path[path_state]

