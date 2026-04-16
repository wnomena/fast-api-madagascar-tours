# FastAPI Madagascar Tours

## 📋 Présentation

API backend haute performance construite avec FastAPI pour l'application Madagascar Tours. Ce service côté serveur fournit tous les endpoints REST nécessaires pour servir l'application React frontend, gérant les circuits touristiques, les réservations et les interactions clients.

## 🎯 Objectif

Créer une API REST performante et type-safe qui alimente l'expérience utilisateur de Madagascar Tours, en gérant efficacement les données clients, les circuits, et les opérations commerciales.

## 🛠️ Stack Technique

- **Framework Web** : FastAPI 0.121.1 (async-first)
- **Serveur ASGI** : Uvicorn 0.38.0
- **Validation de Données** : Pydantic 2.12.4
- **Base de Données** : SQLAlchemy 2.0.44 avec MySQL
- **Pilote MySQL** : PyMySQL 1.1.2, aiomysql 0.3.2
- **Variables d'Environnement** : python-dotenv 1.2.1
- **Validation Email** : email-validator 2.3.0
- **Client HTTP** : httpx 0.28.1
- **CLI** : FastAPI CLI 0.0.16
- **Performance** : uvloop 0.22.1

## 📦 Composants du Projet

### Architecture RESTful

- **Endpoints Circuits** : CRUD complet pour gestion des circuits touristiques
- **Gestion des Réservations** : Endpoints de réservation avec validation métier
- **Authentification Clients** : Endpoints de registration/login
- **Gestion de Contacts** : Formulaires de contact intégrés
- **Middleware CORS** : Support requêtes cross-origin sécurisé
- **Validation Pydantic** : Type-safety automatique sur tous les endpoints

## 🚀 Fonctionnalités Principales

✅ API REST complète avec documentation Swagger automatique
✅ Async/await natif pour performance maximale
✅ Validation de données robuste avec Pydantic
✅ Gestion des erreurs standardisée
✅ Support CORS pour frontend React
✅ ORM SQLAlchemy pour requêtes optimisées
✅ Planification asynchrone avec aiomysql
✅ Monitoring avec Sentry intégré

## 🔧 Installation & Utilisation

```bash
# Installation des dépendances
pip install -r requirements.txt

# Mode développement avec rechargement automatique
fastapi dev main.py

# Mode production
uvicorn main:app --host 0.0.0.0 --port 8000
