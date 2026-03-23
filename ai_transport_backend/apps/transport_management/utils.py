def classify_risk(risk):
    if risk < 2:
        return "Low"
    elif risk < 5:
        return "Medium"
    return "High"