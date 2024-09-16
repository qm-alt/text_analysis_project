 import os
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import string

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def clean_text(text):
    # Hapus tanda baca dan ubah ke huruf kecil
    translator = str.maketrans('', '', string.punctuation)
    return text.lower().translate(translator)

def word_frequency(text):
    words = text.split()
    return Counter(words)

def generate_wordcloud(word_freq, output_path):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(output_path)
    plt.show()

def plot_word_frequency(word_freq, output_path, top_n=10):
    most_common_words = word_freq.most_common(top_n)
    words = [word for word, freq in most_common_words]
    frequencies = [freq for word, freq in most_common_words]
    
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} Most Common Words')
    plt.savefig(output_path)
    plt.show()

def main():
    input_file = 'text_files/sample.txt'
    wordcloud_output = 'output/wordcloud.png'
    barchart_output = 'output/word_frequency.png'
    
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # 1. Baca file teks
    text = read_text_file(input_file)
    
    # 2. Bersihkan teks
    cleaned_text = clean_text(text)
    
    # 3. Hitung frekuensi kata
    word_freq = word_frequency(cleaned_text)
    
    # 4. Hasilkan Word Cloud
    generate_wordcloud(word_freq, wordcloud_output)
    
    # 5. Buat Bar Chart frekuensi kata
    plot_word_frequency(word_freq, barchart_output)

if __name__ == '__main__':
    main()
