"""
@file src/parsers/syllabes_data.py
@version 1.1
@author CN
@author Gudule
@date jan 2017

Données utilisées pour la découpe en syllabes.

@see syllabes.py
"""

#=========================
# Voyelles reconnues par le versificateur
#=============================

VOYELLES = "aeiouyâàäéèêëùûüîïôöœÿ"

#=========================
# Motifs  à une ou deux syllabes
#==========================

def recognize_pat(l, i, pats):
    gr = l[i]
    for pat in pats:
        if type(pat) == list:
            if len(pat) == 2:
                if i > 0:
                    if pat[1] == gr and l[i-1].endswith(pat[0]):
                        return True
            elif len(pat) == 3:
                if pat[2] is None:
                    if i == len(l) - 1:
                        if pat[1] == gr and l[i-1].endswith(pat[0]):
                            return True
                elif i < len(l) - 1:
                    if (pat[1] == gr
                        and l[i-1].endswith(pat[0])
                        and l[i+1].startswith(pat[2]) ):
                        return True
        else:
            if pat == gr:
                return True
    return False

#=========================
# Motifs de synérèses (sauf exceptions)
# Il y a trois types de motifs :
# un motif seul ("au") signifie qu'on ne fait jamais de diérèse
# un motif à deux entrées ("g", "ue") signifie qu'on fait pas la dièrese lorsque
# le groupe de voyelles est précédé par les consonnes indiquées
# un motif à trois entrées ("q", "ue", None) signifie qu'on ne fait pas la diérèse
# lorsque le groupe de voyelles du milieu est précédé par les consonnes indiquées
# (potentiellement rien de spécial) et suivi par les consonnes indiquées
# (potentiellement None ce qui signifie une fin de mot)
#=========================

ONE = [
"ai", "aô", "au", "aî", "aie", "oî",
"eau", "ei", "eu",
"ou", "oû", "où",
"oi", "uu", "eâ",
"uay", "œi", "œu", "oeu", "ui",
["g", "ue"], ["g", "uei"], ["g", "uai"], ["g", "ua"],
 ["g", "eaie"], ["g", "eai"],
["g", "ueu"], ["q", "ueu"], ["g", "uée"], ["q", "uée"],
["g", "uè"], ["g", "uê"], ["g", "ué"],
["q", "ue"], ["q", "ua"], ["q", "uà"], ["q", "uê"], ["q", "ué"], ["q", "uai", ""],
["q", "uaie"],
["q", "uoi"],
"yeu",
["", "oui", "ll"], ["", "oue", None], ["", "ie", None], ["", "ie", "s"],
["", "aye", None], ["", "ue", None], "ée",
"oie" # feuillu
# ("iè"), ["ie", "l"],
# ["ie", "ll"], ["iè", "m"], ["ière", None],
]


TWO = [
["dr", "ie", "z"], ["tr", "ie", "z"],
["pr", "ie", "z"], ["pr", "ie", "r"], ["pl", "ie", "r"], ["pl", "ie", "z"],
["br", "io"], ["tr", "io"], ["cl", "ie", ""], ["tr", "iè"], ["dr", "ie", "r"],
["br", "ie", "n"], # précambrien
["dr", "io"], ["vr", "io"], ["gr", "io"], ["bl", "io"], ["bl", "ié"],
["pr", "ieu"], ["dr", "ieu"],
["vr", "ie", "r"], ["tr", "ie", "r"], ["bl", "ie"], ["bl", "iè"], ["bl", "ia"],
["pl", "ia"], ["cr", "ié"], ["pl", "iée"], ["fr", "ia"], ["fr", "io"], ["tr", "ua"],
["tr", "ia"], ["cr", "iè"], ["pr", "ié"], ["fl", "oué"],
["tr", "ie", "l"], ["tr", "ieu"], ["pl", "ieu"], ["bl", "ieu"],
["tr", "ué"], ["pl", "iai"], ["pl", "io"], ["pl", "iè"], ["pl", "ié"],
# ["", "ée", "ss"],
"oya", "oyé", "oyo", "oyaie", "oyai", "oyè", "oyeu", "oyée", "oyau",
"oyu", "oyie", "oyio",
"éo", "éai", "éa", "éé",
["", "ée", "n"], ["", "ée", "m"], ["", "ée", "ss"], ["", "ée", "x"],
"oï", "oye", "éi", "oa", "aé", "oai", "oé",
["oue", "r"], ["oue", "z"],
"éai", "éaie",
"ayé", "ayè", ["z", "oo"],  "aï",
"ayion", "ayâ", "ayée", ["ay", "s"],
"ayeu", "ayaie", "ayai", "aya", "aou", "ayée", "ayâ", "ayo", "ayu",
"uye", "uya", "uyè", "uyâ", "uyé", "uyau", ["", "yo", "n"], "uyaie",
"uyeu", #ennuyeux
"uo", # fluorescent
"ioa", #radioastronome
"ioé", #radioélectrique
"iaie", "éâ", "oau", # coauteur
"iai", #priait
"oueu", # éboueur
"ueu", # monstrueux
"iée", # oubliée
"ouai" # rabrouait
]

#=========================
# Exceptions aux motifs
#=======================

_EXCEPT_TWO = ["bleui", "baobab", "bluet", "brouet", "chao", "cryog", "coex", # coexister
"extraordinaire", "karaoké", "intraoculaire", "pharaon", "ébloui", "ruade",
"réussi", "réuni", "réuti", "alléluia", "influen", "affluen", "tuyau", "irréel", "réel",
"idéel", "idéaux", "gruau", "gluant", "influai", "incluai", "obstruai", "rabroué", "paranoïa",
"voyou", "maestro", "cacatoès", "aède", "fedayin", "maïa", "youyou"
]


_EXCEPT_ONE = [
"amitié", "châtié", "inanitié", "inimitié", "initié", "moitié", "pitié",
"faon", "taon", "laon", "paon", "aaron", "août", "saoûl", "saoul",
"fiacre", "diacre", "diable", "piaf", "bréviaire", "aviaire", "ferroviaire",
"viande", "diantre",
"pied", "messied", "assied",
"bief", "relief", "briefing",
"ciel", "fiel", "miel",
"bielle", "nielle",
"deuxième", "troisième",
"tien", "mien", "sien", "chien", "bien", "rien", "vien",
"gardien", "paroissien",
"batelier", "collier", "fumier", "guerrier", "herbier",
"laurier", "palmier", "portier", "dernier", "familier", "premier",
"avant-hier", "concierge", "tiers", "vierge", "acquiert",
"lierre", "pierre", "miette", "assiette","pieu",
 "pieux", "essieu", "essieux", "mieux", "monsieur",
"vieux", "lieu", "lieux",
"aimiez", "seriez", "finissiez", "croiriez", "teniez",
"surlier", "perlier",
"parliez", "ferliez", "perliez", "hurliez", "ourliez",
"aimiez", "seriez", "finissiez", "croiriez", "teniez",
"fiole", "kiosque", "mioche", "pioche",
"aimions", "serions", "finissions", "croirions", "tenions",
"surlions", "ferlions", "perlions", "hurlions", "ourlions",
"moelle", "poêle",
"douan", "ouais", "ouest", "fouet",
"juan", "duègne", "écuelle", "suint", "croître",
"oui",
# "relayer", ???
# "balayer", "rougeoy",
"espion",
# éliminer certaines graphies
"essayeraient",
"payeraient",
"coach", "goal", "tweed", "dey", "spleen", "aiguë", "gray", "coopt", # cooptation
"deuil", "feuil"
]


_EXCEPT_ONE_2 = [ "fief", "fiefs", "fier", "dieux", "dieu", "cieux", "boy", "boys"]


def _is_in_list(w, l):
    for test in l:
        if w.startswith(test) or w.endswith(test):
            return True
    return False

def is_except_one(word):
    return _is_in_list(word, _EXCEPT_ONE) or word in _EXCEPT_ONE_2

def is_except_two(word):
    return _is_in_list(word, _EXCEPT_TWO)



#============================
# Exceptions pour la diérèse : la compter dans ces mots (précisément)
#=============================

_EXCEPT_DIE = [
"deum", "museum",
"grièche", "grief",
"client",
"inconvénience", "obédience", "patience",
"science", "conscience"
"meurtrière", "ouvrière", "prière", "sablière", "trière",
"inquiet",
"hardiesse", "liesse",
"druide", "fluide", "incongruité", "bruin", "bruir", "ruine", "jouis", "déesse"
]

def is_except_die(word):
    return _is_in_list(word, _EXCEPT_DIE)



#=================================================


def has_e_muet(word, groups):
    """
    Fonction magique qui détermine si un mot se termine par un e muet.

    A priori pas d'exception notable (sauf bien cherchée).
    De toute façon cette fonction n'est pas très utilisée.
    """
    if word in ["que", "lorsque"]:
        return False
    if groups[-1] == "e":
        return True
    elif groups[-1] == "ue":
        for t in ["q", "g"]:
            if groups[-2].endswith(t):
                return True
    return False


#=====================================

#============================
# Mots qui sont ambigus pour la syll muette
# Il faudrait voir en contexte, avec le POS
#================================

_AMBIGUS = [
"affluent", "confluent", "congruent", "convergent", "coïncident", "couvent", "effluent",
"ferment", "flatulent", "parent", "pressent", "résident", "somnolent", "émergent"
]

#=============================
# Exceptions qui n'ont pas de syllabe muette malgré le fait qu'ils finissent en -ent
#===============================

_EXCEPTIONS_SYLLMUETTE = [
"absent", "abstinent", "accent", "accident", "adjacent",
"agent", "ambivalent", "apparent", "ardent", "ardûment",
"argent", "arpent", "assidûment", "astringent", "auvent",
"avent",
"cent", "chiendent", "coefficient", "comment",
"compétent", "concupiscent", "concurrent", "confident",
"congrûment", "consent", "conséquent", "content",
"continent", "contingent", "continûment", "contrevent",
"convent", "corpulent", "covalent", "crûment",
"dent", "diligent", "dissident", "divergent",
"dolent", "décadent", "détergent", "dûment",
"engoulevent", "entregent", "establishment",
"event", "excellent",  "fervent", "filament", "firmament",
"flatulent", "fluorescent", "fragment", "froment", "fréquent", "féculent",
"gaîment", "gent", "goulûment", "grandiloquent",
"immanent", "imminent", "impeachment",
"impertinent", "impotent", "imprudent", "impudent",
"impénitent", "incident", "incompétent",
"inconséquent", "incontinent", "indigent", "indolent",
"indulgent", "indûment", "inintelligent", "innocent", "insolent", "intelligent",
"intermittent", "latent", "lent", "ligament", "malcontent", "ment",
"moment", "monofilament", "mécontent", "médicament", "négligent", "occident",
"omnipotent", "omniprésent", "onguent", "opulent", "paravent", "parent",
"patent", "permanent", "pertinent", "pigment", "polyvalent", "pourcent",
"proéminent","prudent", "présent", "président", "pschent",
"purulent", "pénitent",  "relent", "repent", "ressent",
"récurrent", "régent", "rémanent", "résident", "sanguinolent",
"sarment", "segment", "sent", "sergent", "serment", "serpent",
"souvent", "strident", "subséquent", "succulent", "talent",
"tangent", "tempérament", "testament", "torrent", "tourment",
"transparent", "trident", "truculent", "turbulent", "urgent",
"vent", "ventripotent", "violent", "virulent",
"éloquent", "éminent", "équivalent", "évent", "évident"
]

_TERM_MUETTE = [
"ement", "amment", "emment", "ément", "aiement", "iment",
"écent", "icent", "escent", "érent", "édent", "ument", "ement"
]

def has_syll_muette(word, groups):
    """
    Fonction magique qui détermine si la dernière syllabe du mot est muette.

    A priori pas d'exception notable.
    @warning ne résoud pas les cas ambigus
    @todo dans une prochaine version, résoudre toutes les ambiguités
    """
    if has_e_muet(word, groups):
        return True
    for test in _TERM_MUETTE:
        if word.endswith(test):
            return False
    if word in _EXCEPTIONS_SYLLMUETTE or word + "s" in _EXCEPTIONS_SYLLMUETTE:
        return False
    if len(groups) > 2:
        if groups[-1] in ["nt", "s"]:
            if groups[-2] == "e":
                return True
            elif groups[-2] == "ue":
                for t in ["q", "g"]:
                    if groups[-3].endswith(t):
                        return True
    return False

#=========================
# Liste de h aspirés : le compter dans les mots qui commencent par ces motifs
# TODO non complète
#==========================
#
# _H_ASPIRE = [
# "hâble", "hache", "hachette", "hachis", "hachisch", "hashich",
# "hachoir", "hachure","hagard",
# "haie", "haillon", "haine", "haïr", "haï", "hais", "haïra", "haire",
# "halage", "halbran", "halbrener", "hâle", "halener",
# "haletant", "haleter", "haleur", "hall",
# "hallali", "halle", "hallebarde", "hallier",
# "halo", "hâloir", "halot", "halotechnie", "halte"
# "hamadryade", "hameau", "hampe", "han", "hanche",
# "hand-ball", "handicap", "handicaper", "hangar",
# "hanneton", "hanse", "hante", "hantise", "happe",
# "haquenée", "haquet", "hara-kiri", "harangue",
# "haras", "harasser", "harceler", "harcèle",
# "harde", "hardi", "harem", "hareng",
# "harengère", "harengerie", "hargneux",
# "hargner", "haricot", "harnacher", "harnais",
# "haro", "harpagon", "harpe", "harpeau",
# "harpie", "harpon", "hart", "hasard",
# "hase", "hâte", "hâtier", "hâtille",
# "hâtif", "hâtive",  "hauban", "haubert",
# "hausse", "haut",
# "hâve", "havane", "havir", "havre", "heaume",
# "hennir", "henniss",
# "henri", "héraut", "hère", "hériss", "hernie", "herniaire",
# "héron", "héros", "herse", "hêtraie", "hêtre",
# "heurter", "heurtoir", "hibou", "heurt",
# "hic", "hideur", "hideux", "hideuse",
# "hiérarchi", "hisser", "hobereau", "hoc",
# "hoche", "hochement", "hochequeue", "hochepot",
# "hochet", "hocher", "hold-up", "hola",
# "hollande", "hollandais", "homard", "hongre",
# "hongrois", "honte", "hoquet", "hoqueton",
# "horde", "horion", "hors", "hors-bord",
# "hors-d’œuvre", "hors-jeu",
# "hors-la-loi", "hors-série",
# "hotte", "hottentot", "houblon", "houille",
# "houle", "houlette", "houppe", "houleux",
# "houppelande", "hourdage",
# "hourder", "hourra", "hourvari", "houseaux",
# "houspille", "houssage", "houssaie", "housse",
# "houssoir", "houx", "hoyau", "hublot", "huche", "hue",
# "hué", "huer", "huguenot",
# "huhau", "huit", "hulotte",
# "humer", "hurl",
# "hune", "hunier", "huppe", "hure",
# "hurle", "hurle", "hurluberlu", "hussard",
# "hutte", "hyacinthe", "hyalin"
# ]

#==========================
# H aspirés : vient de DEM
#========================

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

H_ASPIRE = set(_H_ASPIRE)

# _H_ASPIRE_2 = [
# "hume", "huma", "héler", "hèle"
# ]
#


def is_h_aspire(word):
    """
    Fonction magique qui détermine si un mot commence par un h aspiré (qu'on prononce).
    """
    # for test in _H_ASPIRE:
    #     if word.startswith(test):
    #         return True
    return word in _H_ASPIRE


if __name__ == "__main__":
    print(is_h_aspire("homme"))
    print(is_h_aspire("humain"))
