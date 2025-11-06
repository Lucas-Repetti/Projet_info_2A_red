from datetime import datetime
from datetime import date
"""import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException"""


class Inscription:

    """
    Classe métier représentant une inscription dans un évènement.
    Cette classe contient uniquement la logique métier et les attributs de l'entité.
    """

    def __init__(
        self,
        code_reservation: int,
        id_utilisateur: int = None,
        id_event: str = "",
        id_bus_aller: str = "",
        id_bus_retour: str = ""
    ):
        """
        Constructeur de la classe Inscription.
        """
        # ========================== VALIDATIONS ==========================
        if not isinstance(code_reservation, int) or code_reservation <= 0:
            raise ValueError("Le code de réservation doit être un entier positif.")
        if id_utilisateur is None:
            raise ValueError("L'attribut 'id_utilisateur' (ID utilisateur) est obligatoire.")
        if not isinstance(id_utilisateur, int):
            raise TypeError("L'attribut 'id_utilisateur' doit être un entier.")
        if not id_event or not isinstance(id_event, str):
            raise ValueError("L'ID de l'événement est obligatoire et doit être une chaîne.")
        if not isinstance(id_bus_aller, str):
            raise TypeError("L'identifiant du bus aller doit être une chaîne de caractères.")
        if not isinstance(id_bus_retour, str):
            raise TypeError("L'identifiant du bus retour doit être une chaîne de caractères.")
        # =================================================================

        # ========================== INITIALISATION ==========================
        self.code_reservation = code_reservation
        self.id_utilisateur = id_utilisateur
        self.id_event = id_event
        self.id_bus_aller = id_bus_aller
        self.id_bus_retour = id_bus_retour
        self.date_creation = datetime.now()
        # =================================================================

    # ************************ Méthodes ***********************************************
    """
    @staticmethod
    def envoyer_mail(adresse_email: str):
        # Configuration de l'API
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = "TA_CLE_API_BREVO"  # ← Remplace ici ta clé

        # Création de l’instance API
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

        # Contenu du mail
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": adresse_email}],
            sender={"name": "Ton Nom", "email": "ton_adresse@domaine.com"},
            subject="Ceci est un test Brevo",
            html_content="<html><body><h1>Bonjour !</h1><p>Ceci est un test d’envoi d’e-mail via Brevo.</p></body></html>"
        )

        try:
            response = api_instance.send_transac_email(send_smtp_email)
            print(f"✅ E-mail envoyé à {adresse_email} — Message ID : {response['messageId']}")
        except ApiException as e:
            print(f"❌ Erreur lors de l'envoi : {e}")
    """

    def __repr__(self):
        """Représentation texte"""
        return f"<Inscription {self.id_utilisateur} - {self.nom_event}>"

    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire"""
        return {
            "code_reservation": self.code_reservation,
            "id_utilisateur": self.id_utilisateur,
            "id_event": self.id_event,
            "id_bus_aller": self.id_bus_aller,
            "id_bus_retour": self.id_bus_retour,
            "date_creation": self.date_creation.isoformat(),
        }

    @staticmethod
    def from_dict(data: dict) -> "Inscription":
        """Créer un objet Inscription à partir d'un dictionnaire"""
        return Inscription(
            code_reservation=data.get("code_reservation"),
            id_utilisateur=data.get("id_utilisateur"),
            id_event=data.get("id_event", ""),
            id_bus_aller=data.get("id_bus_aller", ""),
            id_bus_retour=data.get("id_bus_retour", ""),
        )
