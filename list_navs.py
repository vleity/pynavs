from config import DBFILE
from tinydb import TinyDB
import uuid
import json
import pandas as pd
import argparse


if __name__ == '__main__':
    # 参数解析
    parser = argparse.ArgumentParser(description='Add head')
    parser.add_argument('-t', type=str, default='all', help="list head,nav,all")
    parser.add_argument('-a', type=str, default='', help="list nav detail")
    args = parser.parse_args()
    t = args.t
    a = args.a


    # 连接数据库
    db = TinyDB(DBFILE)
    head = db.table("Head")
    navigation = db.table("Navigation")
    head_data = pd.DataFrame(data=head.all())
    nav_data = pd.DataFrame(data=navigation.all())
    # 关闭连接
    db.close()

    # 展示
    if t in ['head','all']:
        print("+----Head----+")
        for index,row in head_data.iterrows():
            print(row.head_id,row.head_name)
    
    if t in ['nav','all']:
        print()
        print("+----Navigation----+")
        print()
        for i,head in head_data.iterrows():
            print("+--"+head.head_name)
            for j,nav in nav_data[nav_data["head_id"]==head.head_id].iterrows():
                if a == 'all':
                    print("  +--{nav_name}【{abstract}】({id},{url},{photo})".format(nav_name=nav.nav_name,abstract=nav.abstract,id=nav.id,url=nav.url,photo=nav.photo))
                else:
                    print("  +--{nav_name}【{abstract}】({url})".format(nav_name=nav.nav_name,abstract=nav.abstract,url=nav.url))



