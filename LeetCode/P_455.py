# coding:utf-8



def findContentChildren(g, s):
    g.sort()
    s.sort()
    count = 0
    for i in range(len(g)):
        j = 0
        if g[i] > s[len(s) - 1]:
            return count
        for j in range(len(s)):
            if s[j] >= g[i]:
                count += 1
                # 这个孩子已经饱了
                g[i] = -1
                s[j] = -1
                break
            j += 1
        i += 1
    return count


if __name__ ==  "__main__":
    g = [10, 9, 8, 7]
    s = [5, 6, 7, 8]
    print(findContentChildren(g, s))

