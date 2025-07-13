# @param {String} s
# @param {String} t
# @return {Boolean}
def is_subsequence(s, t)
    i = 0
    t.each_char do |t|
        i += 1 if t == s[i]
        return true if s.length == i
    end
    s.length == i
end