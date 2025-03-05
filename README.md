# Support-Vector-Machine
Kanser Tespiti SVM Modeli
Bu proje, kanserli ve kanserli olmayan hücreleri ayırt etmek için bir destek vektör makinesi (SVM) modelini kullanarak veri setini sınıflandırmaktadır. 
Proje, Python ve scikit-learn kullanarak hazırlanmıştır ve bir kanser teşhis veri seti üzerinde çalışmaktadır.

Başlangıç
Bu projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

Gereksinimler
Projenin çalışabilmesi için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

pandas
numpy
matplotlib
scikit-learn
Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

bash
Kopyala
Düzenle
pip install pandas numpy matplotlib scikit-learn
Veri Seti
Projede kullanılan veri seti, daha öncede kullanmış olduğum kanserli (Malignant) ve kanserli olmayan (Benign) hücreler arasındaki farkları içeren bir dosya olan data.csv'yi kullanmaktadır. Veri setinde, hücre özellikleri ve etiketler bulunmaktadır. Etiketler, hücrenin kanserli olup olmadığını gösterir. Veri setini ekte paylaşmış olacağım.

Proje Yapısı
Veri Yükleme: data.csv dosyasındaki veriler, pandas kullanılarak yüklenir.
Veri Ön İşleme:
Gereksiz sütunlar (id, Unnamed: 32) kaldırılır.
Kategorik etiketler (M, B) sayısal değerlere dönüştürülür.
Eksik veriler kontrol edilir ve NaN değerleri temizlenir.
Model Eğitimi:
Veriler normalize edilerek, eğitim ve test verilerine ayrılır.
SVM modeli (SVC) kullanılarak eğitim yapılır.
Başarımlı Değerlendirme:
Modelin doğruluk oranı (accuracy) hesaplanır ve yazdırılır.
Kurulum

Katkı
DataI Kaggle sayfası gene bu çalışmada bana öncülük etmiştir. https://www.kaggle.com/kanncaa1

Yazar: Kadir Özan
Tarih: 05.03.2025
