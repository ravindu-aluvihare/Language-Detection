import pickle

# Load model, vectorizer, and label encoder
model = pickle.load(open('model/language_model.pkl', 'rb'))
vectorizer = pickle.load(open('model/cv.pkl', 'rb'))
label_encoder = pickle.load(open('model/label_encoder.pkl', 'rb'))

def predict_language(text):
    data = [text]
    vect = vectorizer.transform(data).toarray()
    result = model.predict(vect)
    lang_name = label_encoder.inverse_transform(result)
    return lang_name[0]
