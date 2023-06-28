import os


def conclusion_file(file):
    """ Выводит значение прочитанных файлов """
    file_path = os.path.join(os.getcwd(), file)
    with open(file_path, 'r', encoding='utf-8') as file_read:                                         
        line_1 = file_read.readline().strip('\n ')
        line_2 = file_read.readline().strip('\n')      
        count = len(file_read.readlines())
        if count > 1:                                                              
            print(f'{"".join(line_1)} файл: {file}')
            print(f'{"".join(line_2)} файл: {file}')        
        else:
            print(f'{"".join(line_1)} файл: {file}')
        print()
                       
    return

def comparison_file(file):
    """ Записывает и выводит отсортированые файлы """
    list_1  = []
    for line in file:
        with open(line, 'r', encoding='utf-8') as file_read: 
            lines = file_read.read().splitlines()
            list_1.append([line, len(lines)])
            list_1[len(list_1)-1] += lines
    list_1.sort(key=len)
    for result in list_1:
        if result[1] > 1:
            print(f'{result[0]}\n2\n{result[2]} {result[0]}\n{result[3]} {result[0]}\n')
        else:
            print(f'{result[0]}\n1\n{result[2]} {result[0]}\n')           
    with open('4.txt', 'w', encoding='utf-8') as file_write:    
        for result in list_1:
            for elem in result:
                file_write.write(f'{elem}\n')
        file_path = os.path.join(os.getcwd(), '4.txt')
        return file_path    
                    
      
if __name__ == '__main__':
       
    conclusion_file('1.txt')
    conclusion_file('2.txt')
    conclusion_file('3.txt') 
    comparison_file(['1.txt', '2.txt', '3.txt'])   