# Simulateur du Théorème Central Limite (TCL)

## Description
Application web interactive construite avec Django permettant de simuler
le Théorème Central Limite (TCL). L'utilisateur choisit une distribution
probabiliste, ses paramètres, la taille d'échantillon et le nombre de
répétitions; l'application génère automatiquement l'histogramme des
moyennes avec la courbe normale théorique.

---

## 1. Prérequis

- Python 3.x
- pip

---

## 2. Installation

```bash
# Cloner le projet
git clone https://github.com/TON_USERNAME/Projet_Django.git
cd Projet_Django

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows :
venv\Scripts\activate
# Mac/Linux :
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

---

## 3. Utilisation

```bash
# Appliquer les migrations
python manage.py migrate

# Lancer le serveur
python manage.py runserver
```

Ouvrez votre navigateur sur :
```
http://127.0.0.1:8000/
```

### Paramètres disponibles

| Distribution | Paramètre |
|---|---|
| Uniforme [0,1] | — |
| Exponentielle | λ (lambda) |
| Binomiale | p (probabilité) |
| Poisson | λ (lambda) |

---

## 4. Fonctionnalités

- Choix de 4 distributions probabilistes
- Paramètres personnalisables (λ, p)
- Histogramme des moyennes d'échantillons
- Courbe normale théorique superposée
- Affichage des stats : moyenne, écart-type

---

## 5. Auteurs

- **Khalil Mohamed Chihaoui** 
