from flask import Flask, render_template
from config import DBFILE,PORT
from tinydb import TinyDB,Query
from tinydb.operations import increment
import uuid
import pandas as pd
import json

app = Flask(__name__)

@app.route('/c/id/')
def c(id):
    try:
        db = TinyDB(DBFILE)
        navigation = db.table("Navigation")
        Q = Query()
        navigation.update(increment('access_count'), Q.id == id)
        db.close()
        return {"code":"200","msg":"success"}
    except Exception as e:
        return {"code":"400","msg":str(e)}
    
@app.route('/')
def index():
    db = TinyDB(DBFILE)
    head = db.table("Head")
    navigation = db.table("Navigation")
    data = pd.DataFrame(data=navigation.all())
    data.access_count = data.access_count.astype('int')
    db.close()

    # 根据导航类型分类

    context = {}

    for nav_type in ['tag']:
        context[nav_type] = dict()
        data_tag = data[data.nav_type == nav_type].sort_values(by='access_count',ascending=False)
        heads = data_tag[['head_id','head_name']].drop_duplicates().sort_values(by='head_id',ascending=True)

        context[nav_type].update({
            'heads': json.loads(heads.to_json(orient='records')),
            'data': json.loads(data_tag.to_json(orient='records'))
        })
    
    # 渲染模板
    return render_template('index.html',context=context)


if __name__ == '__main__':
    app.run(port=PORT)
