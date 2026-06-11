import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib

# 1. Carregar os dados
df = pd.read_csv('dados.csv')

# 2. Transformar texto em números (Vetorização TF-IDF)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['texto'])
y = df['intencao']

# 3. Treinar o modelo (Algoritmo SVM)
modelo = SVC(kernel='linear')
modelo.fit(X, y)

# 4. Salvar o modelo e o vetorizador para usar depois
joblib.dump(modelo, 'modelo_ia.pkl')
joblib.dump(vectorizer, 'vetorizador.pkl')

print("Modelo treinado e salvo com sucesso!")