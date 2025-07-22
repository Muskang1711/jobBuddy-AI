from src.model import match_resumes

def test_basic_match():
    resume = "Python developer with experience in ML, NLP, and cloud deployment."
    jobs = [
        "Looking for a backend developer with Django",
        "Need ML/NLP engineer with Python and Transformers",
        "Hiring front-end React developers"
    ]
    results = match_resumes(resume, jobs)
    assert len(results) == 3
    assert isinstance(results, list)
