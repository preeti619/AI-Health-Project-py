# health_logic.py
def predict_condition(symptoms):
    mapping = {
        "headache": "You might have a migraine or dehydration.",
        "fever": "Possible viral infection or flu.",
        "cough": "Could be a respiratory infection.",
        "cold": "Likely common cold or early signs of allergy.",
        "sore throat": "Possible throat infection or tonsillitis.",
        "fatigue": "Could be due to anemia, stress, or sleep deprivation.",
        "chest pain": "May indicate heart-related issues or acid reflux.",
        "shortness of breath": "Could be asthma or COVID-related.",
        "nausea": "Might be related to indigestion or pregnancy.",
        "vomiting": "Possibly food poisoning or viral infection.",
        "diarrhea": "Could indicate gastrointestinal infection.",
        "constipation": "Possibly diet-related or irritable bowel syndrome.",
        "abdominal pain": "May suggest gastritis or appendicitis.",
        "back pain": "Could be posture-related or disc issues.",
        "joint pain": "Might be arthritis or injury.",
        "dizziness": "Could indicate low BP or vertigo.",
        "blurred vision": "May relate to eye strain or high sugar levels.",
        "weight loss": "Could indicate diabetes or thyroid problems.",
        "weight gain": "Possibly hypothyroidism or lifestyle related.",
        "frequent urination": "May indicate diabetes or UTI.",
        "burning urination": "Likely urinary tract infection.",
        "rash": "Could be allergy or skin infection.",
        "itching": "May relate to allergies or skin conditions.",
        "swelling": "Can be due to injury or kidney issues.",
        "palpitations": "Could be anxiety or heart rhythm issue.",
        "anxiety": "Mental health concern, consider consulting a psychologist.",
        "depression": "Important to seek mental health support.",
        "night sweats": "May be infection or hormonal imbalance.",
        "hair loss": "Can be due to stress or nutritional deficiency.",
        "acne": "Likely hormonal or hygiene-related.",
        "dry skin": "Could be due to dehydration or skin condition.",
        "ear pain": "Possible ear infection or wax buildup.",
        "hearing loss": "Needs audiometry, could be age or exposure-related.",
        "nosebleed": "May result from dry air or high BP.",
        "difficulty swallowing": "Could be throat infection or GERD.",
        "hoarseness": "Likely viral or voice strain.",
        "loss of smell": "Could indicate COVID or sinus issue.",
        "loss of taste": "Possibly COVID or oral issues.",
        "frequent headaches": "May suggest migraines or stress.",
        "muscle cramps": "Can be electrolyte imbalance.",
        "tremors": "May be neurological or anxiety-related.",
        "fainting": "Could be low BP or serious condition.",
        "confusion": "Important to rule out neurological issues.",
        "memory loss": "Could indicate early dementia.",
        "slurred speech": "Seek emergency care, possible stroke.",
        "numbness": "Could be nerve-related or diabetic neuropathy.",
        "tingling": "May suggest vitamin B12 deficiency.",
        "difficulty breathing": "Urgent – possible asthma or lung issue.",
        "high blood pressure": "Monitor regularly, consult a doctor.",
        "low blood pressure": "Ensure hydration, consult physician.",
        "insomnia": "Likely stress, screen time or anxiety."
    }

    result = []
    for symptom in symptoms:
        symptom_clean = symptom.strip().lower()
        if symptom_clean in mapping:
            result.append(f"🩺 {symptom_clean.title()}: {mapping[symptom_clean]}")
        else:
            result.append(f"❓ {symptom_clean.title()}: No information available. Please check input is correct")
    return "\n\n".join(result)
