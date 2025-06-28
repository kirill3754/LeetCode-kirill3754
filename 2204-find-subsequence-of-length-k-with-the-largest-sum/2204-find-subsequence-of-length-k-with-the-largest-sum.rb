# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_subsequence(nums, k)
    arr = []
    nums.each_with_index do |x, i|
        arr << [x, i]
    end
    arr.sort_by! {|x| -x[0]}
    arr = arr.first(k)
    arr.sort_by! {|x| x[1]}
    ans = arr.map {|x| x[0]}
    return ans
end