import random
import os

PERMURATION_SIZE = 256


class Enigma:
    def __init__(self, key: int):
        random.seed(key)
        self.plugboard = Plugboard()
        self.rotors = []
        self.n_rotors = random.randint(20, 50)
        for _ in range(self.n_rotors):
            self.rotors.append(Rotor())
        self.reflector = Reflector()

    def encipher(self, val: int) -> int:
        cipher = self.plugboard.encipher_forwards(val)
        for idx, rotor in enumerate(self.rotors):
            if idx == 0:
                rotor.rotate()
            elif self.rotors[idx - 1].rotate_next():
                rotor.rotate()
            cipher = rotor.encipher_forwards(cipher)

        cipher = self.reflector.encipher(cipher)
        for rotor in self.rotors[::-1]:
            cipher = rotor.encipher_backwards(cipher)

        cipher = self.plugboard.encipher_backwards(cipher)
        return cipher


class Plugboard:
    def __init__(self):
        self.wires = [i for i in range(PERMURATION_SIZE)]
        swapped = []

        for idx, val in enumerate(self.wires):
            if idx not in swapped and random.randint(0, 9) < 6:
                loc = random.randint(0, len(self.wires) - 1)
                if loc not in swapped:
                    tmp = self.wires[loc]
                    self.wires[loc] = val
                    self.wires[idx] = tmp
                    swapped.insert(0, idx)
                    swapped.insert(0, loc)

    def encipher_forwards(self, byte: int) -> int:
        return self.wires[byte]

    def encipher_backwards(self, byte: int) -> int:
        return self.wires.index(byte)


class Rotor:
    def __init__(self):
        self.permutations = [i for i in range(PERMURATION_SIZE)]
        self.rotor_pos = 0
        self.rotate_next_pos = 0

        random.shuffle(self.permutations)

        self.set_position(random.randint(0, PERMURATION_SIZE))

        self.rotate_next_pos = random.randint(0, PERMURATION_SIZE)

    def set_position(self, position: int) -> int:
        change = self.permutations.index(position) - self.rotor_pos
        self.rotor_pos = position
        self.permutations = self.permutations[change:] + self.permutations[:change]

    def rotate(self) -> None:
        self.permutations = self.permutations[1:] + self.permutations[:1]
        self.rotor_pos = (self.rotor_pos + 1) % PERMURATION_SIZE
        # if self.rotor_pos == PERMURATION_SIZE:
        #    self.rotor_pos = 0

    def rotate_next(self) -> bool:
        return self.rotor_pos == self.rotate_next_pos

    def encipher_forwards(self, byte: int) -> int:
        return self.permutations[byte]

    def encipher_backwards(self, byte: int) -> int:
        return self.permutations.index(byte)


class Reflector:
    def __init__(self):
        self.permutations = [i for i in range(0, PERMURATION_SIZE)]
        tmp_val = [i for i in range(0, PERMURATION_SIZE)]

        for idx, val in enumerate(self.permutations):
            if idx == val:
                rnd = idx
                while idx == rnd:
                    rnd = random.choice(tmp_val)
                self.permutations[idx] = rnd
                self.permutations[rnd] = idx
                tmp_val.remove(rnd)
                tmp_val.remove(idx)

    def encipher(self, byte: int) -> int:
        return self.permutations[byte]


def encipher(seed: int, infile_path: str, outfile_path: str):
    e = Enigma(seed)
    read_size = 64
    # Open both files, one for reading, one for writing
    with open(infile_path, "rb") as infd, open(outfile_path, "wb") as outfd:
        #   Create Inifinite loop that we will break out of when we reach the end of the file
        while True:
            #       Read N bytes of data (usually 512, 1024, 2048 bytes)
            buffer = infd.read(read_size)
            #       If we're not at the end of the file
            if buffer:
                #           Create byteArray for the enciphered data
                encoded_buffer = bytearray()
                #           encode each byte
                for b in buffer:
                    encoded_byte = e.encipher(b)
                    encoded_buffer.append(encoded_byte)
                #           write byteArray to output
                outfd.write(encoded_buffer)
            else:
                break


if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    in_path = os.path.join(dir, "random_pic.jpg")
    cipher_path = os.path.join(dir, "cipher.dat")
    decipher_path = os.path.join(dir, "decipher.jpg")
    encipher(4, in_path, cipher_path)
    encipher(4, cipher_path, decipher_path)
    # seed = 3
    # random.seed(seed)
    # val = 10

    # p = Plugboard()
    # c = p.encipher_forwards(val)
    # d = p.encipher_backwards(c)
    # print(f"val = {val}\t c: {c}\t d: {d}")

    # r = Rotor()
    # c = r.encipher_forwards(val)
    # d = r.encipher_backwards(c)
    # print(f"val = {val}\t c: {c}\t d: {d}")

    # r.rotate()
    # c = r.encipher_forwards(val)
    # print(f"val = {val}\t c: {c}\t d: {d}")

    # f = Reflector()
    # c = f.encipher(val)
    # d = f.encipher(c)
    # print(f"val = {val}\t c: {c}\t d: {d}")

    # e = Enigma(seed)
    # c = e.encipher(val)
    # e = Enigma(seed)
    # d = e.encipher(c)
    # print(f"val = {val}\t c: {c}\t d: {d}")

    # cipher = []
    # decipher = []
    # e = Enigma(seed)
    # for val in range(100, 110):
    #     cipher.append(e.encipher(val))
    # e = Enigma(seed)
    # for i, c in enumerate(cipher):
    #     decipher.append(e.encipher(c))
    #     print(f"c: {c},\t d: {decipher[i]}")
