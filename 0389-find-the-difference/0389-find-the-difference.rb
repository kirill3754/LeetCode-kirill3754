# @param {String} s
# @param {String} t
# @return {Character}
def find_the_difference(s, t)
    (t.each_char.tally.to_a - s.each_char.tally.to_a)[0][0]
end