from flask import Flask, render_template, request
import pandas as pd
import prediction
app = Flask(__name__)


median_dic = {
    "dpf_median": 0.3725,
    "skin_median": 23.0,
    "pressure_median": 72.0,
}


@app.route('/')
def land_page():
    return render_template('landing.html')


@app.route('/upload', methods=['GET', 'POST'])
def process_input():
    if request.method.__eq__('POST'):
        if request.values:
            df_test = create_dataframe()
            print('Data to predict', df_test)
            phrase = prediction.produce_result(df_test)
            return render_template('load.html', phrase=phrase)

    return render_template('load.html')


def create_dataframe():
    age = [request.values['age']]
    glucose = [request.values['glucose']]
    bloodPressure = [request.values['bloodPressure']]
    skinThickness = [request.values['skinThickness']]
    insulin = [request.values['insulin']]
    diabetesPedigreeFunction = [request.values['diabetesPedigreeFunction']]
    pregnancies = [request.values['pregnancies']]
    bmi = [request.values['bmi']]

    if isinstance(request.values['bloodPressure'], str):
        bloodPressure = [median_dic["pressure_median"]]
    if isinstance(request.values['skinThickness'], str):
        skinThickness = [median_dic["skin_median"]]
    if isinstance(request.values['diabetesPedigreeFunction'], str):
        diabetesPedigreeFunction = [median_dic["dpf_median"]]
    if isinstance(request.values['pregnancies'], str):
        pregnancies = [0]

    rows = list(zip(pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, diabetesPedigreeFunction, age))
    columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
               'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    df_test = pd.DataFrame(rows, columns=columns)
    return df_test


if __name__ == '__main__':
    app.run()

