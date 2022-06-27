
from flask import Flask, request, render_template
import joblib
from flask_restful import Api
import  pandas  as pd

#model = pickle.load(open('model_cat.pkl', 'rb'))
app = Flask(__name__)
api = Api(app)

@app.route("/")
def main():
    return render_template('_user.html')

#고양이
@app.route('/predict',methods=['POST'])

def home():
    
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']

    a= {'Outcome Subtype':[data1],'Animal Type':[data2],'Sex upon Outcome':[data3],'Age upon Outcome':[data4],'Breed':[data5],'Color':[data6]}
    df = pd.DataFrame(a)
    pred = model_animal.predict(df)
    print(pred)
    return render_template('_predict.html', data=pred)




if __name__ == '__main__':
    # 모델 로드
    # ml/model.py 선 실행 후 생성
    model_animal = joblib.load('/Users/ojihye/Desktop/animal_center/model_animal.pkl')
    
    # Flask 서비스 스타트
    app.run(host='0.0.0.0', port=8000, debug=True)