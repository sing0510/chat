import os #operating system

def read_file(filename):
	lines = []
	with open(filename, 'r')as f:
		for line in f:
			lines .append(line.strip())
	return lines

def convert(lines):
    new = []
    person = None
    Sing_word_count = 0
    Sing_sticker_count =0
    Tom_word_count = 0
    Tom_sticker_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Sing':
            if s[2] == '貼圖':
                Sing_sticker_count += 1
            else:
                for m in s[2:]:
                    Sing_word_count += len(m)


        elif name == 'Tom':
            if s[2] == '貼圖':
                Tom_sticker_count += 1
            else:
                for m in s[2:]:
                    Tom_word_count += len(m)

    print('Sing說了', Sing_word_count ,'傳了', Sing_sticker_count, '貼圖')
    print('Tom說了', Tom_word_count,'傳了', Tom_sticker_count, '貼圖')


def write_file(filename, lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')

		

def main():
    lines = read_file('output.txt')
    lines = convert(lines)
    # write_file('output.txt', lines)

main()