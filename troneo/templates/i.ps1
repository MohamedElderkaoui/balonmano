$filenames = @(
    "player_list.html",
    "player_detail.html",
    "player_form.html",
    "player_confirm_delete.html",
    "trainer_list.html",
    "trainer_detail.html",
    "trainer_form.html",
    "trainer_confirm_delete.html",
    "team_list.html",
    "team_detail.html",
    "team_form.html",
    "team_confirm_delete.html",
    "party_list.html",
    "party_detail.html",
    "party_form.html",
    "match_confirm_delete.html",
    "classification_list.html",
    "classification_detail.html"
)

foreach ($filename in $filenames) {
    $title = $filename -replace '\.html$', ''  # Remove ".html" extension
    $content = @"
{% extends 'base.html' %}

{% block title %} $title-{{ title }}{% endblock %}

{% block style %}{% endblock %}

{% block content %}{% endblock %}
{% block title2 %}{{ title2 }}{% endblock %}
{% block style %}
<style>
     /* Add custom styles if needed */
</style>
{% endblock %}

{% block content %}{% endblock %}
{% block script %}{% endblock %}
"@
    $content | Set-Content $filename
    Write-Host "Created $filename"
}
