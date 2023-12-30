# YouTube Downloader

Dit Python-programma stelt gebruikers in staat om video's van YouTube te downloaden als MP4-bestanden of audio als MP3-bestanden, en slaat informatie op over de gedownloade video's en audio in een SQLite-database.

## Inhoudsopgave
- [Doel van het programma](#Doel-van-het-programma)
- [Waarom dit programma?](#Waarom-dit-programma?)
- [Functionaliteiten](#Functionaliteiten)
- [Installatie](#installatie)
- [Gebruik](#gebruik)
- [Database](#database)
- [Rapport](#rapport)

## Doel van het programma

Deze applicatie is bedoeld om gebruikers in staat te stellen video's en audio van YouTube te downloaden op een snelle en veilige manier. Dit helpt bij het vermijden van advertenties, onderbroken verbindingen en biedt een veilige manier om bestanden op te slaan voor offline gebruik.

## Waarom dit programma?

Als actieve gebruiker van YouTube, merkte ik vaak dat het bekijken van video's met advertenties frustrerend kon zijn en soms was de verbinding niet stabiel genoeg. Om deze redenen begon ik soms liedjes te downloaden om ze zonder onderbrekingen te kunnen beluisteren. Helaas waren de meeste websites voor het downloaden van YouTube-video's of audio's niet alleen vol advertenties, maar ook onveilig. Bovendien had ik soms de behoefte om video's te bewerken en editeren, dus zocht ik naar een veiligere en snellere oplossing om video's en audio te downloaden van YouTube.

## Functionaliteiten

- Downloaden van video's als MP4-bestanden.
- Extractie van audio en opslaan als MP3-bestanden.
- Registratie van informatie zoals titel, grootte en duur in een SQLite-database.
- Genereren van rapporten in Excel-formaat van de gedownloade bestanden.

## Installatie

1. Zorgen dat Python geïnstalleerd is.
2. De repository clonen naar de lokale machine.
3. Een virtuele omgeving maken met `python -m venv project_env`.
4. De virtuele omgeving activeren:
    - Windows: `project_env\Scripts\activate`
    - Unix of MacOS: `source project_env/bin/activate`
5. De vereiste packages installeren met `pip install -r requirements.txt`.

## Gebruik

Voer `python url_downloader.py` uit en volg de instructies op het scherm. Geef een YouTube-URL op en kies het gewenste formaat (mp4 of mp3) om te downloaden.

<img width="430" alt="image" src="https://github.com/FatimaVives/Python_opdracht/assets/115084288/51bb432b-9fd3-41a6-ae11-36bc97a52726">



## Database

De applicatie maakt gebruik van een SQLite-database. De database wordt gegenereerd in het programma en slaat informatie op over de gedownloade video's en audio.

## Rapport

Om een rapport te genereren van de gedownloade video's en audio, voer `python import_excel.py` uit. Het rapport wordt opgeslagen als 'videos_report.xlsx'.
