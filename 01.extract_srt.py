import sys, os

try:

    input_file = sys.argv[1]
    output_file = '.'.join(input_file.split('.')[:-1])

    os.system(f'call ffmpeg -i "{input_file}" -map 0:s:0 "{output_file}.srt" -y')
    
    print('\n\nSuccess!\n\n')
    
except:
    
    print('\n\nSomething went wrong.\n\n')