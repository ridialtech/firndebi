import unittest
from backend import diplomes

class DiplomesTestCase(unittest.TestCase):
    def test_user_has_diploma(self):
        user = {"diplomas": ["PhD", "Master"]}
        self.assertTrue(diplomes.user_has_diploma(user, "PhD"))

    def test_user_missing_diploma(self):
        user = {"diplomas": ["Bachelor"]}
        self.assertFalse(diplomes.user_has_diploma(user, "PhD"))

    def test_valid_diploma(self):
        diploma = {
            "hash_diplome": "deadbeef",
            "verification_url": "https://verify.firndebi.com/deadbeef",
            "etudiant": {
                "matricule": "12345",
                "nom": "Doe",
                "prenoms": "John",
                "date_naissance": "2000-01-01",
            },
            "diplome": {
                "intitule": "Licence Informatique",
                "niveau": "Licence",
                "annee_academique": "2023-2024",
                "date_delivrance": "2024-10-01",
            },
            "etablissement": {
                "nom": "Université Firnde Bi",
                "structure": "Faculté Sciences",
                "pays": "SN",
            },
            "cycle_de_vie": {
                "statut": "VALIDE",
                "cree_le": "2024-10-01T00:00:00Z",
                "maj_le": "2024-10-01T00:00:00Z",
            },
        }
        self.assertTrue(diplomes.is_valid_diploma(diploma))

    def test_invalid_diploma_missing_field(self):
        diploma = {
            "hash_diplome": "deadbeef",
            # missing verification_url
            "etudiant": {
                "matricule": "12345",
                "nom": "Doe",
                "prenoms": "John",
                "date_naissance": "2000-01-01",
            },
            "diplome": {
                "intitule": "Licence Informatique",
                "niveau": "Licence",
                "annee_academique": "2023-2024",
                "date_delivrance": "2024-10-01",
            },
            "etablissement": {
                "nom": "Université Firnde Bi",
                "structure": "Faculté Sciences",
                "pays": "SN",
            },
            "cycle_de_vie": {
                "statut": "VALIDE",
                "cree_le": "2024-10-01T00:00:00Z",
                "maj_le": "2024-10-01T00:00:00Z",
            },
        }
        self.assertFalse(diplomes.is_valid_diploma(diploma))

if __name__ == "__main__":
    unittest.main()
