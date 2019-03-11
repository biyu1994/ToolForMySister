# coding 'utf-8'
import xlrd
import re


def read_excel():
    workbook = xlrd.open_workbook(u'.\ToolsForMySister\面试安排表201901-03(5).xlsx')
    sheet_names = workbook.sheet_names()
    data = {}
    for i in sheet_names:
        a = workbook.sheet_by_name(i)
        Countrows = a.nrows
        for j in range(Countrows):
            row = a.row_values(j)
            # print(row[0],row[1])
            if row[0].replace(' ', '') == '地区' and row[1].replace(' ',
                                                                  '') == '职位':
                first_valid_data = j
                break
        coldata = []
        for k in range(len(a.row_values(first_valid_data))):
            # print(a.row_values(first_valid_data)[k])
            p = re.compile(r'.*面.*情况$')
            if p.search(a.row_values(first_valid_data)[k].replace(' ', '')):
                coldata.append(k)
        for row in range(first_valid_data + 1, Countrows):
            b = a.row_values(row)
            # print(b[2])
            # print(b[2],b[coldata[0]],b[coldata[1],'aaa')
            data[str(
                b[2])] = [str(b[coldata[0]]),
                          str(b[coldata[1]]),
                          str(b[5])]
            # data = dict(str(b[2])='a')
    outdata = {}
    for i,v in data.items():
        out = re.compile(r'.*淘汰.*')
        if out.search(v[0]) or out.search(v[1]):
            outdata[i] = v
    return outdata
