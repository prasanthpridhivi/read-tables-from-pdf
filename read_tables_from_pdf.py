import pandas as pd
from tabula import read_pdf
pdfFile = 'C:\\Users\\Prasanth Pridhivi\\Downloads\\INICET_result.pdf'
pdfFile2 = 'C:\\Users\\Prasanth Pridhivi\\Downloads\\INICET_result_2-end.pdf'
csvFile = 'C:\\Users\\Prasanth Pridhivi\\Downloads\\INICET_result.csv'

#totalPages = 2
totalPages = 792

d = []
data = read_pdf(pdfFile, pages='1')
dataString = str(data[0])
dataArray = dataString.split()
dataArray.insert(0, "Idx")
rollIndex = dataArray.index("Roll")
dataArray.pop(rollIndex+1)

unnamedIndex = dataArray.index("Unnamed:")
dataArray.pop(unnamedIndex+1)
mdIndex = dataArray.index("MD,")
del dataArray[mdIndex-1:mdIndex+14]
print(dataArray)

i = 0
while i < len(dataArray):
    _unnamedIdx = 4
    _dataArray = dataArray[i:i+9]
    _dataArray.pop(_unnamedIdx)
    d.append(_dataArray)
    i+=9

Ddata = read_pdf(pdfFile2, pages='all')
print(len(Ddata))
stop = 0
for p in range(len(Ddata)):
    DdataString = str(Ddata[p])
    DdataArray = DdataString.split()
    if stop == 1:
        break
    slNoIndex = DdataArray.index("Sl.No.")
    del DdataArray[slNoIndex:slNoIndex+8]
    i = 0
    while i < len(DdataArray):
        _dataArray = DdataArray[i:i+8]
        if "MDS" in _dataArray:
            stop = 1
            break
        else:    
            d.append(_dataArray)
            i+=8        



df = pd.DataFrame(d)
df.to_csv(csvFile)