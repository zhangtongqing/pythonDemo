import hashlib
from urllib import parse


privateKey = "ABCDEFG$";
# 获取MD5
def MD5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

# 获取签名
def getSign(url,parames,body):
    keys, paras = sorted(parames), [];
    paras = ['{}={}'.format(key, parames[key]) for key in keys if key != 'sign'];
    stringA = '&'.join(paras)
    stringSignTemp = stringA + '&sign='
    url = url+"?";
    body = urlEncode(body)
    url += stringSignTemp + body + privateKey;
    sign = MD5(url);
    return sign

def urlEncode(body):
    body = str(body); #对象转string
    body = parse.quote(body,"UTF-8");#编码
    body = body \
        .replace("%3D", "=")\
    .replace("%2F", "/")\
    .replace("%2C", ",")\
    .replace("%3A", ":")\
    .replace("%27", "'")\
    .replace("%26", "&")\
    .replace("%7E", "~")\
    .replace("%28", "(")\
    .replace("%24", "$")\
    .replace("%29", ")")\
    .replace("%27", "'")\
    .replace("%21", "!")\
    .replace("%23", "#")\
    .replace("%3B", ";")\
    .replace("%40", "@")\
    .replace("%2B", "+")\
    .replace("+", "%20")\
    .replace("%3F", "?") \
    .replace("'", "%22");#加的
    return body
