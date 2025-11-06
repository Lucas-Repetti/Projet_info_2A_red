from datetime import datetime, date
from decimal import Decimal
from typing import Optional, List


class Evenement:
    """
    Classe métier représentant un événement de l'application.
    Cette classe contient uniquement la logique métier et les attributs de l'entité.
    Les opérations de persistance et d'orchestration sont gérées par la couche service.
    """

    def __init__(
        self,
        date_evenement: Optional[date] = None,
        capacite_max: int = 0,
        created_by: Optional[int] = None,
        id_event: Optional[int] = None,
        created_at: Optional[datetime] = None,
    ):
        """
        Constructeur de la classe Evenement.

        titre: Titre de l'événement (max 100 caractères)
        lieu: Lieu de l'événement (max 100 caractères)
        date_evenement: Date de l'événement
        capacite_max: Capacité maximale de participants
        created_by: ID de l'utilisateur créateur (FK vers utilisateur)
        id_event: Identifiant unique de l'événement (auto-incrémenté en base)
        description_evenement: Description détaillée de l'événement
        created_at: Date de création de l'événement
        tarif: Tarif de participation à l'événement
        """

        # ========================== VALIDATIONS ==========================
        if date_evenement is None:
            raise ValueError("La date de l'événement est obligatoire")
        if not isinstance(date_evenement, date):
            raise ValueError("La date de l'événement doit être un objet date")
        if not isinstance(capacite_max, int):
            raise ValueError("La capacité maximale doit être un entier")
        if capacite_max <= 0:
            raise ValueError("La capacité maximale doit être supérieure à 0")
        if created_by is None:
            raise ValueError("L'ID du créateur est obligatoire")
        if not isinstance(created_by, int) or created_by <= 0:
            raise ValueError("L'ID du créateur doit être un entier positif")
        # =================================================================

        self.id_event = id_event
        self.date_evenement = date_evenement
        self.capacite_max = capacite_max
        self.created_by = created_by
        self.created_at = created_at or datetime.now()

    # ************************ Méthodes ***********************************************
    def est_passe(self) -> bool:
        """
        Vérifie si l'événement est déjà passé.

        return: True si la date de l'événement est antérieure à aujourd'hui
        ------
        """
        return self.date_evenement < date.today()

    def __repr__(self):
        """Représentation technique de l'objet"""
        return (
            f"<Evenement #{self.id_event}"
            f"({self.date_evenement})>"
        )

    def to_dict(self) -> dict:
        """
        Transforme l'objet en dictionnaire pour échange avec les autres couches.
        Utilisé pour la sérialisation (API, DAO, etc.)

        return: Dictionnaire contenant tous les attributs
        ------
        """
        return {
            "id_event": self.id_event,
            "date_evenement": self.date_evenement.isoformat() if self.date_evenement else None,
            "capacite_max": self.capacite_max,
            "created_by": self.created_by,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

    @staticmethod
    def from_dict(data: dict) -> "Evenement":
        """
        Transformation d'un dict (provenant de la DAO ou de l'API) vers un objet métier.

        data: Dictionnaire contenant les champs d'un événement

        return: Instance de Evenement
        ------
        """
        # Conversion de la date si elle est en format string
        date_evenement = data.get("date_evenement")
        if isinstance(date_evenement, str):
            date_evenement = datetime.fromisoformat(date_evenement).date()

        created_at = data.get("created_at")
        if isinstance(created_at, str):
            created_at = datetime.fromisoformat(created_at)

        return Evenement(
            id_event=data.get("id_event"),
            date_evenement=date_evenement,
            capacite_max=data.get("capacite_max", 0),
            created_by=data.get("created_by"),
            created_at=created_at,
        )