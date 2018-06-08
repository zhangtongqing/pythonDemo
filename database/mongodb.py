from pymongo import MongoClient

conn = MongoClient('211.159.153.228', 27017)
db = conn.runoob    #连接runoob数据库，没有则自动创建
my_set = db.test_set #使用test_set集合，没有则自动创建

#添加多条数据到集合中
def add():
    print("...插入数据")
    users=[{"name":"Andy.zhang","age":18},{"name":"mongodb","age":20}]
    my_set.insert(users)

def get():
    print("......查询数据")
    for i in my_set.find():
        print(i)
    #查询name=zhangsan的
    for i in my_set.find({"name":"Andy.zhang"}):
        print("条件查询：",i)
    print("查询一个：",my_set.find_one({"name":"mongodb"}))

def getByid():
    """根据ID查询"""
    id = my_set.find_one({"name": "mongodb"})["_id"]
    print("id:",id)


def deleteById():
    """根据ID删除"""
    id = my_set.find_one({"name": "mongodb"})["_id"]
    my_set.remove(id);
if __name__ == '__main__':
    get();
    getByid();