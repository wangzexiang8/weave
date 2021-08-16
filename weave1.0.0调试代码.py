import os
import sys


# 变量容器
# ——————————————————————————————————————————————————————————————————

var_name_list = []
var_value_list = []

# __________________________________________________________________
path = input('文件所在路径:')

for file in os.listdir(path):
    count = 0
    for word in file:
        count = count + 1
        if word == '.':
            file_name = file[count:]

            if file_name == 'txt':
                file_path = path + '\\' + file
                for code in open(file_path):
                    print("weave代码是：" + code)
                    c_count = -1

                    for n in code:
                        c_count = c_count + 1

                        if n == ' ':
                            print("空格位置是：" + str(c_count))
                            ins_code = code[:c_count]
                            print("控制语句是：" + ins_code)

                            # -------------------------------------------------------------------------------------
                            # ins_code 控制语句

                            if ins_code == "print":
                                count_print = -1
                                for print_word in code:
                                    count_print = count_print + 1
                                    if print_word == '<':
                                        print('______________________运行结果________________________')
                                        print(str(code[c_count + 1:count_print]))
                                        print('_____________________________________________________')
                                    if print_word == '?':
                                        for sy, ww in enumerate(code):

                                            if ww == '+':
                                                print('______________________运行结果________________________')
                                                var_js_f = code[c_count + 1:sy]
                                                var_js_s = code[sy + 1:count_print]
                                                for j, var_f in enumerate(var_name_list):
                                                    if var_f == var_js_f:
                                                        var_js_f_num = var_value_list[int(j)]
                                                        for jj, var_s in enumerate(var_name_list):
                                                            if var_s == var_js_s:
                                                                var_js_s_num = var_value_list[int(jj)]
                                                                print(int(var_js_f_num) + int(var_js_s_num))
                                                print('_____________________________________________________')

                                            if ww == '-':
                                                print('______________________运行结果________________________')
                                                var_js_f = code[c_count + 1:sy]
                                                var_js_s = code[sy + 1:count_print]
                                                for j, var_f in enumerate(var_name_list):
                                                    if var_f == var_js_f:
                                                        var_js_f_num = var_value_list[int(j)]
                                                        for jj, var_s in enumerate(var_name_list):
                                                            if var_s == var_js_s:
                                                                var_js_s_num = var_value_list[int(jj)]
                                                                print(int(var_js_f_num) - int(var_js_s_num))
                                                print('_____________________________________________________')

                                            if ww == '*':
                                                print('______________________运行结果________________________')
                                                var_js_f = code[c_count + 1:sy]
                                                var_js_s = code[sy + 1:count_print]
                                                for j, var_f in enumerate(var_name_list):
                                                    if var_f == var_js_f:
                                                        var_js_f_num = var_value_list[int(j)]
                                                        for jj, var_s in enumerate(var_name_list):
                                                            if var_s == var_js_s:
                                                                var_js_s_num = var_value_list[int(jj)]
                                                                print(int(var_js_f_num) * int(var_js_s_num))
                                                print('_____________________________________________________')

                                            if ww == '/':
                                                print('______________________运行结果________________________')
                                                var_js_f = code[c_count + 1:sy]
                                                var_js_s = code[sy + 1:count_print]
                                                for j, var_f in enumerate(var_name_list):
                                                    if var_f == var_js_f:
                                                        var_js_f_num = var_value_list[int(j)]
                                                        for jj, var_s in enumerate(var_name_list):
                                                            if var_s == var_js_s:
                                                                var_js_s_num = var_value_list[int(jj)]
                                                                print(int(var_js_f_num) / int(var_js_s_num))
                                                print('_____________________________________________________')

                            if ins_code == "int":
                                print("由于基于python编写，不会发生整型截断")
                                count_is = -1
                                for make_word in code:
                                    count_is = count_is + 1
                                    if make_word == "=":
                                        var_name_list.append(code[c_count + 1:count_is])
                                        var_value_list.append(int(code[count_is + 1:]))
                                        print(var_name_list)
                                        print(var_value_list)

                            if ins_code == "str":
                                print('----------------------------------------------------------')
                                print("警告：str()函数正在维护")
                                print("暂不支持str()函数的操作")
                                print("不会影响代码继续执行")
                                print("系统建议删除此变量")
                                print('-----------------------------------------------------------')
                                # count_is = -1
                                # for make_word in code:
                                #     count_is = count_is + 1
                                #     if make_word == "=":
                                #         var_name_list.append(code[c_count+1:count_is])
                                #         var_value_list.append(code[count_is+1:])
                                #         print(var_name_list)
                                #         print(var_value_list)

                            else:
                                print("已忽略此行")
                        else:
                            pass
            else:
                pass
        else:
            pass



