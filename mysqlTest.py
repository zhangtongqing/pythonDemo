import pymysql

# 打开数据库连接
db = pymysql.connect("211.159.153.228","dev","dev123","running",charset='utf8');

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 查询语句
sql = "select t.user_id ,t.username, t.`password`, t.nick_name, t.token from t_user t limit 5";
try:
    cursor.execute(sql);
    results = cursor.fetchall();
    for row in results:
        userid = row[0]
        username = row[1]
        password = row[2]
        nickname = row[3]
        token = row[4]

        print("userId=%s,userName=%s,password=%s,nickName=%s,token=%s",userid,username,password,nickname,token);
except:
    print("获取数据异常...");

# 关闭数据库连接
db.close();