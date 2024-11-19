# Huffman Encoding Compression and Decompression

## 1. Programming Language and IDE
- **Programming Language**: Python 3.10+
- **IDE**: 
  - VS Code
  - PyCharm
  - 或其他支援 Python 的編輯器

---

## 2. Significant Libraries and Functions
### Libraries
- **`os`**:
  - 用於檢查文件大小並計算壓縮比。
- **`collections.Counter`**:
  - 用於統計字符頻率。
- **`heapq`**:
  - 用於實現最小堆，構建 Huffman 樹。

### Key Functions
1. **`build_huffman_tree(text)`**:
   - 功能：根據字符頻率構建 Huffman 樹。
   - 過程：
     - 使用 `Counter` 計算頻率。
     - 使用 `heapq` 建立最小堆，進行節點合併。
2. **`create_codes(node, current_code, codes)`**:
   - 功能：生成字符的 Huffman 二進制編碼表。
   - 遞歸遍歷樹結構，為每個字符生成唯一的二進制編碼。
3. **`coding_file(input_file, output_file)`**:
   - 功能：將原始文本壓縮為 `.huff` 格式。
   - 步驟：
     - 建立 Huffman 樹和編碼表。
     - 將文本轉換為二進制字符串，填充位元對齊到位元組。
     - 寫入編碼表和壓縮數據。
4. **`decoding_file(input_file, output_file)`**:
   - 功能：將 `.huff` 文件解壓為原始文本。
   - 步驟：
     - 讀取編碼表和壓縮的二進制數據。
     - 使用編碼表逐位解碼還原文本。

---

## 3. Compression Ratios of the Four Test Files
| **Test File**             | **Original Size (bytes)** | **Compressed Size (bytes)** | **Compression Ratio (%)** |
|---------------------------|---------------------------|-----------------------------|---------------------------|
| Lyrics_GangNamStyle.txt   | TBD                       | TBD                         | TBD                       |
| PeterPan.txt              | TBD                       | TBD                         | TBD                       |
| 歌詞_黃金甲.txt             | TBD                       | TBD                         | TBD                       |
| 西遊記.txt                 | TBD                       | TBD                         | TBD                       |

### Compression Ratio Formula:
\[
\text{Compression Ratio (\%)} = \left( 1 - \frac{\text{Compressed Size}}{\text{Original Size}} \right) \times 100
\]

---

## 4. How to Run
### Setup
1. 確保安裝 Python 3.10 或以上版本。
2. 將測試文件放置在對應資料夾中，如：
   - `Lyrics_GangNamStyle/Lyrics_GangNamStyle.txt`
   - `PeterPan/PeterPan.txt`
   - `歌詞_黃金甲/歌詞_黃金甲.txt`
   - `西遊記/西遊記.txt`
3. 確保目錄結構如下：
