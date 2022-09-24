import warnings
import pickle
warnings.simplefilter(action='ignore', category=FutureWarning)


rf_model = pickle.load(open('static/models/random_forest.sav', 'rb'))


def produce_result(dataframe):
    if rf_model.predict(dataframe)[0] == 0:
        return 'You do NOT have diabetes with a probability of up to 83 %'
    else:
        return 'You HAVE diabetes with a probability of up to 83 %'
