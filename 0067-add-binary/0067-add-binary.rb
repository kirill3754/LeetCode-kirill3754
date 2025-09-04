# @param {String} a
# @param {String} b
# @return {String}
def add_binary(a, b)
    max_l = [a.length, b.length].max
    a = a.rjust(max_l, "0")
    b = b.rjust(max_l, "0")
    ans = ""
    r = "0"
    (max_l - 1).downto(0) do |i|
        if a[i] == "0" && b[i] == "0"
            ans << (r == "0" ? "0" : "1")
            r = "0"
        elsif a[i] == "1" && b[i] == "1"
            ans << (r == "0" ? "0" : "1")
            r = "1"
        else
            ans << (r == "0" ? "1" : "0")
        end
    end
    ans << (r == "1" ? "1" : "")
    ans.reverse
end