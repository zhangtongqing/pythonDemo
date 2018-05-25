import json
from urllib import parse
parames ={
    "token":"33f0948f556846869f116b6abac7d76e", #用户token
    "userId":2276,  #用户ID
    "t":"pc"
}

keys, paras = sorted(parames), [];
print(keys)
print(paras)
paras = ['{}={}'.format(key, parames[key]) for key in keys if key != 'sign'];
stringA = '&'.join(paras)  #返回通过指定字符连接序列中元素后生成的新字符串。
stringSignTemp = stringA + '&sign='
print(stringSignTemp)
print(stringA)


# token=33f0948f556846869f116b6abac7d76e&userId=2276&t=pc
b = parse.urlencode(parames);
print(b)

str = "-";
seq = ("a", "b", "c"); # 字符串序列
print (str.join( seq ));


#用 & 链接数组元素
str = "&";
seq = ["a=1","b=2","c=3"]
print (str.join( seq ));

#循环字典
for key in parames.keys():
    print(parames[key])