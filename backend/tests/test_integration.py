import unittest
from backend import auth, diplomes


class IntegrationTestCase(unittest.TestCase):
    """Integration tests combining auth and diploma validation."""

    def setUp(self):
        self.user = {
            "username": "admin",
            "password": "secret",
            "diplomas": ["Licence Informatique"],
        }
        self.diploma = {
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

    def test_end_to_end_flow(self):
        """Authenticate, validate diploma, then confirm user owns it."""
        self.assertTrue(auth.authenticate(self.user["username"], self.user["password"]))
        self.assertTrue(diplomes.is_valid_diploma(self.diploma))
        self.assertTrue(diplomes.user_has_diploma(self.user, self.diploma["diplome"]["intitule"]))


if __name__ == "__main__":
    unittest.main()
