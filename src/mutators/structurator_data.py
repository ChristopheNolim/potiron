"""
@file src/mutators/structurator_data.py
@version 1.0
@author CN
@author Gudule
@date fev 2017

Données nécessaires au structurateur.

@see mutators/structurator.py

"""

POSSIB = [
[1, 2, 5],
[1, 3, 4],
# [1, 17, 18],
[6],
[6, 4],
[7, 5],
[8],
[9, 10],
# [11, 12],
[13],
[14, 15, 5],
[14, 21, 18],
[14, 16, 4],
[14, 20],
[25, 18],
[26, 27],
[11, 12]
]

LISTS = {
1 : [
"dans le mouton vert, un vert mouton",
"dans les moutons verts, un vert mouton",
"dans le vert mouton, un vert mouton",
"dans les verts moutons, un vert mouton",
"dans les moutons verts, une verte moule",
"dans les verts moutons, une verte moule",
"dans la moule verte, une verte moule",
"dans la verte moule, une verte moule",
"tel un mouton vert, un vert mouton",
"oubliant les moutons, un vert mouton",
"tel un mouton vert, un mouton vert",
"ainsi qu'un mouton, un mouton vert",
"ainsi qu'un mouton, un mouton vert",
"ainsi qu'un mouton, un vert mouton",
"ainsi qu'un mouton, un mouton",
"comme un mouton vert, un mouton vert",
"dans la moule verte, une verte moule",
"telle une moule, une verte moule",
"oubliant les moutons, une verte moule",
"telle une moule verte, une verte moule",
"ainsi qu'une moule, une verte moule",
"comme une moule verte, une moule verte",
"oubliant, oubliant, une verte moule",
"oubliant, oubliant, un vert mouton",
"oubliant lentement, une verte moule",
"oubliant lentement, un vert mouton"
],
2 : [
"oubliait les moutons des moutons verts",
"oubliait lentement les verts moutons",
"oubliait les moules des moutons verts",
"oubliait le mouton des moutons verts"
],
3 : [
"oubliait les moutons du mouton vert",
"oubliait le mouton du mouton vert",
"oubliait le mouton du vert mouton",
"oubliait lentement le mouton vert",
"oubliait les moutons du vert mouton"
],
# "oubliait les moules de la verte moule",
# "oubliait les moules vertes de la moule",
# "oubliait les moules de la moule verte"
# ],
4 : [
"qui, oublié, oubliait les moutons verts",
"qui, oublié, oubliait les verts moutons",
"qui, oublié, oubliait les vertes moules",
"qui, oublié, oubliait les moules vertes",
"qui, oublié, oubliait une moule verte",
"qui, oublié, oubliait une verte moule",
"qui, oublié, oubliait un vert mouton",
"qui, oublié, oubliait un mouton vert",
"oublié, il oubliait les moutons verts",
"oublié, il oubliait les verts moutons",
"oublié, il oubliait les vertes moules",
"oublié, il oubliait les moules vertes",
"oublié, il oubliait une moule verte",
"oublié, il oubliait une verte moule",
"oublié, il oubliait un vert mouton",
"oublié, il oubliait un mouton vert"
],
5 : [
"qui, oubliés, oubliaient les moutons verts",
"qui, oubliés, oubliaient les verts moutons",
"qui, oubliés, oubliaient les vertes moules",
"qui, oubliés, oubliaient les moules vertes",
"qui, oubliés, oubliaient une moule verte",
"qui, oubliés, oubliaient une verte moule",
"qui, oubliés, oubliaient un vert mouton",
"qui, oubliés, oubliaient un mouton vert",
"oubliés, ils oubliaient les moutons verts",
"oubliés, ils oubliaient les verts moutons",
"oubliés, ils oubliaient les vertes moules",
"oubliés, ils oubliaient les moules vertes",
"oubliés, ils oubliaient une moule verte",
"oubliés, ils oubliaient une verte moule",
"oubliés, ils oubliaient un vert mouton",
"oubliés, ils oubliaient un mouton vert"
],
6 : [
"un mouton vert oubliait un mouton",
"un mouton oubliait un mouton vert",
"une moule verte oubliait un mouton",
"un mouton vert oubliait un mouton"
],
7 : [
"un mouton vert oubliait des moutons",
"des moutons verts oubliaient des moutons",
"une moule verte oubliait des moutons",
"un mouton oubliait des moutons verts"
],
25 : [
"une moule verte oubliait une moule",
"un mouton vert oubliait une moule",
"un mouton oubliait une moule verte",
"une moule oubliait une verte moule"
],
8 : [
"un mouton vert oubliait son mouton",
"un mouton oubliait son mouton vert",
"une moule verte oubliait son mouton",
"une moule verte oubliait sa moule",
"une moule verte oubliait ses moutons",
"une moule verte oubliait ses moutons",
"un mouton vert oubliait ses moutons",
"un mouton oubliait ses moutons verts",
"une moule oubliait ses moutons verts",
"une moule oubliait ses moules vertes",
"une moule verte oubliait sa moule",
"un mouton vert oubliait son mouton"
],
9 : [
"pourquoi oubliez - vous, moutons verts",
"pourquoi oubliez - vous, ô moutons verts"
],
10 : [
"qui, oubliés, oubliez les moutons verts",
"qui, oubliés, oubliez les verts moutons",
"qui, oubliés, oubliez les vertes moules",
"qui, oubliés, oubliez les moules vertes",
"qui, oubliés, oubliez une moule verte",
"qui, oubliés, oubliez une verte moule",
"qui, oubliés, oubliez un vert mouton",
"qui, oubliés, oubliez un mouton vert"
],
26 : [
"pourquoi oubliez - vous, moules vertes",
"pourquoi oubliez - vous, vertes moules",
"pourquoi oubliez - vous, ô moules vertes"
],
27 : [
"qui, oubliées, oubliez les moutons verts",
"qui, oubliées, oubliez les verts moutons",
"qui, oubliées, oubliez les vertes moules",
"qui, oubliées, oubliez les moules vertes",
"qui, oubliées, oubliez une moule verte",
"qui, oubliées, oubliez une verte moule",
"qui, oubliées, oubliez un vert mouton",
"qui, oubliées, oubliez un mouton vert"
],
11 : [
"pourquoi refuses - tu, mouton vert",
"pourquoi refuses - tu, moule verte",
"pourquoi refuses - tu, ô mouton vert",
"pourquoi refuses - tu, ô moule verte"
],
12 : [
"qui, oubliant, refuses les moutons verts",
"qui, oubliant, refuses les verts moutons",
"qui, oubliant, refuses les vertes moules",
"qui, oubliant, refuses les moules vertes",
"qui, oubliant, refuses une moule verte",
"qui, oubliant, refuses une verte moule",
"qui, oubliant, refuses un vert mouton",
"qui, oubliant, refuses un mouton vert"
],
13 : [
"oubliez, moutons verts, vos moutons verts",
"moutons verts, oubliez vos vers moutons",
"oubliez, moules vertes, vos vertes moules",
"toi, mouton vert, refuse ton mouton vert",
"toi, verte moule, refuse ton mouton vert"
],
14 : [
"dans le mouton vert, de verts moutons",
"dans les moutons verts, des moutons verts",
"dans le vert mouton, de verts moutons",
"dans les verts moutons, de verts moutons",
"dans les moutons verts, de vertes moules",
"dans les verts moutons, de vertes moules",
"dans la moule verte, de vertes moules",
"dans la verte moule, de vertes moules",
"tels de verts moutons, de verts moutons",
"tels de verts moutons, de verts moutons",
"dans la moule verte, de vertes moules",
"telles des moules, de vertes moules",
"oubliant les moutons, de vertes moules",
"telles des moules, de vertes moules",
"comme une moule verte, de vertes moules",
"oubliant, oubliant, de vertes moules",
"oubliant, oubliant, de verts moutons"
],
15 : [
"oubliaient les moutons des moutons verts",
"oubliaient les moules des moutons verts",
"oubliaient les moules vertes des moutons"
],
20 : [
"oubliaient les moules des vertes moules",
"oubliant, oubliaient les vertes moules",
"oubliaient les moutons des vertes moules"
],
21 : [
"oubliaient les moules de la verte moule",
"oubliaient les moules vertes de la moule",
"oubliaient les moules de la moule verte"
],
16 : [
"oubliaient les moutons du mouton vert",
"oubliaient les moutons du vert mouton"
],
17 : [
"oubliait les moutons de la moule verte",
"oubliait les moutons de la verte moule"
],
# "oubliait les moules de la verte moule",
# "oubliait les moules vertes de la moule",
# "oubliait les moules de la moule verte"
# ],
18 : [
"qui, oubliée, oubliait les moutons verts",
"qui, oubliée, oubliait les verts moutons",
"qui, oubliée, oubliait les vertes moules",
"qui, oubliée, oubliait les moules vertes",
"qui, oubliée, oubliait une moule verte",
"qui, oubliée, oubliait une verte moule",
"qui, oubliée, oubliait un vert mouton",
"qui, oubliée, oubliait un mouton vert",
"oubliée, elle oubliait les moutons verts",
"oubliée, elle oubliait les verts moutons",
"oubliée, elle oubliait les vertes moules",
"oubliée, elle oubliait les moules vertes",
"oubliée, elle oubliait une moule verte",
"oubliée, elle oubliait une verte moule",
"oubliée, elle oubliait un vert mouton",
"oubliée, elle oubliait un mouton vert"
]
}

