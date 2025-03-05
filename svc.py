# Gerekli kütüphaneleri içe aktar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Veri setini oku
df = pd.read_csv("data.csv")
#Gereksiz sütunları kaldır
df.drop(["id", "Unnamed: 32"], axis=1, inplace=True)
# Kategorik etiketi sayısal hale getir (M=1, B=0)
df["diagnosis"] = df["diagnosis"].map({"M": 1, "B": 0})
#Eksik veri var mı kontrol et
print("Eksik veri var mı?\n", df.isnull().sum())

#Özellikleri (X) ve etiketleri (y) ayır
y = df["diagnosis"].values
x_data = df.drop(["diagnosis"], axis=1)

#normalizasyon
x = (x_data - x_data.min()) / (x_data.max() - x_data.min())
#Train-test ayrımı (70% train - 30% test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
#NumPy array'e çevir (NaN kontrolü sonrası)
x_train = np.array(x_train)
y_train = np.array(y_train)
#Tekrar eksik veri olup olmadığını kontrol et
print("x_train'de NaN var mı?", np.isnan(x_train).sum())
print("y_train'de NaN var mı?", np.isnan(y_train).sum())

#Eğer hala NaN varsa, onları temizle
x_train = np.nan_to_num(x_train)
x_test = np.nan_to_num(x_test)

#SVM modelini oluştur ve eğit
svc_model = SVC(random_state=1)
svc_model.fit(x_train, y_train)

#Modelin başarımını ölç
accuracy = svc_model.score(x_test, y_test)
print("Accuracy score:", accuracy)
#Alternatif doğruluk hesaplama
y_pred = svc_model.predict(x_test)
accuracy2 = accuracy_score(y_test, y_pred)
print("Accuracy score with predict:", accuracy2)
