# dao/utilisateur_dao.py
from typing import Optional, List
from Projet_info_2A.src.business_object.utilisateur import Utilisateur
from Projet_info_2A.src.dao.db_connection import DBConnection


class UtilisateurDAO:
    """Accès aux données pour les utilisateurs"""

    @staticmethod
    def creer(utilisateur: Utilisateur) -> Utilisateur:
        query = """
            INSERT INTO utilisateur (nom, prenom, email, mot_de_passe, role, date_creation)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id_utilisateur;
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
                    (
                        utilisateur.nom,
                        utilisateur.prenom,
                        utilisateur.email,
                        utilisateur.mot_de_passe,
                        utilisateur.role,
                        utilisateur.date_creation,
                    ),
                )
                utilisateur.id_utilisateur = cursor.fetchone()["id_utilisateur"]
        return utilisateur

    @staticmethod
    def get_by_id(id_utilisateur: int) -> Optional[Utilisateur]:
        query = "SELECT * FROM utilisateur WHERE id_utilisateur = %s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                row = cursor.fetchone()
                if row:
                    return Utilisateur.from_dict(row)
                return None

    @staticmethod
    def trouver_tous() -> List[Utilisateur]:
        query = "SELECT * FROM utilisateur ORDER BY id_utilisateur"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Utilisateur.from_dict(row) for row in rows]