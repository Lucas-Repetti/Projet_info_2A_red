DROP SCHEMA IF EXISTS projet CASCADE;
CREATE SCHEMA projet;

SET search_path TO projet;

CREATE TABLE projet.utilisateur (
    id_utilisateur SERIAL PRIMARY KEY,
    nom            VARCHAR(50),
    prenom         VARCHAR(50),
    email          VARCHAR(100) UNIQUE,
    mot_de_passe   VARCHAR(100),
    role           BOOLEAN DEFAULT FALSE
);

CREATE TABLE projet.evenement (
    id_event        SERIAL PRIMARY KEY,
    date_evenement  DATE NOT NULL,
    capacite_max    INT CHECK (capacite_max > 0),
    created_by      INT NOT NULL REFERENCES projet.utilisateur(id_utilisateur) ON DELETE CASCADE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projet.bus (
    id_bus          SERIAL PRIMARY KEY,
    id_event        INT NOT NULL REFERENCES projet.evenement(id_event) ON DELETE CASCADE,
    sens            BOOLEAN NOT NULL,
    heure_depart    TIMESTAMP NOT NULL
);

CREATE TABLE projet.inscription (
    code_reservation SERIAL PRIMARY KEY,
    id_utilisateur   INT NOT NULL REFERENCES projet.utilisateur(id_utilisateur) ON DELETE CASCADE,
    id_event         INT NOT NULL REFERENCES projet.evenement(id_event) ON DELETE CASCADE,
    id_bus_aller     INT REFERENCES projet.bus(id_bus) ON DELETE SET NULL,
    id_bus_retour    INT REFERENCES projet.bus(id_bus) ON DELETE SET NULL,
    created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
