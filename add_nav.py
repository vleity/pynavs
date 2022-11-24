from config import DBFILE
from tinydb import TinyDB
import uuid
import argparse
import pandas as pd

"""
python add_nav.py --name xxx --abstract xx --url xx --photo static/images/pynavs.png --type tag --head_id 99
"""

if __name__ == '__main__':
    # 参数解析
    parser = argparse.ArgumentParser(description='Add head')
    parser.add_argument('--name', type=str, default='', help="nav_name")
    parser.add_argument('--abstract', type=str, default='', help="abstract")
    parser.add_argument('--url', type=str, default='', help="url")
    parser.add_argument('--photo', type=str, default='static/images/pynavs.png', help="photo")
    parser.add_argument('--type', type=str, default='tag', help="type: tag image")
    parser.add_argument('--head_id', type=str, default='99', help="head_id from Head")
    
    args = parser.parse_args()
    nav_id = str(uuid.uuid1())
    nav_name = args.name
    nav_abstract = args.abstract
    nav_url = args.url
    nav_photo = args.photo
    nav_type = args.type
    nav_head_id = args.head_id
    
    # 连接数据库
    db = TinyDB(DBFILE)
    head = db.table("Head")
    navigation = db.table("Navigation")
    head_data = pd.DataFrame(data=head.all())
    data = pd.DataFrame(data=navigation.all())
    nav_head_name = head_data[head_data['head_id']==nav_head_id]["head_name"].values[0]
    ids = list(data['id'])
    if nav_id in ids:
        print('id={} is already exists'.format(nav_id))
        exit
    else:
        # 向表中添加数据
        navigation.insert_multiple([{
                "id": nav_id, 
                "nav_name": nav_name, 
                "abstract": nav_abstract, 
                "url": nav_url, 
                "photo": nav_photo, 
                "nav_type": nav_type, 
                "head_id": nav_head_id, 
                "head_name": nav_head_name, 
                "access_count": 0
            }])

    # 关闭连接
    db.close()
