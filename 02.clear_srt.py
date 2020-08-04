"""
Creates readable text file from SRT file.
"""
import re, sys

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def is_time_stamp(l):
  if l[:2].isnumeric() and l[2] == ':':
    return True
  return False

def has_letters(line):
  if re.search('[a-zA-Z]', line):
    return True
  return False

def has_no_text(line):
  l = line.strip()
  if not len(l):
    return True
  if l.isnumeric():
    return True
  if is_time_stamp(l):
    return True
  if l[0] == '(' and l[-1] == ')':
    return True
  if not has_letters(line):
    return True
  return False

def is_lowercase_letter_or_comma(letter):
  if letter.isalpha() and letter.lower() == letter:
    return True
  if letter == ',':
    return True
  return False

def clean_up(lines):
  """
  Get rid of all non-text lines and
  try to combine text broken into multiple lines
  """
  new_lines = []
  for line in lines[1:]:
    if has_no_text(line):
      continue
    elif len(new_lines) and is_lowercase_letter_or_comma(line[0]):
      #combine with previous line
      new_lines[-1] = new_lines[-1].strip() + ' ' + line
    else:
      #append line
      new_lines.append(line)
  return new_lines

def main(args):
  """
    args[1]: file name
    args[2]: encoding. Default: utf-8.
      - If you get a lot of [?]s replacing characters,
      - you probably need to change file_encoding to 'cp1252'
  """
  file_name = args[1]
  file_encoding = 'utf-8' if len(args) < 3 else args[2]
  with open(file_name, encoding=file_encoding, errors='replace') as f:
    lines = f.read().splitlines()
    new_lines = clean_up(lines)
  new_file_name = file_name[:-4] + '.txt'
  with open(new_file_name, 'w') as f:
    f.write(cleanhtml('\n'.join(new_lines)))

if __name__ == '__main__':
  try:
    main(sys.argv)
    print('Success!')
  except:
    print('Something went wrong...')

"""
NOTES
 * Run from command line as
 ** python srt_to_txt.py file_name.srt cp1252
 * Creates file_name.txt with extracted text from file_name.srt 

 * Script assumes that lines beginning with lowercase letters or commas 
 * are part of the previous line and lines beginning with any other character
 * are new lines. This won't always be correct. 
"""