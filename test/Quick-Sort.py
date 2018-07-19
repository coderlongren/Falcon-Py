class Solution:
    def quick_sort(self, seq, left, right):
        if left < right:
            i, j = left, right
            head = seq[i]
            while i < j and seq[j] > head:
                j -= 1
            if i < j:
                seq[i] = seq[j]
                i += 1
            while i < j and seq[i] < head:
                i += 1
            if i < j:
                seq[j] = seq[i]
                j -= 1
            seq[i] = head

            self.quick_sort(seq, left, i - 1)
            self.quick_sort(seq, i + 1, right)

main = Solution()
seq = [2,1]
main.quick_sort(seq, 0, len(seq) - 1)
print(seq)