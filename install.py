from config import DBFILE
from tinydb import TinyDB
import uuid


if __name__ == '__main__':
    # 连接数据库
    db = TinyDB(DBFILE)

    # 创建 Head 表，存储一级导航
    head = db.table("Head")

    # 向表中添加数据
    head.insert_multiple([
            {"head_id": "1","head_name": "工作专区"},
            {"head_id": "2","head_name": "大数据专区"},
            {"head_id": "3","head_name": "PostgreSQL专区"},
            {"head_id": "4","head_name": "素材专区"},
            {"head_id": "99","head_name": "个人专区"}
        ])

    # 创建 Navigation 表，存储二级导航
    navigation = db.table("Navigation")

    # 向表中添加数据
    navigation.insert_multiple([
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "五分钟学大数据", 
                "abstract": "五分钟学大数据", 
                "url": "https://www.fivedata.cn/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Hadoop", 
                "abstract": "Hadoop", 
                "url": "https://hadoop.apache.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "ZooKeeper", 
                "abstract": "ZooKeeper", 
                "url": "https://zookeeper.apache.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Hive", 
                "abstract": "Hive", 
                "url": "https://hive.apache.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 1
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Kafka", 
                "abstract": "Kafka", 
                "url": "https://kafka.apache.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Hbase", 
                "abstract": "Hbase", 
                "url": "https://hbase.apache.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Flume", 
                "abstract": "Flume", 
                "url": "https://flume.apache.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Spark", 
                "abstract": "Spark", 
                "url": "https://spark.apache.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Flink", 
                "abstract": "Flink", 
                "url": "https://flink.apache.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "DolphinScheduler", 
                "abstract": "DolphinScheduler", 
                "url": "https://dolphinscheduler.apache.org/zh-cn/index.html", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Azkaban", 
                "abstract": "Azkaban", 
                "url": "https://azkaban.readthedocs.io/en/latest/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Kettle", 
                "abstract": "Kettle", 
                "url": "https://pentaho-community.atlassian.net/wiki/spaces/EAI/overview", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 1
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Kettle中文网", 
                "abstract": "Kettle中文网", 
                "url": "http://www.kettle.org.cn/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 1
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Pyecharts", 
                "abstract": "Pyecharts", 
                "url": "https://gallery.pyecharts.org/#/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": "2"
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "SeaTunnel", 
                "abstract": "SeaTunnel", 
                "url": "https://seatunnel.apache.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 1
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "SeaTunnel中文文档", 
                "abstract": "SeaTunnel中文文档", 
                "url": "https://interestinglab.github.io/seatunnel-docs/#/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Pigsty", 
                "abstract": "Pigsty", 
                "url": "https://pigsty.cc/zh/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "3", 
                "head_name": "PostgreSQL专区", 
                "access_count": 2
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "DataX", 
                "abstract": "DataX", 
                "url": "https://github.com/alibaba/DataX", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "DataX-Web", 
                "abstract": "DataX-Web", 
                "url": "https://github.com/WeiYe-Jing/datax-web", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Debezium", 
                "abstract": "Debezium", 
                "url": "https://debezium.io/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 1
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Postgrehub", 
                "abstract": "Postgrehub", 
                "url": "https://postgreshub.cn/index", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "3", 
                "head_name": "PostgreSQL专区", 
                "access_count": 1
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "PostgreSQL文档", 
                "abstract": "PostgreSQL文档", 
                "url": "http://www.postgres.cn/docs/14/index.html", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "3", 
                "head_name": "PostgreSQL专区", 
                "access_count": 2
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Greenplum源码", 
                "abstract": "Greenplum源码", 
                "url": "https://github.com/greenplum-db/gpdb", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "3", 
                "head_name": "PostgreSQL专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Greenplum官网", 
                "abstract": "Greenplum官网", 
                "url": "https://greenplum.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "3", 
                "head_name": "PostgreSQL专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "德哥Github", 
                "abstract": "德哥Github", 
                "url": "https://github.com/digoal", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "3", 
                "head_name": "PostgreSQL专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "盘古云课堂", 
                "abstract": "盘古云课堂", 
                "url": "http://www.pgedu.cn/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "3", 
                "head_name": "PostgreSQL专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "worldvectorlogo", 
                "abstract": "logo素材", 
                "url": "https://worldvectorlogo.com/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "4", 
                "head_name": "素材专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "60Logo", 
                "abstract": "logo素材", 
                "url": "https://www.60logo.com/list", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "4", 
                "head_name": "素材专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Gitee", 
                "abstract": "Gitee", 
                "url": "https://gitee.com/vleity", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "99", 
                "head_name": "个人专区", 
                "access_count": 4
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Github", 
                "abstract": "Github", 
                "url": "https://github.com/vleity", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "99", 
                "head_name": "个人专区", 
                "access_count": 1
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Delta Lake", 
                "abstract": "Build Lakehouses with Delta Lake", 
                "url": "https://delta.io/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Hudi", 
                "abstract": "Apache Hudi", 
                "url": "https://hudi.apache.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "Iceberg", 
                "abstract": "Apache Iceberg", 
                "url": "https://iceberg.apache.org/", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "2", 
                "head_name": "大数据专区", 
                "access_count": 0
            }, 
            {
                "id": str(uuid.uuid1()), 
                "nav_name": "EDB PG", 
                "abstract": "EDB Download PostgreSQL", 
                "url": "https://www.enterprisedb.com/software-downloads-postgres", 
                "photo": "static/images/pynavs.png", 
                "nav_type": "tag", 
                "head_id": "3", 
                "head_name": "PostgreSQL专区", 
                "access_count": 1
            }
        ])


    # 关闭连接
    db.close()



