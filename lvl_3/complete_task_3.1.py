class Matrix:
    def __init__(self, num_x, num_y, n):
        self.num_x = num_x
        self.num_y = num_y
        if  0 < n:
            self.s = [[n] * num_y for _ in range(num_x)]
        else:
            self.s = [[None] * num_y for _ in range(num_x)]     

    
    def get_sense(self, x, y):
        if 0 <= y < self.num_x and 0 <= x < self.num_y:
            return self.s[x][y]        
       
           
    def get_num_y(self):
        return self.num_y

    def get_num_x(self):
        return self.num_x

    def screen(self):
        for y in self.s:
            print(y) 

    def pt(self):
        print("Число строк:", matrix.get_num_x())
        print("Число колонок:", matrix.get_num_y())        


    # Примеры матрицы:
matrix = Matrix(8, 8, 8)
matrix.screen()
print()
matrix.pt()

# [8, 8, 8, 8, 8, 8, 8, 8]
# [8, 8, 8, 8, 8, 8, 8, 8]
# [8, 8, 8, 8, 8, 8, 8, 8]
# [8, 8, 8, 8, 8, 8, 8, 8]
# [8, 8, 8, 8, 8, 8, 8, 8]
# [8, 8, 8, 8, 8, 8, 8, 8]
# [8, 8, 8, 8, 8, 8, 8, 8]
# [8, 8, 8, 8, 8, 8, 8, 8]

# Число строк: 8
# Число колонок: 8

matrix = Matrix(3, 2, -1)
matrix.screen()
matrix.pt()

# [None, None]
# [None, None]
# [None, None]

# Число строк: 3
# Число колонок: 2               
        
