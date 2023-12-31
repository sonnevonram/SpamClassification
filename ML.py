from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Data contoh (bisa diganti dengan dataset yang sesuai)
email = [
    ("Gratis masuk ke konser besok? Segera dapatkan tiketnya!", "spam"),
    ("Halo, bagaimana kabarmu? Sudah lama tidak berbicara.", "ham"),
    ("Selamat! Kamu memenangkan hadiah spesial.", "spam"),
    ("Pertemuan besok di kantor jam 9 pagi.", "ham"),
]

# Memisahkan pesan dan label
texts, labels = zip(*email)

# Mengonversi label menjadi nilai biner: 0 untuk ham, 1 untuk spam
label_map = {"ham": 0, "spam": 1}
y = [label_map[label] for label in labels]

# Mengonversi teks menjadi fitur vektor menggunakan CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model SVM (Support Vector Machine) dan melatihnya
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train, y_train)

# Melakukan prediksi pada data uji
y_pred = svm_classifier.predict(X_test)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')
