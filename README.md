# Assonance

Tämä on Helsingin yliopiston tsoha-harjoitustyökurssissa kehitetty web-sovellus. 

## Sovelluksen tarkoitus

Assonance-sovelluksen tarkoituksena on luoda web-portaali, jonka avulla sekä bändit että muusikot pystyvät löytämään sopivan seuran soittamiseen. 

## Demo (toistaiseksi ei ole saatavilla)

**https://assonance.herokuapp.com/**

## Kirjautuminen järjestelmävalvojana
 
 - Email: admin@test.com
 - Salasana: admin

 ## Sovelluksen asentaminen 

- Asenta ja konfiguroi PostgreSQL. Latausopas sopivalle käyttöjärjestelmälle löytyy [täältä].
- Kloonaa repon komennolla `git clone https://github.com/IlmastMaksim/assonance.git`
- Siirty juurihakemistoon
- Tietokannassa käytetyt taulut löytyvät tiedostosta `schema.sql`. Määrittele niitä PostgreSQL-tulkin tai pgAdminin avulla. [Tässä on hyvät ohjeet]
- Luo virtuaaliympäristön `python3 -m venv venv`
- Käytä aktivointikomentoa `source venv/bin/activate`
- Asenta kaikki tarvittavat paketit `pip install -r requirements.txt`
- Luo `.env`-tiedosto ja kirjoita sinne seuraavat ympäristömuuttujat:

| Avainsana | Arvo |
| ------ | ------ |
| DATABASE_URL  | postgresql://${username}:${password}@${host}:${port}/${database} |
| SECRET_KEY | ${YOUR_SECRET_KEY} |
| FLASK_APP | app |
| FLASK_ENV | development |
| ADMIN_NAME | ${YOUR_ADMIN_NAME} |
| ADMIN_EMAIL | ${YOUR_ADMIN_EMAIL} |
| ADMIN_PASSWD | ${YOUR_ADMIN_PASSWD} |
- Suorita `flask run` jotta käynnistää sovelluksen
- Mene osoitteen `localhost:5000` selaimessa.

## Toiminnallisuus

- ✅ Käyttäjä voi läpäistyä rekisteröitymisen joko bändi- tai muusikkokäyttäjänä. 
- ✅ On mahdollista myös kirjautua sisään admin-käyttäjänä.
- ✅ Admin-käyttäjä hallitsee sovelluksen sisältöä poistamalla ilmoituksia, jotka vaikka loukkaavat käyttönotton sääntöjä.
- ✅ Bändikäyttäjä pystyy luomaan ja julkaisemaan sovellukseen ilmoituksia muusikon hausta, joihin voi kuulua: 
    - Muusikon soittama musiikki-instrumentti
    - Musiikkityylit, joissa bändi soittaa
    - Sijainti
    - Bändin kuvaus
    - Yhteystiedot
    - Päivämäärä, jona ilmoitus oli julkaistu
- ✅ Muusikkokäyttäjä pystyy luomaan ja julkaisemaan sovellukseen ilmoituksia bändin hausta, joihin voi kuulua:
    - Mitä musiikki-instrumenttia muusikko osaa soittaa
    - Mieluiset musiikkityylit
    - Sijainti
    - Muusikon luonnen kuvaus
    - Yhteystiedot
    - Päivämäärä, jona ilmoitus oli julkaistu
- ✅ Bändi/muusikko voi vastata sopivaan ilmoitukseen hakemuksen muodossa.
- ✅ Silloin kun sopiva bändi/musiikko on löytänyt ilmoituksen voi piilota.
- ✅ Ilmoituksia voi selata
- ✅ Ilmoituksia voi selata myös käyttäen suodatusta. 

[täältä]: <https://www.postgresql.org/download/>
[Tässä on hyvät ohjeet]: <https://www.javatpoint.com/postgresql-create-table>