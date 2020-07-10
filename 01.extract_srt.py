import sys, os

try:

    input_file = sys.argv[1]
    output_file = '.'.join(input_file.split('.')[:-1])

    os.system(f'ffmpeg -i "{input_file}" -map 0:s:0 "{output_file}.srt" -y')
    
    input('\n\nSuccess!\n\n')
    
except:
    
    input('\n\nSomething is wrong.\n\n')