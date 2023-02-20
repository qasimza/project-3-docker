import os
import socket

with open('/home/output/result.txt', 'w+', newline='\n') as results:  

    results.write('-----------------------------------------------RESULTS-----------------------------------------------\n')

    # a) Listing names of all the text files
    results.write('\nFilenames:\n')
    path = '/home/data'
    files = list()
    for file in os.listdir(path):
        if file.endswith('.txt'):
            results.write(f'{file}\n')
            files.append(f'/home/data/{file}')

    # b, c) Total words in each, grand total
    
    total_words = 0

    results.write('\nWord Count:\n')
    for file_name in files:
        with open(file_name, 'r') as file:
            num_words = len(file.read().split())
            results.write(f'Number of words in {file_name}: {num_words}\n')
            total_words+=num_words
    
    results.write(f'\nTotal words: {total_words}\n')

    # d) Top 3 words with maximum number of counts in IF.txt
    results.write('\nTop 3 words in IF.txt and their word counts:\n')
    with open('/home/data/IF.txt', 'r') as if_txt:
        freq_dict = dict()
        for word in if_txt.read().lower().split():
            if word in freq_dict.keys():
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
        for k,v, in sorted(freq_dict.items(), key=lambda words: words[1], reverse = True)[:3]:
            results.write(f'Word:{k}; Count{v}\n')
            
    # e) Find IP address of the machine
    results.write(f'\nIP address: {socket.gethostbyname(socket.gethostname())}\n')    






