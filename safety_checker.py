import re
def check_safety(text):
    text_lower = text.lower()
    warnings = []
    information = []
    if "expiry" in text_lower or "exp" in text_lower:
        information.append("Expiry information detected.")
    else:
        warnings.append("Expiry date could not be detected.")
    if "store" in text_lower or "storage" in text_lower:
        information.append("Storage instructions detected.")
    else:
        warnings.append("Storage instructions could not be detected.")
    if "dose" in text_lower or "dosage" in text_lower:
        information.append("Dosage information detected.")
    else:
        warnings.append("Dosage information could not be detected.")
    if "warning" in text_lower or "precaution" in text_lower:
        information.append("Warning or precaution information detected.")
    else:
        warnings.append("Warning or precaution information could not be detected.")
    if "prescription" in text_lower or "rx" in text_lower:
        warnings.append("This appears to be a prescription medicine. Use only as directed by a qualified healthcare professional.")
    if "children" in text_lower:
        information.append("Information related to children was detected.")
    return information, warnings