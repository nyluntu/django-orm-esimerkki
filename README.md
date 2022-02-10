# Django ORM esimerkkiprojekti

Django projekti luotu komennolla: `docker-compose run webdjango django-admin startproject ormesimerkki .`

Projektin saa käyntiin seuraavin komennoin.

```
# Docker ympäristön pystyttäminen
docker-compose build
docker-compose up -d

# tämän jälkeen kopioi tietokannan asetukset
cp example-mydb.conf mydb.conf
```

Tietokantamuutosten luominen ja päivittäminen.

```
docker-compose run webdjango python manage.py makemigrations
docker-compose run webdjango python manage.py migrate
```

Pääkäyttäjän luominen.

```
docker-compose run webdjango python manage.py createsuperuser
```

