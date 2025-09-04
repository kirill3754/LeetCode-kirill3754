# @param {String} s
# @return {Integer}
def length_of_last_word(s)
    l = s.split(" ")
    l[-1].length()
end