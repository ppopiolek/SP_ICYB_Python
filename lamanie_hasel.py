import requests
import re
from bs4 import BeautifulSoup
import click
import json
import os
import random
from itertools import combinations

def get_html_of(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f'HTTP status code of {resp.status_code} returned.')
        exit(1)
    return resp.content.decode()

def count_occurrences_in(word_list):
    word_count = {}
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

def get_all_words_from(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    return re.findall(r'\w+', raw_text)

def generate_password_mutations(word):
    mutations = [word, word.capitalize(), word.upper()]
    substitutions = word.replace('a', '@').replace('s', '$').replace('o', '0').replace('e', '3')
    mutations.append(substitutions)

    years = ['2022', '2023']
    appendices = ['!', '1!', '2!', '3!', '01', '123', '!', '!!!', '_', '99', '999']
    for year in years:
        mutations.append(word + year)
    for appendix in appendices:
        mutations.append(word + appendix)
    
    mutations.append(word * 2)
    mutations.append(word.capitalize() + word.upper())
    mutations.append(''.join(random.choice((str.upper, str.lower))(c) for c in word))
    
    symbols = ['*', '#', '@', '$']
    for symbol in symbols:
        mutations.append(word + symbol)
        mutations.append(word + symbol * 2)
    
    double_substitutions = substitutions.replace('i', '1').replace('l', '1').replace('t', '7')
    mutations.append(double_substitutions)

    return mutations

def get_top_words_from(url, length=None, combo_length=1):
    all_words = get_all_words_from(url)
    occurrences = count_occurrences_in(all_words)
    sorted_words = sorted(occurrences.items(), key=lambda item: item[1], reverse=True)
    
    filtered_words = [word for word, freq in sorted_words if length is None or len(word) >= length]
    
    combined_words = []
    for combo in combinations(filtered_words[:10], combo_length):
        combined_words.append(''.join(combo))
    
    top_words_with_mutations = []
    for word in combined_words:
        top_words_with_mutations.extend(generate_password_mutations(word))

    return top_words_with_mutations

def save_to_file(word_list, filename):
    with open(filename, 'w') as file:
        for word in word_list:
            file.write(word + '\n')
    print(f"Results saved to {filename}")

@click.command()
@click.option('--length', default=None, type=int, help='Minimum length of words to consider')
@click.option('--combo-length', default=1, type=int, help='Number of words to combine for generating passwords')
def main(length, combo_length):
    with open('wiki.json', 'r') as file:
        data = json.load(file)
    
    if not os.path.exists("password_lists"):
        os.makedirs("password_lists")

    for login, url in data.items():
        print(f"Generating password list for {login} from {url}")
        top_words_with_mutations = get_top_words_from(url, length, combo_length)
        save_to_file(top_words_with_mutations, f'password_lists/{login}_passwords.txt')

if __name__ == '__main__':
    main()
