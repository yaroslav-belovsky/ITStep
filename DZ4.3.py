castle = [1, ["c"], 543, "P", ["n", ["r"]], "i", [[["s"]]]]
word = "" + castle[3] + castle[4][1][0] + castle[5] + castle[4][0] + castle[1][0] + chr(castle[2] - 442) + castle[6][0][0][0] + castle[6][0][0][0]
print(word)