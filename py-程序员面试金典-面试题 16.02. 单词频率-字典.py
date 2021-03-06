class WordsFrequency(object):
    """
设计一个方法，找出任意指定单词在一本书中的出现频率。
你的实现应该支持如下操作：
WordsFrequency(book)构造函数，参数为字符串数组构成的一本书
get(word)查询指定单词在书中出现的频率

示例：
WordsFrequency wordsFrequency = new WordsFrequency({"i", "have", "an", "apple", "he", "have", "a", "pen"});
wordsFrequency.get("you"); //返回0，"you"没有出现过
wordsFrequency.get("have"); //返回2，"have"出现2次
wordsFrequency.get("an"); //返回1
wordsFrequency.get("apple"); //返回1
wordsFrequency.get("pen"); //返回1
提示：
book[i]中只包含小写字母
1 <= book.length <= 100000
1 <= book[i].length <= 10
get函数的调用次数不会超过100000
链接：https://leetcode-cn.com/problems/words-frequency-lcci
    """
    def __init__(self, book):
        """
        :type book: List[str]
        """
        self.rec = {}
        for x in book:
            self.rec[x] = self.rec.get(x, 0) + 1

    def get(self, word):
        """
        :type word: str
        :rtype: int
        """
        return self.rec.get(word, 0)


def main():
    commands = ["WordsFrequency","get","get","get","get","get"], \
               [[["i","have","an","apple","he","have","a","pen"]],["you"],["have"],["an"],["apple"],["pen"]]
    ret = []
    for i, x in enumerate(commands[0]):
        if x == 'WordsFrequency':
            test = WordsFrequency(commands[1][i][0])
            ret.append(None)
        elif x == 'get':
            ret.append(test.get(commands[1][i][0]))

    print(ret)


if __name__ == '__main__':
    main()
