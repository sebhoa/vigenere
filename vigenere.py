from string import ascii_letters

class Code:

    def __init__(self, cle):
        self.alpha = ascii_letters
        self.size = len(self.alpha)
        self.cle = cle
        self.pass_phrase = ''

    def set_pass_phrase(self, msg):
        i = 0
        for c in msg.lower():
            if c in self.alpha:
                self.pass_phrase += self.cle[i]
                i = (i + 1) % len(self.cle)
            else:
                self.pass_phrase += ' '


    def encode(self, msg):
        self.set_pass_phrase(msg)
        coded = ''
        for idc, c in enumerate(msg):
            if c in self.alpha:
                i = self.alpha.index(c)
                coded +=  self.alpha[(i + self.alpha.index(self.pass_phrase[idc])) % self.size]
            else:
                coded += c
        return coded

    def decode(self, coded):
        decoded = ''
        for idc, c in enumerate(coded):
            if c in self.alpha:
                i = self.alpha.index(c)
                decoded +=  self.alpha[(i - self.alpha.index(self.pass_phrase[idc])) % self.size]
            else:
                decoded += c
        return decoded


cle = 'musique'
msg = "J'adore ecouter FUN-RADIO toute la journee"
codec = Code(cle)
coded = codec.encode(msg)
print('Message codé :')
print(coded)
print('Message original :')
print(codec.decode(coded))







