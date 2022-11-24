from config import DBFILE
from tinydb import TinyDB
import uuid
import argparse
import pandas as pd

"""
python add_head.py --id xx --name xxx
"""

if __name__ == '__main__':
    # 参数解析
    parser = argparse.ArgumentParser(description='Add head')
    parser.add_argument('--id', type=str, default='0', help="head_id")
    parser.add_argument('--name', type=str, default='', help="head_name")
    args = parser.parse_args()
    head_id = args.id
    head_name = args.name
    
    # 连接数据库
    db = TinyDB(DBFILE)
    head = db.table("Head")
    data = pd.DataFrame(data=head.all())
    ids = list(data['head_id'])
    if head_id in ids:
        print('id={} is already exists'.format(head_id))
        exit
    else:
        # 向表中添加数据
        head.insert_multiple([{"head_id": head_id,"head_name": head_name}])

    # 关闭连接
    db.close()



