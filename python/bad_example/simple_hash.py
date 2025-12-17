import struct

# Rotate left for 64-bit words
def rol(x, r):
    return ((x << r) & ((1<<64)-1)) | (x >> (64-r))

# ChaCha-style quarter round on four 64-bit words
def quarter_round(a, b, c, d):
    a = (a + b) & ((1<<64)-1)
    d ^= a; d = rol(d, 32)
    c = (c + d) & ((1<<64)-1)
    b ^= c; b = rol(b, 24)
    a = (a + b) & ((1<<64)-1)
    d ^= a; d = rol(d, 16)
    c = (c + d) & ((1<<64)-1)
    b ^= c; b = rol(b, 63)
    return a, b, c, d

# Single-round permutation using two quarter rounds
def permute(state):
    s0, s1, s2, s3 = state
    s0, s1, s2, s3 = quarter_round(s0, s1, s2, s3)
    s0, s1, s2, s3 = quarter_round(s0, s2, s1, s3)
    return [s0, s1, s2, s3]

# Improved toy hash function with block processing and ARX mixing
def improved_hash(text: bytes) -> str:
    # Initialize 256-bit state (four 64-bit words)
    state = [
        0xA5A5A5A5A5A5A5A5,
        0x0123456789ABCDEF,
        0x0F1E2D3C4B5A6978,
        0xFFFFFFFF00000000
    ]

    # Absorb message in 8-byte blocks with 0x80 padding
    for i in range(0, len(text), 8):
        block = text[i:i+8].ljust(8, b'\x80')  # pad with 0x80 then zeros
        m0, = struct.unpack(">Q", block)
        state[0] ^= m0

        # Mix with 4 rounds of ARX permutation per block
        for _ in range(4):
            state = permute(state)

    # Finalization: incorporate bit length and run 12 more rounds
    bits = len(text) * 8
    state[1] ^= bits
    for _ in range(12):
        state = permute(state)

    # Produce 256-bit (32-byte) hex output
    return "".join(f"{x:016x}" for x in state)

# Example usage
print(improved_hash(b"password1234"))
