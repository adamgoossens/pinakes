#!/bin/bash
set -e
export DJANGO_SETTINGS_MODULE=ansible_catalog.settings.defaults
export ANSIBLE_CATALOG_ALLOWED_HOSTS="*"
export ANSIBLE_CATALOG_DEBUG="True"
echo -e "\e[34m >>> Seed Kaycloak data \e[97m"
ansible-playbook -vvv tools/keycloak_setup/dev.yml
echo -e "\e[34m >>> Migrating changes \e[97m"
python manage.py migrate
echo -e "\e[32m >>> migration completed \e[97m"

echo -e "\e[32m >>> Create Source object\e[97m"
python manage.py shell < tools/minikube/scripts/initialize_source.py

echo -e "\e[32m >>> Fetch UI tar\e[97m"
curl -o ui.tar.xz https://raw.githubusercontent.com/lgalis/ansible-catalog-ui-build/main/ui.tar.xz
tar -xf ui.tar.xz --directory ansible_catalog/ui

echo -e "\e[34m >>> Start development server \e[97m"
python manage.py runserver 0.0.0.0:8000
