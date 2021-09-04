import GetDiamondList

if __name__ == '__main__':
    prod_list = GetDiamondList.getDiamondList()
    GetDiamondList.insertIntoDatabase(prod_list, host='', port='', user='', password='', database='')