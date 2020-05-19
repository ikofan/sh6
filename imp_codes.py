import datetime
import xlrd
import os
import django

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


def imp_codes(io):
    start_row = 1

    from codes.models import CodesH6, System, Packages
    from django.contrib.auth.models import User

    wb = xlrd.open_workbook(io)
    ws = wb.sheet_by_name('NoG')

    codes_db = CodesH6.objects.all()
    system_db = System.objects.all()
    packages_db = Packages.objects.all()

    name_col = ws.col_values(0, start_row)
    title_col = ws.col_values(1, start_row)
    system_col = ws.col_values(2,start_row)
    comments_col = ws.col_values(3,start_row)
    status_col = ws.col_values(4,start_row)
    res_w_col = ws.col_values(5,start_row)
    res_not_w_col = ws.col_values(6,start_row)
    brand_col = ws.col_values(7,start_row)
    # 驱动先删掉，得单独处理
    # drive_col = ws.col_values(8,start_row)
    a64_col = ws.col_values(13,start_row)
    a62_col = ws.col_values(14, start_row)
    a42_col = ws.col_values(15, start_row)
    b64_col = ws.col_values(18, start_row)
    b62_col = ws.col_values(19, start_row)
    b42_col = ws.col_values(20, start_row)

    package_col = ws.col_values(9,start_row)
    personal_col = ws.col_values(10,start_row)
    knowledge_col = ws.col_values(11,start_row)
    content_col = ws.col_values(12,start_row)

    for name, title, system, comments, status, res_w, res_not_w, brand, package, personal, knowledge, content,a64,a62,a42,b64,b62,b42 in zip(name_col, title_col, system_col, comments_col, status_col, res_w_col, res_not_w_col, brand_col, package_col, personal_col, knowledge_col, content_col,a64_col,a62_col,a42_col,b64_col,b62_col,b42_col):
        if brand == 'H6':
            brand = 3
        elif brand == 'H6A':
            brand = 1
        elif brand == 'H6B':
            brand =2
        else:
            brand = ""


        (code, result) = CodesH6.objects.get_or_create( name = name,
                                                        title = title,
                                                        # system = system,
                                                        comments = comments,
                                                        status = status,
                                                        restriction_with = res_w,
                                                        restriction_not_with = res_not_w,
                                                        # brand = brand,
                                                        # package = "",
                                                        personal_comments = personal,
                                                        knowledge = knowledge,
                                                        content = content,
                                                        owner_id = 3
                                                       )
        if result:
            system_list = system.split('/')
            for ss in system_list:
                for sys_item in system_db:
                    if ss == sys_item.name:
                        code.system.add(sys_item)

            if brand == 'H6' or brand == 'H6A':
                if a64 != "":
                    a64_val = 1
                    code.drive_type.add(a64_val)
                if a62 != "":
                    a62_val = 2
                    code.drive_type.add(a62_val)
                if a42 != "":
                    a42_val = 3
                    code.drive_type.add(a42_val)

            elif brand == 'H6B':
                for item in [b64,b62,b42]:
                    if item != "":
                        code.drive_type.add(item)


def main():
    io = r'C:\Users\kapa\OneDrive\工作文档\sh6-saef27.xlsx'
    imp_codes(io)
    print('导入成功！')


if __name__ == '__main__':
    main()