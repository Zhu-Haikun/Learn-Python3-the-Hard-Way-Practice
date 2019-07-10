class Song(object):
    # 通过__init__函数生成实例变量lyrics
    def __init__(self, lyrics):
        self.lyrics = lyrics
    # 遍历实例变量lyrics，并打印
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()