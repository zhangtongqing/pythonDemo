#list列表中的值，可以修改
#元中的值不能修改 但是可以连接组合


list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]; #列表
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 );#元组
dict  =  { 'key1': 456,"key2":"value2" }; #字典

print(list);
print(tuple);
print(dict);
print("**************");
print(list[0]);
print("列表截取：",list[0:3]);

print(tuple[0]);
print("元组截取：",list[0:3]);

print("获取字典元素：",dict["key1"]);



