import requests
from bs4 import BeautifulSoup
import time
import random
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbikea                     # 'dbikea'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

# @app.route('/<name>')
# def name(name):
#    return "안녕!  " + name + "Welcome"


# @app.route("/info", methods=['GET'])
# def move_forward1():
#        #Moving forward code
#        return render_template('info.html')


# @app.route("/rand", methods=['GET'])
# def move_forward2():
#        #Moving forward code
#        return render_template('rand.html')


# @app.route('/info/random', methods=['GET'])
# def listing():
#     # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기 
#     # 랜덤으로 sofas 정렬
#     sofas = list(db.sofas.find({}, {'_id': False}))
#     chairs = list(db.chairs.find({}, {'_id': False}))
#     desks = list(db.desks.find({}, {'_id': False}))
#     random.shuffle(chairs)
#     random.shuffle(sofas)
#     random.shuffle(desks)

#     rand = sofas + chairs + desks
#     random.shuffle(rand)
    
#     return jsonify({'result':'success', 'rand': rand})

# @app.route('/info/sofa', methods=['GET'])
# def get_sofa():
#     sofas = list(db.sofas.find({}, {'_id': False}))
#     random.shuffle(sofas)
#     return jsonify({'result':'success', 'sofas': sofas})



# @app.route('/info/price/sofa', methods=['POST'])
# def get_price_sofa():
#     min_price = request.form['min_price_give']
#     max_price = request.form['max_price_give']
#     sofa_list = []
#     sofas = list(db.sofas.find({}, {'_id': False}))
#     for sofa in sofas:
#         price = int(sofa['price'].replace('￦','').replace('원','').strip().replace(',',''))
#         if int(min_price) <= price and price <= int(max_price):
#             sofa_list.append(sofa)
#     random.shuffle(sofa_list)
#     return jsonify({'result':'success', 'sofas': sofa_list})



# # 데이터 삭제 (이미지 주소가 같은걸 삭제)
# @app.route('/info/delete', methods=['POST'])
# def star_delete():
#     # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
#     img_receive = request.form['img_give']
#     # 2. mystar 목록에서 delete_one으로 img이 name_receive와 일치하는 star를 제거합니다.
#     db.sofas.delete_one({'img':img_receive})
#     db.chairs.delete_one({'img':img_receive})
#     db.desks.delete_one({'img':img_receive})
#     # 3. 성공하면 success 메시지를 반환합니다.
#     return jsonify({'result': 'success'})

# @app.route('/info/like', methods=['POST'])
# def star_like():
    
#     img_receive = request.form['img_give']
#     # sofa일때
#     try:
#         star1 = db.sofas.find_one({'img':img_receive})
#         new_like = star1['like']+1
#         db.sofas.update_one({'img':img_receive},{'$set':{'like':new_like}})
#     except:
#         pass
#     #chair일때
#     try:
#         star2 = db.chairs.find_one({'img':img_receive})
#         new_like = star2['like']+1
#         db.chairs.update_one({'img':img_receive},{'$set':{'like':new_like}})
#     except:
#         pass
#     #desk일때
#     try:
#         star3 = db.desks.find_one({'img':img_receive})
#         new_like = star3['like']+1
#         db.desks.update_one({'img':img_receive},{'$set':{'like':new_like}})
#     except:
#         pass

#     return jsonify({'result': 'success'})

# @app.route('/info/sofa/like', methods=['GET'])
# def like_sofa_list() :
#     sofas = list(db.sofas.find({},{'_id':False}).sort('like',-1))
#     return jsonify({'result': 'success','sofas':sofas})

# @app.route('/info/chair/like', methods=['GET'])
# def like_chair_list() :
#     chairs = list(db.chairs.find({},{'_id':False}).sort('like',-1))
#     return jsonify({'result': 'success','chairs':chairs})

# @app.route('/info/desk/like', methods=['GET'])
# def like_desk_list() :
#     desks = list(db.desks.find({},{'_id':False}).sort('like',-1))
#     return jsonify({'result': 'success','desks':desks})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)