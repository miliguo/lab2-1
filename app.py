from flask import Flask, request, jsonify, render_template

username="郭茹萍"
# define statu_dics here
R200_OK = {'code': 200, 'message': 'OK all right.'}
R201_CREATED = {'code': 201, 'message': 'All created.'}
R204_NOCONTENT = {'code': 204, 'message': 'All deleted.'}
R400_BADREQUEST = {'code': 400, 'message': 'Bad request.'}
R403_FORBIDDEN = {'code': 403, 'message': 'You can not do this.'}
R404_NOTFOUND = {'code': 404, 'message': 'No result matched.'}


def fullResponse(statu_dic, data):
    return jsonify({'status': statu_dic, 'data': data})

def statusResponse(statu_dic):
    return jsonify({'status': statu_dic})


app=Flask(__name__)

datas=[{'studentId':'20212010100','name':'a','department':'MS','major':'A'},
       {'studentId':'20212010101','name':'b','department':'MS','major':'B'},
       {'studentId':'20212010102','name':'c','department':'MS','major':'C'},
       {'studentId':'20212010103','name':'d','department':'MS','major':'A'},
       {'studentId':'20212010104','name':'e','department':'IEM','major':'B'},
       {'studentId':'20212010105','name':'f','department':'IEM','major':'C'}]
@app.route('/')
def api_root():
    return 'welcome'
#GET请求，查看学生
@app.route('/api/v1/student')
def getStudent():
    return fullResponse(R200_OK,datas)
#POST请求，增加一个学生
@app.route('/api/v1/student',methods=['POST'])
def addOne():
    request_data=request.get_json()
    if not 'studentId'in request_data or not 'name' in request_data or not 'department' in request_data or not 'major' in request_data:
        return statusResponse(R400_BADREQUEST)
    studentId=request_data['studentId']
    name=request_data['name']
    department=request_data['department']
    major=request_data['major']
    datas.append({'studentId':studentId,'name':name,'department':department,'major':major})
    return statusResponse(R201_CREATED)

#curl --header "Content-Type: application/json" -X POST http://127.0.0.1:5000/student -d "{\"studentId\": \"20212010126\", \"name\": \"guoruping\",\"department\": \"ML\", \"major\": \"web\"}"
#不能识別中文
#PUT请求，修改学生信息
@app.route('/api/v1/student',methods=['PUT'])
def ediOne():
    request_data = request.get_json()
    result=[data for data in datas if data['studentId']==request_data['studentId']]
    if len(result)==0:
        return statusResponse(R404_NOTFOUND)
    result[0]['studentId'] = request_data['studentId']
    result[0]['name'] = request_data['name']
    result[0]['department'] = request_data['department']
    result[0]['major'] = request_data['major']
    return statusResponse(R201_CREATED)
#curl --header "Content-Type: application/json" -X PUT http://127.0.0.1:5000/student -d "{\"studentId\": \"20212010100\", \"name\": \"guoruping\",\"department\": \"ML\", \"major\": \"web\"}"

#DELETE删除，没什么好说的
@app.route('/api/v1/student', methods=['DELETE'])
def delOne():
    request_data = request.get_json()
    result = [data for data in datas if data['studentId'] == request_data['studentId']]
    if len(result) == 0:
        return statusResponse(R404_NOTFOUND)
    datas.remove(result[0])
    return statusResponse(R204_NOCONTENT)
#curl --header "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/student -d "{\"studentId\": \"20212010100\"}"

@app.route('/index')
def index():
    return render_template('index.html',username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

