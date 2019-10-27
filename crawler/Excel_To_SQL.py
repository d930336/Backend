import pandas as pd
import mysql.connector

class Convert_Excel_To_MySQL():
    def __init__(self,file_path):
        self.file_path = file_path
        self.df = pd.read_excel(file_path).dropna(thresh=3)
        self.col = list(self.df.columns)
    def Get_Value_To_Tuple(self):
        arr = []
        for i in self.df.index:
            row_val = []
            for col in self.col:
                row_val.append(self.df[col][i])
            arr.append(tuple(row_val))
        self.dataset = arr
    def Connect_To_Sql(self, conn , db):
        self._conn = conn
        self._db = db
        self._mycursor = self._conn.cursor()
        self._mycursor.execute('use ' + str(self._db))
    def Insert_To_SQL(self):
        sql = "insert into test_token_coupon"
My_Excel = Convert_Excel_To_MySQL("KFC1027.xlsx")
My_Excel.Get_Value_To_Tuple()
print(My_Excel.dataset)


