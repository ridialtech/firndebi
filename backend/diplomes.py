"""Helpers for working with diploma data."""

def user_has_diploma(user: dict, diploma: str) -> bool:
    """Check if a user dictionary contains a given diploma."""
    return diploma in user.get("diplomas", [])


def is_valid_diploma(data: dict) -> bool:
    """Validate minimal Firnde Bi diploma structure.

    The schema follows the six families of data described in the
    documentation. Only a subset of required fields is checked here
    to keep the example concise.
    """

    try:
        # Technical keys
        for key in ["hash_diplome", "verification_url"]:
            if key not in data:
                return False

        # Student information
        etu = data.get("etudiant", {})
        for key in ["matricule", "nom", "prenoms", "date_naissance"]:
            if key not in etu:
                return False

        # Diploma details
        dipl = data.get("diplome", {})
        for key in [
            "intitule",
            "niveau",
            "annee_academique",
            "date_delivrance",
        ]:
            if key not in dipl:
                return False

        # Establishment details
        etab = data.get("etablissement", {})
        for key in ["nom", "structure", "pays"]:
            if key not in etab:
                return False

        # Lifecycle data
        cycle = data.get("cycle_de_vie", {})
        for key in ["statut", "cree_le", "maj_le"]:
            if key not in cycle:
                return False

        return True
    except Exception:
        return False
