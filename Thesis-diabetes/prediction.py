import warnings
import pickle
warnings.simplefilter(action='ignore', category=FutureWarning)


rf_model = pickle.load(open('static/models/random_forest.sav', 'rb'))


def produce_result(dataframe):
    if rf_model.predict(dataframe)[0] == 0:
        return 'У Вас ОТСУТСТВУЕТ диабет с вероятностью до 83 %'
    else:
        return 'У Вас ПРИСУТСТВУЕТ диабет с вероятностью до 83 %'
