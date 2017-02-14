"""
@file src/mutators/formatter.py
@version 1.0
@author CN
@author Gudule
@date fev 2017

Utilitaire permettant de reformater les mots, c'est-à-dire de faire
des élisions et d'espacer correctement les phrases en sortie.

@todo ce fichier contient une liste de h aspirés, mais n peut récupérer
directement cette info dans les LexiconItem.

"""

from lexicon.lexiconitem import LexiconItem


_VOY = "aeouiüïöôûîâàéèùê" # pas le y car il n'intervient pas dans les élisions


_PUNC = {
"?" : " ?",
"!" : " !",
"," : ",",
"." : "."
}

_H_ASPIRE = [
'ha', 'ha', 'habanera', 'hacha', 'hachage',
'hachaient', 'hachait', 'hachant', 'hache', 'hache',
'hache-paille', 'hachent', 'hacher', 'hacherai', 'hacherait',
'haches', 'haches', 'hachette', 'hachettes', 'hacheur',
'hacheurs', 'hachez', 'hachis', 'hachisch', 'hachoir',
'hachoirs', 'hachuraient', 'hachurait', 'hachurant', 'hachure',
'hachuré', 'hachurée', 'hachurées', 'hachurés', 'hachèrent',
'haché', 'hachée', 'hachées', 'hachés', 'hacienda',
'haciendas', 'hacker', 'hackers', 'haddock', 'hadith',
'hadj', 'hagard', 'hagarde', 'hagardes', 'hagards',
'haggis', 'haie', 'haies', 'haillonneuse', 'haillonneux',
'haine', 'haines', 'haineuse', 'haineusement', 'haineuses',
'haineux', 'haire', 'haires', 'haka', 'hakka',
'hala', 'halage', 'halages', 'halaient', 'halait',
'halal', 'halant', 'halent', 'haler', 'haleta',
'haletaient', 'haletais', 'haletait', 'haletant', 'haleter',
'haleté', 'haleur', 'haleurs', 'halez', 'half-track',
'half-tracks', 'hall', 'hallali', 'halle', 'hallebarde',
'hallebardes', 'hallebardier', 'hallebardiers', 'halles', 'hallier',
'halliers', 'halloween', 'halls', 'halo', 'halos',
'halte', 'halte-garderie', 'halter', 'halva', 'halèrent',
'halète', 'halètent', 'halètes', 'halé', 'halée',
'halés', 'hamac', 'hamacs', 'hamada', 'hambourgeois',
'hambourgeois', 'hambourgeoises', 'hamburger', 'hamburgers', 'hameau',
'hameaux', 'hammam', 'hammams', 'hammerless', 'hampe',
'hampes', 'hamster', 'hamsters', 'han', 'han',
'hanap', 'hanaps', 'hanche', 'hanches', 'hanchée',
'handball', 'handicap', 'handicapait', 'handicapant', 'handicape',
'handicaper', 'handicapera', 'handicapeur', 'handicaps', 'handicapé',
'handicapée', 'handicapées', 'handicapés', 'hangar', 'hangars',
'hanneton', 'hannetons', 'hanovrien', 'hanovriens', 'hanta',
'hantaient', 'hantais', 'hantait', 'hantant', 'hantavirus',
'hante', 'hantent', 'hanter', 'hantera', 'hanterai',
'hanterait', 'hanteront', 'hantes', 'hantez', 'hantise',
'hantises', 'hanté', 'hantée', 'hantées', 'hantés',
'happa', 'happai', 'happaient', 'happait', 'happant',
'happe', 'happe', 'happement', 'happening', 'happenings',
'happent', 'happer', 'happerait', 'happy end', 'happy ends',
'happy few', 'happé', 'happée', 'happées', 'happés',
'haquet', 'haquets', 'hara-kiri', 'harangua', 'haranguaient',
'haranguait', 'haranguant', 'harangue', 'harangue', 'haranguer',
'haranguerais', 'harangues', 'haranguez', 'harangué', 'haranguée',
'harangués', 'harari', 'haras', 'harassaient', 'harassant',
'harassant', 'harassante', 'harassantes', 'harassants', 'harasse',
'harassement', 'harassent', 'harasser', 'harassé', 'harassée',
'harassées', 'harassés', 'harcela', 'harcelai', 'harcelaient',
'harcelais', 'harcelait', 'harcelant', 'harcelant', 'harcelante',
'harcelantes', 'harcelants', 'harceler', 'harcelez', 'harceliez',
'harcelèrent', 'harcelé', 'harcelée', 'harcelées', 'harcelés',
'harcèle', 'harcèlent', 'harcèlera', 'harcèlerai', 'harcèleraient',
'harcèlerez', 'harcèlerons', 'harcèleront', 'hard', 'hard',
'hard-top', 'harde', 'hardent', 'harder', 'hardes',
'hardiesse', 'hardiesses', 'hardiment', 'harem', 'harems',
'hareng', 'harengs', 'harenguet', 'harenguier', 'haret',
'harfang', 'hargne', 'hargnes', 'hargneuse', 'hargneusement',
'hargneuses', 'hargneux', 'haricot', 'haricots', 'haridelle',
'haridelles', 'harissa', 'harki', 'harkis', 'harmattan',
'harnacha', 'harnachaient', 'harnachais', 'harnachait', 'harnachement',
'harnachements', 'harnacher', 'harnachiez', 'harnachèrent', 'harnaché',
'harnachée', 'harnachées', 'harnachés', 'harnais', 'haro',
'harpe', 'harper', 'harpes', 'harpie', 'harpies',
'harpions', 'harpiste', 'harpon', 'harponna', 'harponnage',
'harponne', 'harponnent', 'harponner', 'harponnera', 'harponneur',
'harponneurs', 'harponné', 'harponnée', 'harponnés', 'harpons',
'harpyes', 'hart', 'harts', 'has been', 'hasard',
'hasarda', 'hasardai', 'hasardaient', 'hasardais', 'hasardait',
'hasardant', 'hasarde', 'hasardent', 'hasarder', 'hasardera',
'hasarderais', 'hasardeusement', 'hasards', 'hasardé', 'hasardée',
'hasch', 'haschich', 'hase', 'hases', 'hassidim',
'hassidique', 'hassidisme', 'hauban', 'haubans', 'haubanée',
'haubanés', 'haubert', 'haussa', 'haussai', 'haussaient',
'haussais', 'haussait', 'haussant', 'hausse', 'hausse',
'haussement', 'haussements', 'haussent', 'hausser', 'hausserait',
'hausses', 'hausses', 'haussez', 'haussier', 'haussière',
'haussons', 'haussât', 'haussèrent', 'haussé', 'haussée',
'haussées', 'haussés', 'haut', 'haut', 'haut',
'haut-commissaire', 'haut-commissariat', 'haut-de-forme', 'haut-fond', 'haut-le-coeur',
'haut-le-corps', 'haut-parleur', 'haut-parleurs', 'haut-relief', 'hautain',
'hautain', 'hautaine', 'hautainement', 'hautaines', 'hautains',
'hautains', 'hautbois', 'haute', 'hautement', 'hautes',
'hauteur', 'hauteurs', 'hautin', 'hautins', 'hauts',
'hauts', 'hauts-commissaires', 'hauts-de-forme', 'hauts-fonds', 'hauts-fourneaux',
'havanais', 'havane', 'havane', 'havanes', 'have',
'haveneau', 'haveneaux', 'haver', 'haves', 'havrais',
'havresac', 'havresacs', 'hayon', 'hayons', 'heaume',
'heaumes', 'hein', 'hello', 'hem', 'hennin',
'hennir', 'hennirent', 'hennissaient', 'hennissait', 'hennissant',
'hennissant', 'hennissantes', 'hennissement', 'hennissements', 'hennissent',
'hennit', 'henry', 'hep', 'herniaire', 'herniaires',
'hernie', 'hernies', 'hernieux', 'hersait', 'herse',
'herser', 'herses', 'hersé', 'hersés', 'hertz',
'hertzienne', 'hertziennes', 'hertziens', 'hessois', 'hessois',
'hessoise', 'heu', 'heurt', 'heurta', 'heurtai',
'heurtaient', 'heurtais', 'heurtait', 'heurtant', 'heurte',
'heurtent', 'heurter', 'heurtera', 'heurterai', 'heurteraient',
'heurterait', 'heurterions', 'heurtez', 'heurtions', 'heurtoir',
'heurtoirs', 'heurtons', 'heurts', 'heurtât', 'heurtèrent',
'heurté', 'heurtée', 'heurtées', 'heurtés', 'hi-han',
'hi-han', 'hibou', 'hiboux', 'hic', 'hic et nunc',
'hickory', 'hideur', 'hideurs', 'hideuse', 'hideusement',
'hideuses', 'hideux', 'hier', 'highlander', 'highlanders',
'hilaire', 'hile', 'hindi', 'hip', 'hissa',
'hissai', 'hissaient', 'hissais', 'hissait', 'hissant',
'hisse', 'hissent', 'hisser', 'hissera', 'hisserai',
'hissez', 'hissons', 'hissâmes', 'hissèrent', 'hissé',
'hissée', 'hissées', 'hissés', 'hit', 'hit-parade',
'hit-parades', 'hits', 'hittite', 'hittite', 'hittites',
'ho', 'hobbies', 'hobby', 'hobereau', 'hobereaux',
'hochepot', 'hochet', 'hochets', 'hockey', 'hockeyeur',
'hockeyeurs', 'hold up', 'hold-up', 'holding', 'holdings',
'hollandais', 'hollandais', 'hollandaise', 'hollandaise', 'hollandaises',
'hollandaises', 'hollande', 'hollywoodien', 'hollywoodienne', 'hollywoodiennes',
'hollywoodiens', 'holster', 'homard', 'homardiers', 'homards',
'hombre', 'home', 'home-trainer', 'homeland', 'homes',
'hondurien', 'hondurien', 'hongkongais', 'hongre', 'hongre',
'hongres', 'hongres', 'hongrois', 'hongrois', 'hongroise',
'hongroises', 'honni', 'honnie', 'honnir', 'honnis',
'honnissait', 'honnissant', 'honnissent', 'honnit', 'honoris causa',
'honte', 'hontes', 'honteuse', 'honteusement', 'honteuses',
'honteux', 'hop', 'hopak', 'hoquet', 'hoqueta',
'hoquetai', 'hoquetais', 'hoquetait', 'hoquetant', 'hoqueter',
'hoquetons', 'hoquets', 'hoquette', 'hoqueté', 'horion',
'horions', 'hormis', 'hornblende', 'hors-bord', 'hors-bord',
'hors-piste', 'horse-guard', 'horse-guards', 'hosanna', 'hosannas',
'hot', 'hot', 'hot dog', 'hot dogs', 'hotte',
'hotter', 'hottes', 'hotu', 'hotus', 'hou',
'houa', 'houari', 'houblon', 'houblonnés', 'houblons',
'houe', 'houille', 'houiller', 'houilles', 'houle',
'houler', 'houles', 'houlette', 'houleuse', 'houleuses',
'houleux', 'houligan', 'houliganisme', 'houlque', 'houp',
'houppe', 'houppelande', 'houppelandes', 'houppes', 'houppette',
'houppettes', 'hourdis', 'hourds', 'houri', 'houris',
'hourra', 'hourra', 'hourras', 'hourvari', 'hourvaris',
'housards', 'house', 'house-boat', 'house-boats', 'houseau',
'houseaux', 'houspilla', 'houspillaient', 'houspillait', 'houspillant',
'houspille', 'houspillent', 'houspiller', 'houspillâmes', 'houspillèrent',
'houspillé', 'houspillée', 'houspillées', 'houspillés', 'housse',
'housses', 'houssés', 'houx', 'hovercraft', 'hoyau',
'hua', 'huaient', 'huait', 'huant', 'hublot',
'hublots', 'huche', 'huches', 'huchet', 'hue',
'hue', 'huer', 'huerta', 'huez', 'hugolien',
'hugoliens', 'huguenot', 'huguenot', 'huguenote', 'huguenote',
'huguenots', 'huis', 'huit', 'huit-reflets', 'huitaine',
'hulotte', 'hulottes', 'hulula', 'hululaient', 'hululait',
'hululant', 'hulule', 'hululement', 'hululements', 'hululent',
'hululer', 'hululée', 'hum', 'huma', 'humai',
'humaient', 'humais', 'humait', 'humant', 'hume',
'hument', 'humer', 'humeras', 'humez', 'humions',
'humons', 'humèrent', 'humé', 'humée', 'humés',
'hune', 'hunes', 'hunier', 'huniers', 'hunter',
'huppe', 'hure', 'hures', 'hurla', 'hurlai',
'hurlaient', 'hurlais', 'hurlait', 'hurlant', 'hurlant',
'hurlante', 'hurlantes', 'hurlants', 'hurle', 'hurlement',
'hurlements', 'hurlent', 'hurler', 'hurlera', 'hurlerai',
'hurleraient', 'hurlerais', 'hurlerait', 'hurlerez', 'hurleront',
'hurles', 'hurleur', 'hurleur', 'hurleurs', 'hurleurs',
'hurlez', 'hurlions', 'hurlât', 'hurlèrent', 'hurlé',
'hurlée', 'hurlées', 'hurlés', 'huron', 'huron',
'huronne', 'huronne', 'hurrah', 'hurrah', 'hurrahs',
'hurricane', 'hurricanes', 'husky', 'hussard', 'hussarde',
'hussards', 'hussite', 'hussites', 'hutte', 'hutter',
'huttes', 'huèrent', 'hué', 'huée', 'huées', 'hués',
'hyacinthe', 'hyalin'
]

_SENT = "!?:."

def _format_out(out):
    """
    Formate une liste de mots en sortie, renvoie une chaîne de caractères.
    Gère la ponctuation.
    """
    res = ""
    i = 0
    mustupper = True
    while i < len(out):
        if out[i] in _SENT:
            mustupper = True

        if out[i].startswith("-t"):
            res = res + out[i]
            i += 1
        elif out[i] in _PUNC:
            # faire une belle ponctuation
            res = res + _PUNC[out[i]]
            i += 1
        else:
            if mustupper:
                res = res + " " + out[i].title()
                mustupper = False
            else:
                res = res + " " + out[i]
            i += 1

    res = res.replace("' ", "'").replace(" '", "'")
    return res


# def format_out_tagged(tagged):
#     """
#     Takes a list of tagged words and returns a well-formatted text.
#     """
#     # res = list()
#     for i in range(len(tagged)):
#         tagged[i]["out"] = tagged[i]["ortho"].lower()
#         if i < len(tagged) - 1:
#             if tagged[i]["out"] == "de" and tagged[i+1]["out"] == "le":
#                 tagged[i]["out"] = "du"
#                 tagged[i+1]["out"] = ""
#         if i < len(tagged) - 1:
#             if tagged[i]["out"] in ["se", "que", "la", "le", "de", "ne", "je", "me", "te", "se"]:
#                 if tagged[i+1]["out"][0] in _VOY:
#                     tagged[i]["out"] = tagged[i]["out"][:-1] + "'"
#                 elif tagged[i+1]["out"][0] == "h" and tagged[i+1]["out"] not in _H_ASPIRE:
#                     tagged[i]["out"] = tagged[i]["out"][:-1] + "'"
#     return _format_out([d["out"] for d in tagged])


_APOS = {'gram': 'PUN', 'orth': "'"}

_APOS = LexiconItem.from_dict(_APOS)


def format_tagged(lexitems):
    """
    Ne modifie pas sur place ! Renvoie une copie des items de lexique en entrée.

    @todo améliorer le code
    """
    # print( [t["orth"] for t in lexitems] )
    # retirer les mots vides
    res = []
    i = 0
    while i < len(lexitems):
        w = lexitems[i]["orth"].lower()
        tmp = lexitems[i].copy()
        if i < len(lexitems) - 1:
            w2 = lexitems[i+1]["orth"].lower()
            if w == "de" and w2 == "le":
                if i < len(lexitems) - 2 and lexitems[i+2]["orth"].lower()[0] in _VOY:
                    # tmp = lexitems[i].copy()
                    tmp["orth"] = "de l"
                    tmp["count"] = 1 # "hasdie", "syllmuette", "emuet", "haspi"
                    # lexitems[i]["hasdie"] = False
                    res.append(tmp)
                    res.append(_APOS)
                    # words2.append("de l'")
                else:
                    # tmp = lexitems[i].copy()
                    tmp["orth"] = "du"
                    tmp["count"] = 1
                    res.append(tmp)
                    # res.append(_APOS)
                    # words2.append("du")
                i += 2
            # elif w2 == "":
            #
            #     words2.append(w)
            #     i += 2

            elif w == "à" and w2 == "le":
                tmp["orth"] = "au"
                tmp["count"] = 1
                res.append(tmp)
                i += 2
                # words2.append("au")
            elif w == "ce" and w2[0] in _VOY:
                tmp["orth"] = "cet"
                tmp["count"] = 1
                res.append(tmp)
                # words2.append("cet")
                i += 1
            elif w == "sa" and w2[0] in _VOY:
                tmp["orth"] = "son"
                tmp["count"] = 1
                res.append(tmp)
                # words2.append("son")
                i += 1
            elif w == "du" and (w2[0] in _VOY or (w2[0] == "h" and w2 not in _H_ASPIRE)):
                # i += 1
                tmp["orth"] = "de l"
                tmp["count"] = 1
                res.append(tmp)
                res.append(_APOS)
                i += 1
                # words2.append("de l'")
            elif w == "au" and w2[0] in _VOY:
                # i += 1
                tmp["orth"] = "à l"
                tmp["count"] = 1
                res.append(tmp)
                res.append(_APOS)
                i += 1
                # words2.append("à l'")
            elif w in ["se", "que", "la", "le", "de", "ne", "je", "me", "te", "se"]:
                if w2[0] in _VOY or (w2[0] == "h" and w2 not in _H_ASPIRE):
                    tmp["orth"] = w[:-1]
                    tmp["count"] = 0
                    res.append(tmp)
                    res.append(_APOS)
                    # words2.append( + "'")
                else:
                    res.append(tmp)
                    # words2.append(w)
                i += 1
            else:
                res.append(tmp)
                i += 1
        else:
            res.append(tmp)
            i += 1

    # print([t["orth"] for t in res])
    return res


# def format_out(words):
#     """
#     Takes a list of words and returns a text.
#
#     @todo improve the code !
#     """
#     # retirer les mots vides
#     words2 = []
#     i = 0
#     while i < len(words):
#         w = words[i].lower()
#
#         if i < len(words) - 1:
#             w2 = words[i+1].lower()
#             if w == "de" and w2 == "le":
#                 if i < len(words) - 2 and words[i+2].lower()[0] in _VOY:
#                     words2.append("de l'")
#                 else:
#                     words2.append("du")
#                 i += 2
#             elif w2 == "":
#                 words2.append(w)
#                 i += 2
#
#             elif w == "à" and w2 == "le":
#                 i += 2
#                 words2.append("au")
#             elif w == "ce" and w2[0] in _VOY:
#                 i += 1
#                 words2.append("cet")
#             elif w == "sa" and w2[0] in _VOY:
#                 i += 1
#                 words2.append("son")
#             elif w == "du" and (w2[0] in _VOY or (w2[0] == "h" and w2 not in _H_ASPIRE)):
#                 i += 1
#                 words2.append("de l'")
#             elif w == "au" and w2[0] in _VOY:
#                 i += 1
#                 words2.append("à l'")
#             elif w in ["se", "que", "la", "le", "de", "ne", "je", "me", "te", "se"]:
#                 if w2[0] in _VOY or (w2[0] == "h" and w2 not in _H_ASPIRE):
#                     words2.append(w[:-1] + "'")
#                 else:
#                     words2.append(w)
#                 i += 1
#             else:
#                 words2.append(w)
#                 i += 1
#         else:
#             words2.append(w)
#             i += 1
#     return _format_out(words2)

