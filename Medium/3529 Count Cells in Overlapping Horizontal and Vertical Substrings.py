# https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/description/

class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        
        m = len(grid)
        n = len(grid[0]) if m else 0
        total = m * n
        L = len(pattern)
        if L == 0 or L > total:
            return 0
        
        # Generate horizontal string H
        h_str = []
        for row in grid:
            h_str.extend(row)
        h_str = ''.join(h_str)
        
        # Generate vertical string V
        v_str = []
        for j in range(n):
            for i in range(m):
                v_str.append(grid[i][j])
        v_str = ''.join(v_str)
        
        # Find all occurrences in H and V using KMP
        h_occurrences = self.kmp_search(h_str, pattern)
        v_occurrences = self.kmp_search(v_str, pattern)
        
        # Mark covered positions in H using prefix sum
        len_h = len(h_str)
        covered_h = [0] * (len_h + 1)
        for s in h_occurrences:
            covered_h[s] += 1
            end = s + L
            if end <= len_h:
                covered_h[end] -= 1
        current = 0
        for i in range(len_h):
            current += covered_h[i]
            covered_h[i] = current > 0
        
        # Mark covered positions in V using prefix sum
        len_v = len(v_str)
        covered_v = [0] * (len_v + 1)
        for s in v_occurrences:
            covered_v[s] += 1
            end = s + L
            if end <= len_v:
                covered_v[end] -= 1
        current = 0
        for i in range(len_v):
            current += covered_v[i]
            covered_v[i] = current > 0
        
        # Count cells covered by both horizontal and vertical substrings
        count = 0
        for i in range(m):
            for j in range(n):
                pos_h = i * n + j
                pos_v = j * m + i
                if pos_h < len_h and pos_v < len_v and covered_h[pos_h] and covered_v[pos_v]:
                    count += 1
        return count
    
    def kmp_search(self, text: str, pattern: str) -> List[int]:
        lps = self.compute_lps(pattern)
        i = j = 0
        occurrences = []
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == len(pattern):
                    occurrences.append(i - j)
                    j = lps[j - 1]
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return occurrences
    
    def compute_lps(self, pattern: str) -> List[int]:
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
