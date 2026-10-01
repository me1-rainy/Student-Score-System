
#这三行为了确定当前文件的绝对路径，防止文件找不到
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "students_cjglxt.txt")

students={}
def save_data(students,file_path):
    with open(file_path,"w",encoding="utf-8") as f:
        for student in students.values():
            f.write(f"{student['name']},{student['score']}\n")
    print("已保存学生信息到文件")

#为了在退出的时候提供保存提示，设置一个变量
has_changed=False
try:
    with open(file_path,"r",encoding="utf-8") as f:
        for line in f:
          #防止对txt文件的分数直接修改，导致的float转换失败
          try:
            clean_line=line.strip()
            parts=clean_line.split(",")
            name=parts[0]
            score=float(parts[1])
            students[name]={"name":name,"score":score}
          except (ValueError, IndexError):
            print(f"跳过无效行: {line}").strip()
            continue
except FileNotFoundError:
    print("暂无历史数据，请录入新学生")    

print(f"已读取{len(students)}条记录")

while True:
    print()
    print("===== 学生成绩管理系统 ======")
    print("1.添加 2.查看全部 3.查询 4.删除")
    print("5.统计 6.保存      0.退出")
    choice=input("请选择功能： ")

    if choice=="1":
        #姓名为空或者重名的防御处理
        while True:
            name=input("请输入姓名： ").strip()
            if len(name)==0:
                print("姓名不能为空，请重新输入！")
            elif name in students:
                print("该学生已存在，请重新输入！")
            else:
                break
        #分数输入防御处理
        while True:
            try:
                score=float(input("请输入分数： "))
                break
            except ValueError:
                print("输入的分数无效，请重新输入！")
        students[name]={"name":name,"score":score}
        print(f"已录入：{name} {score}分")
        has_changed=True
    elif choice=="2":
        print("所有学生如下：")
        for student in students.values():
            print(f"{student['name']},{student['score']}分")
    elif choice=="3":
        name=input("请输入要查找的学生姓名： ").strip()
        if name in students:
            print(f"学生信息：{students[name]['name']}，分数：{students[name]['score']}")
        else:
            print("未查询到该学生信息！")
    elif choice=="4":
        name=input("请输入要删除的学生姓名： ").strip()
        if name in students:
            del students[name]
            print(f"已删除学生：{name}")
            has_changed=True
        else:
            print("未查询到该学生信息！")
    elif choice=="5":
        print(f"学生人数：{len(students)}")
        scores=[]
        for student in students.values():
            scores.append(student['score'])
        scores.sort()
        if len(scores)>0:
            print(f"平均分：{sum(scores)/len(scores):.1f}")
            print(f"最高分：{scores[-1]}")
            print(f"最低分：{scores[0]}")
            sum_count=sum(1 for score in scores if score>=60)
            print(f"及格率：{sum_count/len(scores)*100:.1f}%")
        else:
            print("暂无学生信息")
    elif choice=="6":
        save_data(students, file_path)
        has_changed=False
    elif choice=="0":
        if has_changed:
            save_choice=input("有未保存的更改，是否保存？(y/n)").strip().lower()
            if save_choice=="y":
                save_data(students, file_path)
        print("退出系统")
        break
    else:
        print("无效的选择，请重新输入！")

#接下来展示试例运行结果
#第一次我们初始分配了错误的txt： A,100.0
#                             B,95.9
#                             C,abc

#跳过无效行: C,abc

#已读取2条记录

#===== 学生成绩管理系统 ======
#1.添加 2.查看全部 3.查询 4.删除
#5.统计 6.保存      0.退出
#请选择功能： 1
# 请输入姓名： C
# 请输入分数： 88.8
# 已录入：C 88.8分

# ===== 学生成绩管理系统 ======
# 1.添加 2.查看全部 3.查询 4.删除
# 5.统计 6.保存      0.退出
# 请选择功能： 2
# 所有学生如下：
# A,100.0分
# B,95.9分
# C,88.8分

# ===== 学生成绩管理系统 ======
# 1.添加 2.查看全部 3.查询 4.删除
# 5.统计 6.保存      0.退出
# 请选择功能： 3
# 请输入要查找的学生姓名： B
# 学生信息：B，分数：95.9

# ===== 学生成绩管理系统 ======
# 1.添加 2.查看全部 3.查询 4.删除
# 5.统计 6.保存      0.退出
# 请选择功能： 4
# 请输入要删除的学生姓名： A
# 已删除学生：A

# ===== 学生成绩管理系统 ======
# 1.添加 2.查看全部 3.查询 4.删除
# 5.统计 6.保存      0.退出
# 请选择功能： 5
# 学生人数：2
# 平均分：92.3
# 最高分：95.9
# 最低分：88.8
# 及格率：100.0%

# ===== 学生成绩管理系统 ======
# 1.添加 2.查看全部 3.查询 4.删除
# 5.统计 6.保存      0.退出
# 请选择功能： 0
# 有未保存的更改，是否保存？(y/n)y
# 已保存学生信息到文件
# 退出系统
