# potiron
Utilitaire de manipulation du langage naturel.

Potiron est programmé en python3 et utilise les packages suivants :
* json (pour la sérialisation de certaines données)
* sqlite3 (pou la manipulation de DB)

La documentation et beaucoup de commentaires sont en français, 
parce que Potiron ne manipule que du français.

L'image de potiron est libre de droits et provient de Pixabay.

Potiron est encore en développement. Il ne comporte pas d'interface graphique,
mais il est possible de le tester avec le fichier demo.py.

Le fichier demo.py permet de produire facilement des sonnets. Cela peut
prendre plusieurs secondes, voire une demi-minute dans les pires cas, et
la procédure peut échouer si Potiron ne parvient pas à écrire des 
alexandrins corrects. Un échec est symptomatique d'un manque de vocabulaire.

Le processus interne est asez non-déterministe pour que deux
sonnets sur le même thème ne soient jamais identiques (et même très différents).

Pour résumer, donc, lancez :
python3 demo.py sonnet random

Pour écrire un sonnet sur un domaine particulier (la liste provient du DEM,
et est disponible dans doms.txt), lancez :
python3 demo.py sonnet (votre domaine)

Potiron est en libre téléchargement sous licence LGPL, car il utilise des données
sous licence LGPL. Plus d'informations dans la documentation du package lexicon.

Potiron ne peut actuellement pas faire grand-chose d'autre qu'écrire des poèmes,
car il n'est pas distribué avec un POS tagger.

En cas de bug ou d'alexandrin mal formé (cela arrive régulièrement, car
le compte sur lequel se base Potiron comporte des bugs et des omissions),
n'hésitez pas à me contacter directement sur WattPad.
