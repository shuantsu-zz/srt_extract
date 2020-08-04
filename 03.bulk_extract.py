try:
    import sys, os

    print(sys.argv[1:])

    preserve = input('Preserve srt? (Y/N)').lower().strip() == 'y'

    for file in sys.argv[1:]:
        print(file)
        os.system(f'python 01.extract_srt.py "{file}"')
        srt = '.'.join(file.split('.')[:-1]) + '.srt'
        os.system(f'python 02.clear_srt.py "{srt}"')
        if not preserve:
            try:
                os.remove(srt)
            except:
                print('nothing to delete')
            
except Exception as e:
    print('error', e)
    
input()