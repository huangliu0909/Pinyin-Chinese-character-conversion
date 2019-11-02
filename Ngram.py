def get2grams(input):
    output = {}
    for i in range(len(input) - 1):
        tempfirst = input[i]
        tempend = input[i+1]
        if tempfirst not in output:
            output[tempfirst] = {}
        if tempend not in output[tempfirst]:
            output[tempfirst][tempend] = 0
        output[tempfirst][tempend] += 1
    for k in output:
        sum = 0
        for kk in output[k]:
            sum += output[k][kk]
        for kk in output[k]:
            output[k][kk] /= sum
    return output


