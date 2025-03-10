class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = 'aeiou'
        vowel_dict = {vowel: 0 for vowel in vowels}
        vowel_cnt = [vowel_dict.copy()]
        cur_cons_cnt = 0
        cons_cnt = []
        for c in word:
            if c in vowel_dict:
                vowel_dict[c] += 1
            else:
                cur_cons_cnt += 1
            vowel_cnt.append(vowel_dict.copy())
            cons_cnt.append(cur_cons_cnt)
        
        position_cons = [0]
        cur_cons_cnt = 0
        for i, cnt in enumerate(cons_cnt):
            if cnt > cur_cons_cnt:
                cur_cons_cnt += 1
                position_cons.append(i)
        #print(cons_cnt)
        #print(position_cons)
        ans = 0

        def check_vowels_present(i, j):
            vowel_i = vowel_cnt[i]
            vowel_j = vowel_cnt[j+1]
            for vowel in vowels:
                if vowel_j[vowel] - vowel_i[vowel] == 0:
                    return False
            return True
        if cur_cons_cnt == 0 and k>0:
            return 0
        if cur_cons_cnt == 0:
            for i in range(n-4):
                left_start = i
                right_start = n - 1
                left = left_start
                right = right_start
                if not check_vowels_present(i, right_start):
                    continue
                while left < right:
                    mid = (left + right) // 2
                    #print(left, mid, right, check_vowels_present(i, mid))
                    if check_vowels_present(i, mid):
                        right = mid
                    else:
                        left = mid + 1
                #print('ans=', ans, right, right_start)
                ans += (right_start - right + 1)                
            return ans

        for i in range(n):
            cur_cons_cnt = cons_cnt[i]
            if word[i] not in vowels:
                cur_cons_cnt -= 1
            needed_cons_cnt = cur_cons_cnt + k
            if needed_cons_cnt >= len(position_cons):
                break
            left_start = position_cons[needed_cons_cnt]
            if needed_cons_cnt + 1 >= len(position_cons):
                right_start = n - 1
            else:
                right_start = position_cons[needed_cons_cnt + 1] - 1
            #print(i, word[i], cur_cons_cnt, needed_cons_cnt,  left_start, right_start)
            if not check_vowels_present(i, right_start):
                continue
            left = left_start
            right = right_start
            while left < right:
                mid = (left + right) // 2
                #print(left, mid, right, check_vowels_present(i, mid))
                if check_vowels_present(i, mid):
                    right = mid
                else:
                    left = mid + 1
            #print('ans=', ans, right, right_start)
            ans += (right_start - right + 1)
        return ans



        