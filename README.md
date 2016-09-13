## Sputnik

## Projet de ballon stratosphétique
### Description

Le but du projet est d'envoyer un ballon dans le proche-espace, entre 25 et 30km d'altitude, avec une charge utile scientifique. La charge utile sera composée de : 

- Un nano-ordinateur embarqué : Raspberry Pi 1 model A;
- Un GPS NEO-6;
- Un modem 3G;
- Une caméra 1080p : caméra Raspberry Pi;
- Une carte d'acquisition de données analogiques : Température, pression;
- Batteries : pack USB 6000mAh.

### Fonctions

#### BDD
Base de données mySQL qui contient les données du vol.

BDD Sputnik
Tables :
- Status (timestamp, Frontend, GPS, Hubble, Laïka)
- ScienceMonsta (timestamp, température, pression)
- GPS (timestamp, latitude, longitude, altitude, nb_sat, vitesse)
- Hubble_video (timestamp, path)
- Hubble_image (timestamp, image)

#### Frontend
Communication par SMS, envoie de données télémétriques, commandes Shell.

Commandes Shell :
- ``ping`` -> ``pong.``
- ``reboot``
- ``status`` -> Envoie l'état des sous-systèmes
- ``autodestruct`` -> ``nope.``
- ``beaconmode`` -> uniquement envoi de position GPS par SMS

#### GPS
Module qui décortique l'information fournie par le GPS (UART), envoi vers BDD.

#### Hubble
Capture d'images et de vidéos à intervalles définis, envoi vers BDD.

#### Laïka
Watchdog qui s'assure que les processus sont en marche.

#### ScienceMonsta
Module qui acquiert la température et la pression, envoi vers BDD.

### Général

#### Tâches :

- [x] Achat du ballon;
- [x] Achat du parachute;
- [ ] Achat de la bonbonne d'hélium;
- [ ] Planifier les pratiques générales.
 
