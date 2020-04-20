import xlrd
import os,sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
father_path = os.path.dirname(os.path.dirname(__file__))
dataExcel_path = father_path+'\pytestData.xlsx'
def getExcelData():
    oExcelData=xlrd.open_workbook(dataExcel_path).sheet_by_name('omplogin')
    oRowNums=oExcelData.nrows
    oColNums=oExcelData.ncols
    oKeys=oExcelData.row_values(0)
    dataList=[]
    j=1
    for i in range(oRowNums-1):
        values = oExcelData.row_values(j)
        dict={}
        for x in range(oColNums):
            dict[oKeys[x]]=values[x]
        dataList.append(dict)
        j=j+1
    return dataList
@pytest.fixture(scope='module')
def omplogin(request):
    username=request.param['username']
    password=request.param['password']
    expected = request.param['expected']
    return (username,password,expected)

