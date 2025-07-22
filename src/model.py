from src.embed import generate_embedding
from sklearn.metrics.pairwise import cosine_similarity

def match_resumes(resume: str, job_descriptions: list):
    resume_emb = generate_embedding(resume)
    job_embs = [generate_embedding(jd) for jd in job_descriptions]
    scores = cosine_similarity([resume_emb], job_embs)[0]
    sorted_matches = [jd for _, jd in sorted(zip(scores, job_descriptions), reverse=True)]
    return sorted_matches[:3]
