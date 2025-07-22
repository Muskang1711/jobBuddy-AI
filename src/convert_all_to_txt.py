import pandas as pd
import os

def convert_resumes(csv_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(csv_path)
    print("📄 Resume Columns:", df.columns)

    saved = 0
    for idx, row in df.iterrows():
        resume_txt = row.get("Resume") or row.get("resume") or row.get("resume_text")
        if pd.isna(resume_txt):
            continue
        file_path = os.path.join(output_dir, f"resume_{idx+1}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(resume_txt))
        print(f"✅ Resume Saved: {file_path}")
        saved += 1
    print(f"🎯 Total resumes saved: {saved}")

def convert_jd_csv_to_txt(csv_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(csv_path)
    print("🧾 JD Columns:", df.columns)

    saved = 0

    # Try auto-detecting the description column
    jd_col = None
    for col in df.columns:
        if "description" in col.lower():
            jd_col = col
            break

    if not jd_col:
        print("❌ No Job Description column found.")
        return

    for idx, row in df.iterrows():
        jd_text = row.get(jd_col)
        if pd.isna(jd_text):
            continue

        file_path = os.path.join(output_dir, f"jd_csv_{idx+1}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(jd_text))

        print(f"✅ Saved: {file_path}")
        saved += 1

    print(f"🎉 Total JDs saved: {saved}")


if __name__ == "__main__":
    convert_jd_csv_to_txt(
        csv_path="data\job_descriptiom\data job posts.csv",
        output_dir="data/job_descriptions_txt_output/"
    )
    convert_resumes(
        csv_path="data/resumes/UpdatedResumeDataSet.csv",
        output_dir="data/resumes_txt_output/"
    )