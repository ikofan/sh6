import datetime
import xlrd
import os
import django
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh6.settings")
django.setup()
"""
在 pycharm下的Run，Edit Configuration..
environment variable, 增加DJANGO_SETTINGS_MODULE", mywork.settings
同时from mema.models import Category, Post这种不能写在头上，必须在函数里，否则报错
ws.cell(row, 0).value，必须加上value，否则得到的内容时text：具体内容
xlrd处理日期，要单独写判断，ctype=3的日期
model里面的关联表格Category User, 引用到c[1]的级别就行，要保证时Cat类
p.create后就直接操作数据库写入记录了，不用p.save，也没有这个函数
参考：https://blog.csdn.net/ZT7524/article/details/89916879
"""


def imp(io):
    start_row = 1

    from codes.models import CodesH6, System, Packages, DriveType
    from django.contrib.auth.models import User

    wb = xlrd.open_workbook(io)
    ws = wb.sheet_by_name('NoG2')

    brief = benefits = ''

    nrows = ws.nrows
    for row in range(1, nrows):
        record = ws.row(row)

        # 处理brand
        if record[7] == 'H6':
            brand = 3
        elif record[7] == 'H6A':
            brand = 1
        elif record[7] == 'H6B':
            brand = 2
        else:
            brand = 0

        # 处理brief和Benefits
        # 排除没有html标签的
        if len(record[10].value) > 12:
            soup = BeautifulSoup(record[10].value, 'html.parser')
            # 先确定有没有brief和benefits这两个字段
            brief_benefits = soup.select('h1 a')
            brief_benefits_body = soup.select('div > .pit-content-par')

            if brief_benefits:
                if len(brief_benefits_body) == 2:
                    if brief_benefits[0].text == 'In Brief':
                        brief = str(brief_benefits_body[0].p)
                    else:
                        brief = ""
                        # 内容里面有可能没有Benefit，而是Offertext，还有可能只有Brief，连offertext都没有写
                    if brief_benefits[1].text == 'Benefits and Arguments':
                        benefits = str(brief_benefits_body[1])
                    else:
                        benefits = '<p>{}</p>'.format(brief_benefits[1].text) + str(brief_benefits_body[1])
                else:
                    if brief_benefits[0].text == 'In Brief':
                        brief = str(brief_benefits_body[0].p)
                    else:
                        brief = ""
            else:
                brief = benefits = ''
        else:
            brief = benefits = ''

        sql = CodesH6(
            name=record[0].value.strip(),
            title=record[1].value.strip(),
            comments=record[3].value.strip(),
            status=record[4].value,
            brand=brand,
            brief=brief,
            benefits=benefits,
            personal_comments=record[8].value,
            knowledge=record[9].value
        )
        sql.save()

        systems = record[2].value.split('/')
        for sys in systems:
            sql.system.add(System.objects.get(name=sys.strip()).id)

        if record[4]:
            if record[4] == 'H6' or 'H6A':
                if record[11]:
                    sql.drive_type.add(6)
                if record[12]:
                    sql.drive_type.add(5)
                if record[13]:
                    sql.drive_type.add(4)
            elif record[4] == 'H6B':
                if record[15]:
                    sql.drive_type.add(6)
                if record[16]:
                    sql.drive_type.add(5)
                if record[17]:
                    sql.drive_type.add(4)

        sql.save()


def main():
    io = r'D:\sh6-saef27.xlsx'
    imp(io)
    print('导入成功！')


if __name__ == '__main__':
    main()
