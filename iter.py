parames ={
    "token":"33f0948f556846869f116b6abac7d76e", #用户token
    "userId":2276,  #用户ID
    "t":"pc"
}

keys, paras = sorted(parames), [];
paras = ['{}={}'.format(key, parames[key]) for key in keys if key != 'sign'];
stringA = '&'.join(paras)
stringSignTemp = stringA + '&sign='
print(stringSignTemp)