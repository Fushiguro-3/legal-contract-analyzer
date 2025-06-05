import spacy

nlp = spacy.load("en_core_web_sm")

def extract_clauses(text):
    doc = nlp(text)
    clauses = {
        "dates": [],
        "parties": [],
        "obligations": [],
    }

    for ent in doc.ents:
        if ent.label_ in ["DATE"]:
            clauses["dates"].append(ent.text)
        if ent.label_ in ["ORG", "PERSON"]:
            clauses["parties"].append(ent.text)

    # Basic pattern matching for obligations
    for sent in doc.sents:
        if "shall" in sent.text or "must" in sent.text:
            clauses["obligations"].append(sent.text.strip())

    return clauses
