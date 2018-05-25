import time;

timestr = time.time();
print(timestr); #时间戳

format1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());  #格式化字符串  2018-05-23 17:11:17
format2 = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime());  #格式化字符串  Wed May 23 17:11:17 2018
var1 = "Wed May 23 17:11:17 2018";
format3 = time.mktime(time.strptime(var1,"%a %b %d %H:%M:%S %Y"))
print(format1);
print(format2);
print(format3);
