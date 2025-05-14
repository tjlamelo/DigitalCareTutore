#!/bin/bash

# Nom de l'application Django
APP_NAME="dme"

# Dossier des templates
TEMPLATE_DIR="${APP_NAME}/templates/${APP_NAME}"

# Création du dossier si nécessaire
mkdir -p "$TEMPLATE_DIR"

# Liste des modèles à générer
MODELS=("allergie" "antecedent" "mesure" "vaccination" "consultation" "hospitalisation")

# Fonction pour générer un template de liste
generate_list_template() {
    MODEL=$1
    FILE="${TEMPLATE_DIR}/liste_${MODEL}s.html"
    cat > "$FILE" <<EOL
{% extends "base.html" %}
{% block title %}Liste des ${MODEL}s{% endblock %}
{% block content %}
<h2>Liste des ${MODEL}s</h2>
<ul>
  {% for item in ${MODEL}s %}
    <li>
      {{ item }}
      <a href="{% url 'modifier_${MODEL}' dossier.id item.id %}">Modifier</a>
      <a href="{% url 'supprimer_${MODEL}' dossier.id item.id %}">Supprimer</a>
    </li>
  {% endfor %}
</ul>
<a href="{% url '${MODEL}_form' dossier.id %}">Ajouter un(e) nouveau(x) ${MODEL}</a>
{% endblock %}
EOL
}

# Fonction pour générer un template de formulaire
generate_form_template() {
    MODEL=$1
    FILE="${TEMPLATE_DIR}/${MODEL}_form.html"
    cat > "$FILE" <<EOL
{% extends "base.html" %}
{% block title %}{% if item %}Modifier le(la) ${MODEL}{% else %}Nouveau(elle) ${MODEL}{% endif %}{% endblock %}
{% block content %}
<h2>{% if item %}Modifier{% else %}Ajouter{% endif %} un(e) ${MODEL}</h2>
<form method="post">
  {% csrf_token %}
  <label>Nom :</label>
  <input type="text" name="nom" value="{{ item.nom|default:'' }}" required><br><br>

  <label>Gravité :</label>
  <select name="gravite">
    {% for name, value in gravite_allergies %}
      <option value="{{ name }}" {% if item.gravite == name %}selected{% endif %}>{{ value }}</option>
    {% endfor %}
  </select><br><br>

  <button type="submit">Enregistrer</button>
</form>
{% endblock %}
EOL
}

# Spécifique aux antécédents médicaux
generate_antecedent_form() {
    FILE="${TEMPLATE_DIR}/antecedent_form.html"
    cat > "$FILE" <<EOL
{% extends "base.html" %}
{% block title %}{% if antecedent %}Modifier l'antécédent{% else %}Nouvel antécédent{% endif %}{% endblock %}
{% block content %}
<h2>{% if antecedent %}Modifier{% else %}Ajouter{% endif %} un antécédent médical</h2>
<form method="post">
  {% csrf_token %}
  <label>Description :</label>
  <textarea name="description" required>{{ antecedent.description|default:'' }}</textarea><br><br>

  <label>Type d'antécédent :</label>
  <select name="type_antecedent">
    {% for name, value in types_antecedents %}
      <option value="{{ name }}" {% if antecedent.type_antecedent == name %}selected{% endif %}>{{ value }}</option>
    {% endfor %}
  </select><br><br>

  <label>Date :</label>
  <input type="date" name="date" value="{{ antecedent.date|date:"Y-m-d"|default:'' }}"><br><br>

  <button type="submit">Enregistrer</button>
</form>
{% endblock %}
EOL
}

# Spécifique aux mesures cliniques
generate_mesure_form() {
    FILE="${TEMPLATE_DIR}/mesure_form.html"
    cat > "$FILE" <<EOL
{% extends "base.html" %}
{% block title %}{% if mesure %}Modifier la mesure{% else %}Nouvelle mesure{% endif %}{% endblock %}
{% block content %}
<h2>{% if mesure %}Modifier{% else %}Ajouter{% endif %} une mesure clinique</h2>
<form method="post">
  {% csrf_token %}
  <label>Taille (cm) :</label>
  <input type="number" step="0.1" name="taille" value="{{ mesure.taille|default:'' }}"><br><br>

  <label>Poids (kg) :</label>
  <input type="number" step="0.1" name="poids" value="{{ mesure.poids|default:'' }}"><br><br>

  <label>Pression artérielle :</label>
  <select name="pression_arterielle">
    {% for name, value in pressions_arterielles %}
      <option value="{{ name }}" {% if mesure.pression_arterielle == name %}selected{% endif %}>{{ value }}</option>
    {% endfor %}
  </select><br><br>

  <button type="submit">Enregistrer</button>
</form>
{% endblock %}
EOL
}

# Spécifique aux vaccinations
generate_vaccination_form() {
    FILE="${TEMPLATE_DIR}/vaccination_form.html"
    cat > "$FILE" <<EOL
{% extends "base.html" %}
{% block title %}{% if vaccination %}Modifier la vaccination{% else %}Nouvelle vaccination{% endif %}{% endblock %}
{% block content %}
<h2>{% if vaccination %}Modifier{% else %}Ajouter{% endif %} une vaccination</h2>
<form method="post">
  {% csrf_token %}
  <label>Nom du vaccin :</label>
  <input type="text" name="nom_vaccin" value="{{ vaccination.nom_vaccin|default:'' }}" required><br><br>

  <label>Date de vaccination :</label>
  <input type="date" name="date_vaccination" value="{{ vaccination.date_vaccination|date:"Y-m-d"|default:'' }}" required><br><br>

  <label>Dose :</label>
  <input type="text" name="dose" value="{{ vaccination.dose|default:'' }}"><br><br>

  <button type="submit">Enregistrer</button>
</form>
{% endblock %}
EOL
}

# Spécifique aux consultations
generate_consultation_form() {
    FILE="${TEMPLATE_DIR}/consultation_form.html"
    cat > "$FILE" <<EOL
{% extends "base.html" %}
{% block title %}{% if consultation %}Modifier la consultation{% else %}Nouvelle consultation{% endif %}{% endblock %}
{% block content %}
<h2>{% if consultation %}Modifier{% else %}Ajouter{% endif %} une consultation</h2>
<form method="post">
  {% csrf_token %}
  <label>Motif de consultation :</label>
  <input type="text" name="motif_consultation" value="{{ consultation.motif_consultation|default:'' }}" required><br><br>

  <label>Traitement prescrit :</label>
  <textarea name="traitement_prescrit">{{ consultation.traitement_prescrit|default:'' }}</textarea><br><br>

  <button type="submit">Enregistrer</button>
</form>
{% endblock %}
EOL
}

# Spécifique aux hospitalisations
generate_hospitalisation_form() {
    FILE="${TEMPLATE_DIR}/hospitalisation_form.html"
    cat > "$FILE" <<EOL
{% extends "base.html" %}
{% block title %}{% if hospitalisation %}Modifier l'hospitalisation{% else %}Nouvelle hospitalisation{% endif %}{% endblock %}
{% block content %}
<h2>{% if hospitalisation %}Modifier{% else %}Ajouter{% endif %} une hospitalisation</h2>
<form method="post">
  {% csrf_token %}
  <label>Date d'admission :</label>
  <input type="datetime-local" name="date_admission" value="{{ hospitalisation.date_admission|date:"Y-m-d\TH:i"|default:'' }}" required><br><br>

  <label>Date de sortie :</label>
  <input type="datetime-local" name="date_sortie" value="{{ hospitalisation.date_sortie|date:"Y-m-d\TH:i"|default:'' }}"><br><br>

  <label>Motif d'hospitalisation :</label>
  <input type="text" name="motif_hospitalisation" value="{{ hospitalisation.motif_hospitalisation|default:'' }}" required><br><br>

  <button type="submit">Enregistrer</button>
</form>
{% endblock %}
EOL
}

# Génération des templates
echo "Génération des templates dans $TEMPLATE_DIR..."

for MODEL in "${MODELS[@]}"; do
    generate_list_template "$MODEL"
done

generate_form_template "allergie"
generate_antecedent_form
generate_mesure_form
generate_vaccination_form
generate_consultation_form
generate_hospitalisation_form

echo "✅ Templates générés avec succès !"