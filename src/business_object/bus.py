class Bus:
    """
    Classe métier représentant un bus pour un trajet (vers l'évènement ou au retour de l'évènement).
    Cette classe contient uniquement la logique métier et les attributs de l'entité.
    """

    def __init__(self, id_bus, id_event, sens):
        """
        Constructeur de la classe Bus.

        id_bus : Identifiant unique du bus (auto-incrémenté en base)
        id_event : Identifiant de l'évènement auquel le bus est attribué
        sens : aller ou retour de l'évènement ("Aller" ou "Retour")
        """

        # ========================== VALIDATIONS ==========================
        if id_event is None:
            raise ValueError("L'identifiant de l'évènement doit être renseigné")

        if not sens or sens.strip() == "":
            raise ValueError("Le sens ne peut pas être vide")
        if sens not in ("Aller", "Retour"):
            raise ValueError("Le sens doit être 'Aller' ou 'Retour'")
        # =================================================================

        self.id_bus = id_bus
        self.id_event = id_event
        # On stocke le sens sous forme booléenne pour simplifier les traitements
        self.sens = True if sens == "Aller" else False

    # ************************ MÉTHODES MÉTIER ************************
    def get_sens_str(self) -> str:
        """Retourne 'Aller' ou 'Retour' selon le booléen interne."""
        return "Aller" if self.sens else "Retour"

    def __repr__(self) -> str:
        """Représentation technique de l'objet."""
        return f"<Bus #{self.id_bus} (event={self.id_event}, sens={self.get_sens_str()})>"

    # ************************ MÉTHODES DE SÉRIALISATION ************************
    def to_dict(self) -> dict:
        """
        Transforme l'objet Bus en dictionnaire pour échange avec la DAO ou une API.
        """
        return {
            "id_bus": self.id_bus,
            "id_event": self.id_event,
            # On reconvertit le booléen en texte pour cohérence avec la base/API
            "sens": self.get_sens_str(),
        }

    @staticmethod
    def from_dict(data: dict) -> "Bus":
        """
        Crée une instance de Bus à partir d'un dictionnaire.
        data : dict contenant les champs du bus.
        """
        if not data:
            raise ValueError("Les données du bus ne peuvent pas être vides")

        id_bus = data.get("id_bus")
        id_event = data.get("id_event")
        sens = data.get("sens")

        # Si sens est stocké en booléen en base (ex: True/False), on convertit vers texte
        if isinstance(sens, bool):
            sens = "Aller" if sens else "Retour"

        return Bus(id_bus=id_bus, id_event=id_event, sens=sens)
