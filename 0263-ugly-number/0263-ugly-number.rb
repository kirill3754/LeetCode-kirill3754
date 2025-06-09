# @param {Integer} n
# @return {Boolean}
def is_ugly(n)
    return false if n<1
    while true
        if n % 2 == 0
            n = n / 2
        elsif n % 3 == 0
            n = n / 3
        elsif n % 5 == 0
            n = n / 5
        elsif n > 1
            return false
        else
            return true
        end
    end
end