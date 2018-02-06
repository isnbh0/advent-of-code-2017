
class TM():
    def __init__(self, blueprint):
        self.tape = {0 : 0}
        self.cursor = 0
        self.state = blueprint[0]
        self.blueprint = blueprint

    def step(self, n=1):
        for i in range(n):
            try:
                val = self.tape[self.cursor]
            except:
                self.tape[self.cursor] = 0
                val = self.tape[self.cursor]
                
            self.tape[self.cursor] = self.blueprint[self.state][val][0]
            self.cursor += self.blueprint[self.state][val][1]
            self.state = self.blueprint[self.state][val][2]
        return
    
    def checksum(self):
        return sum(self.tape.values())

