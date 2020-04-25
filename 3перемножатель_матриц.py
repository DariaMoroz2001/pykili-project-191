import random
 
 #перемножение матриц
def matrixmult(matrix1,matrix2):
    s=0     #сумма
    temporary_matrix=[]    #временная матрица
    matrix3=[]   #конечная матрица
    if len(matrix2)!=len(matrix1[0]):
        print("Матрицы не могут быть перемножены")        
    else:
        row1=len(matrix1)      #количество строк в первой матрице
        column1=len(matrix1[0])   #Количество столбцов в первой матрице   
        row2=column1           #и строк во второй матрице
        column2=len(matrix2[0])   #количество столбцов во второй матрице
        for z in range(0,row1):
            for j in range(0,column2):
                for i in range(0,column1):
                   s=s+matrix1[z][i]*matrix2[i][j]
                temporary_matrix.append(s)
                s=0
            matrix3.append(temporary_matrix)
            temporary_matrix=[]           
    return matrix3
 
 #создание матриц
def creatematrix(row,column):
    temporary_matrix=[]
    matrix=[]
    for i in range(0,row):
        for j in range(0,column):
            temporary_matrix.append(random.randint(1,10))
        matrix.append(temporary_matrix)
        temporary_matrix=[]
    return matrix

 #main
def main():
    column1=1
    row2=2
    while column1!=row2:
        print("Кол-во столбцов первой матрицы должно быть = кол-ву строк второй матрицы")
        
        row1=input('Введите кол-во строк для первой матрицы > ')
        row1=int(row1)
            
        column1=input('Введите кол-во столбцов для первой матрицы > ')
        column1=int(column1)
            
        row2=input('Введите кол-во строк для второй матрицы > ')
        row2=int(row2)
        
            
        column2=input('Введите кол-во столбцов для второй матрицы > ')
        column2=int(column2)
            
        if row1 <= 0 or column1 <= 0 or row2 <= 0 or column2 <= 0:
            column1=1
            row2=2
            print('Дружок-пирожок, ты ввел отрицательные данные. Количество строк и столбцов не может быть меньше или равно 0. Попробуй-ка еще раз!')

 
    matrix1= creatematrix(row1,column1)
    matrix2= creatematrix(row2,column2)
    
    print('\nПервая матрица:')
    
    #nice print(выводит двумерный числовой список на экран построчно, разделяя числа пробелами внутри одной строки)
    for i in range(len(matrix1)):   
        for j in range(len(matrix1[i])):
            print(matrix1[i][j], end=' ')
        print()
 
    print('\nВторая матрица:')
    
    #nice print(выводит двумерный числовой список на экран построчно, разделяя числа пробелами внутри одной строки)
    for i in range(len(matrix2)):  
        for j in range(len(matrix2[i])):
            print(matrix2[i][j], end=' ')
        print()
 
    matrix3=matrixmult(matrix1,matrix2)
    print('\nПолучившаяся матрица:')
    
    #nice print(выводит двумерный числовой список на экран построчно, разделяя числа пробелами внутри одной строки)
    for i in range(len(matrix3)):   
        for j in range(len(matrix3[i])):
            print(matrix3[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()
