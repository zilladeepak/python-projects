def open_file(path:str) -> str :
    with open(path,'rt') as file:
        text :str = file.read()
    return text

def analyser(text:str) ->dict[str,int]:
    print(f'"{text}"')
    print('-------')
    result :dict[str,int] = {
        'total_chrs_inclu_spaces':len(text),
        'total_chrs_excle_spaces':len(text.replace(' ','')),
        'total_spaces':text.count(' '),
        'total_words':len(text.split())
        }
    return result


def main() -> None:
    text :str = open_file('demo_file.txt')
    text_analysis :dict[str,int] = analyser(text)
    for key,value in text_analysis.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    main()
