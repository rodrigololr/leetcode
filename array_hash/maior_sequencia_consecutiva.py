Solution(object):
    class def longestConsecutive(self, nums):
        num_set = set(nums)
        max_length = 0

        for num in num_set:
        # só começa sequência se for o início (não tem anterior)
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

            # conta quantos consecutivos tem
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length
        