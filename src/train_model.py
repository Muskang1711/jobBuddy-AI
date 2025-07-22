import pandas as pd
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import joblib

from src.embedding_generator import get_embeddings 

def load_texts_from_folder(folder_path):
    texts = []
    for filename in sorted(os.listdir(folder_path)):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            texts.append(file.read())
    return texts

def create_dataset(resumes, jds, num_resumes=100, num_jds=10):
    data = []
    for i in range(min(len(resumes), num_resumes)):
        for j in range(min(len(jds), num_jds)):
            is_match = 1 if i % num_jds == j else 0
            data.append({
                "resume": resumes[i],
                "jd": jds[j],
                "is_match": is_match
            })
    return pd.DataFrame(data)

def train_and_save_model(X, y, output_path="model/resume_matcher_model.pkl"):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("📊 Classification Report:\n", classification_report(y_test, y_pred))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    joblib.dump(clf, output_path)
    print(f"✅ Model saved at {output_path}")

if __name__ == "__main__":
    resume_folder = "data/resumes_txt_output"
    jd_folder = "data/job_descriptions_txt_output"

    resumes = load_texts_from_folder(resume_folder)
    jds = load_texts_from_folder(jd_folder)

    df = create_dataset(resumes, jds)

  
    resume_embeddings = get_embeddings(df["resume"].tolist(),model_name ="all-miniLM-L6-v2" )
    jd_embeddings = get_embeddings(df["jd"].tolist(),model_name ="all-miniLM-L6-v2" )

    X = [np.concatenate((r, j)) for r, j in zip(resume_embeddings, jd_embeddings)]
    y = df["is_match"].values

    train_and_save_model(X, y)