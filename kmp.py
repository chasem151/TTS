class KMP:
    def __init__(self, txt, pat):
        self.__txt = txt
        self.__pat = pat
        self.__next = [0] * len(self.__pat)

    def __getNext(self) -> None:
        self.__next[0] = -1
        k = -1
        j = 0
        while j < len(self.__pat) - 1:
            if k == -1 or self.__pat[j] == self.__pat[k]:
                j += 1
                k += 1
                self.__next[j] = k
            else:
                k = self.__next[k]

    def search(self) -> []:
        if not self.__pat or not self.__txt:
            return []

        self.__getNext()
        res = []
        i, j = 0, 0
        while i < len(self.__txt):
            while j < len(self.__pat):
                if i >= len(self.__txt):
                    break
                if j == -1 or self.__txt[i] == self.__pat[j]:
                    i += 1
                    j += 1
                else:
                    j = self.__next[j]
            if j == len(self.__pat):
                res.append(i - j)
                j = 0
        return res


if __name__ == '__main__':
    txt = ""
    pat = "ab"
    kmp = KMP(txt, pat)
    print("all found pos:", kmp.search())
