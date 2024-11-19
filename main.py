import os
from collections import Counter
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0]

def create_codes(node, current_code, codes):
    if not node:
        return
    if node.char is not None:
        codes[node.char] = current_code
    create_codes(node.left, current_code + "0", codes)
    create_codes(node.right, current_code + "1", codes)

def coding_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    root = build_huffman_tree(text)
    codes = {}
    create_codes(root, "", codes)

    compressed_text = "".join(codes[char] for char in text)

    with open(output_file, 'wb') as f:
        codebook = str(codes).encode('utf-8')
        f.write(len(codebook).to_bytes(4, 'big'))
        f.write(codebook)

        padded_binary_data = compressed_text + '0' * (8 - len(compressed_text) % 8)
        byte_data = bytearray(int(padded_binary_data[i:i+8], 2) for i in range(0, len(padded_binary_data), 8))
        f.write(byte_data)

        original_size = os.path.getsize(input_file)
        compressed_size = os.path.getsize(output_file)

        compression_ratio = (1 - compressed_size / original_size) * 100

    print(f"原始文件大小: {original_size} byte")
    print(f"壓縮文件大小: {compressed_size} byte")
    print(f"壓縮比: {compression_ratio:.2f}%")

def decoding_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        codebook_length = int.from_bytes(f.read(4), 'big')
        codebook = eval(f.read(codebook_length).decode('utf-8'))

        binary_data = ''.join(format(byte, '08b') for byte in f.read())

    reversed_codebook = {v: k for k, v in codebook.items()}

    current_code = ""
    decoded_text = ""
    for bit in binary_data:
        current_code += bit
        if current_code in reversed_codebook:
            decoded_text += reversed_codebook[current_code]
            current_code = ""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decoded_text)

    print(f"解壓文件大小: {os.path.getsize(output_file)} byte")

if __name__ == "__main__":
    # #----------Lyrics_GangNamStyle----------
    # input_file = "Lyrics_GangNamStyle/Lyrics_GangNamStyle.txt"
    # compressed_file = "Lyrics_GangNamStyle/Lyrics_GangNamStyle.huff"
    # decompressed_file = "Lyrics_GangNamStyle/Lyrics_GangNamStyle_output.txt"

    # #----------PeterPan----------
    # input_file = "PeterPan/PeterPan.txt"
    # compressed_file = "PeterPan/PeterPan.huff"
    # decompressed_file = "PeterPan/PeterPan_output.txt"    
    
    #----------歌詞_黃金甲----------
    # input_file = "歌詞_黃金甲/歌詞_黃金甲.txt"
    # compressed_file = "歌詞_黃金甲/歌詞_黃金甲.huff"
    # decompressed_file = "歌詞_黃金甲/歌詞_黃金甲output.txt"

    #----------西遊記----------
    input_file = "西遊記/西遊記.txt"
    compressed_file = "西遊記/西遊記.huff"
    decompressed_file = "西遊記/西遊記output.txt"

    coding_file(input_file, compressed_file)

    decoding_file(compressed_file, decompressed_file)
