import os


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
            if file_name == 'wv':
                file_path = path + '\\' + file
                for code in open(file_path):
                    c_count = -1
                    for n in code:
                        c_count = c_count + 1
                        if n == ' ':
                            ins_code = code[:c_count]

                            # -------------------------------------------------------------------------------------
                            # ins_code 控制语句

                            if ins_code == "print":
                                count_print = -1
                                for print_word in code:
                                    count_print = count_print + 1
                                    if print_word == '<':
                                        print(str(code[c_count + 1:count_print]))
                                    elif print_word == '?':
                                        for sy, ww in enumerate(code):
                                            if ww == '+':
                                                var_js_f = code[c_count + 1:sy]
                                                var_js_s = code[sy + 1:count_print]
                                                for j, var_f in enumerate(var_name_list):
                                                    if var_f == var_js_f:
                                                        var_js_f_num = var_value_list[int(j)]
                                                        for jj, var_s in enumerate(var_name_list):
                                                            if var_s == var_js_s:
                                                                var_js_s_num = var_value_list[int(jj)]
                                                                print(var_js_f_num + var_js_s_num)

                                            elif ww == '-':
                                                var_js_f = code[c_count + 1:sy]
                                                var_js_s = code[sy + 1:count_print]
                                                for j, var_f in enumerate(var_name_list):
                                                    if var_f == var_js_f:
                                                        var_js_f_num = var_value_list[int(j)]
                                                        for jj, var_s in enumerate(var_name_list):
                                                            if var_s == var_js_s:
                                                                var_js_s_num = var_value_list[int(jj)]
                                                                print(var_js_f_num - var_js_s_num)

                                            elif ww == '*':
                                                var_js_f = code[c_count + 1:sy]
                                                var_js_s = code[sy + 1:count_print]
                                                for j, var_f in enumerate(var_name_list):
                                                    if var_f == var_js_f:
                                                        var_js_f_num = var_value_list[int(j)]
                                                        for jj, var_s in enumerate(var_name_list):
                                                            if var_s == var_js_s:
                                                                var_js_s_num = var_value_list[int(jj)]
                                                                print(var_js_f_num * var_js_s_num)

                                            elif ww == '/':
                                                var_js_f = code[c_count + 1:sy]
                                                var_js_s = code[sy + 1:count_print]
                                                for j, var_f in enumerate(var_name_list):
                                                    if var_f == var_js_f:
                                                        var_js_f_num = var_value_list[int(j)]
                                                        for jj, var_s in enumerate(var_name_list):
                                                            if var_s == var_js_s:
                                                                var_js_s_num = var_value_list[int(jj)]
                                                                print(var_js_f_num / var_js_s_num)
                                            else:
                                                pass
                                    else:
                                        pass
                            elif ins_code == "int":
                                count_is = -1
                                for make_word in code:
                                    count_is = count_is + 1
                                    if make_word == "=":
                                        var_name_list.append(code[c_count + 1:count_is])
                                        var_value_list.append(int(code[count_is + 1:]))

                            elif ins_code == "str":
                                fenge = code.split(" ")
                                use_code = fenge[1]
                                for x, i in enumerate(use_code):
                                    if i == "=":
                                        var_name_list.append(use_code[:x])
                                        var_value_list.append(use_code[x+1:-1])
                                    else:
                                        pass

                            elif ins_code == "input":
                                for xh, i in enumerate(code):
                                    if i == "=":
                                        var_name_list.append(code[c_count+1:xh])
                                        for xxh, b in enumerate(code):
                                            if b == "%":
                                                if code[xxh+1] == "d":
                                                    var_value_list.append(int(input()))
                                                elif code[xxh+1] == "s":
                                                    var_value_list.append(str(input()))
                                                else:
                                                    pass
                                            else:
                                                pass
                            else:
                                pass
                        else:
                            pass
            else:
                pass
        else:
            pass
