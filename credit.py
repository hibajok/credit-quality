"""Évaluation simple du risque de crédit."""

HIGH_THRESHOLD = 0.6
MEDIUM_THRESHOLD = 0.3


def calculate_risk(income, debt, age):
    """Retourne "HIGH", "MEDIUM" ou "LOW" selon le ratio dette/revenu.

    Retourne -1 si le revenu est nul ou négatif.
    Le paramètre `age` est conservé pour compatibilité (non utilisé).
    """
    if income <= 0:
        return -1

    ratio = debt / income

    if ratio > HIGH_THRESHOLD:
        return "HIGH"
    if ratio > MEDIUM_THRESHOLD:
        return "MEDIUM"
    return "LOW"