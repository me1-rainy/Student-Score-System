students={}
try:
    with open("students_cjglxt.txt","r",encoding="utf-8") as f:
        for line in f:
          clean_line=line.strip()
          parts=clean_line.split(",")
          name=parts[0]
          score=float(parts[1])
          students[name]={"name":name,"score":score}
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
        name=input("请输入姓名： ")
        score=float(input("请输入分数： "))
        students[name]={"name":name,"score":score}
        print(f"已录入：{name} {score}分")
    elif choice=="2":
        print("所有学生如下：")
        for student in students.values():
            print(f"{student['name']},{student['score']}分")
    elif choice=="3":
        name=input("请输入要查找的学生姓名： ")
        if name in students:
            print(f"学生信息：{students[name]['name']}，分数：{students[name]['score']}")
        else:
            print("未查询到该学生信息！")
    elif choice=="4":
        name=input("请输入要删除的学生姓名： ")
        if name in students:
            del students[name]
            print(f"已删除学生：{name}")
        else:
            print("未查询到该学生信息！")
    elif choice=="5":
        print(f"学生人数：{len(students)}")
        scores=[]
        for student in students.values():
            scores.append(student['score'])
        scores.sort()
        if len(scores)>0:
            print(f"平均分：{sum(scores)/len(scores)}:.1f")
            print(f"最高分：{scores[-1]}")
            print(f"最低分：{scores[0]}")
            sum_count=sum(1 for score in scores if score>=60)
            print(f"及格率：{sum_count/len(scores)*100:.1f}%")
        else:
            print("暂无学生信息")
    elif choice=="6":
        with open("students_cjglxt.txt","w",encoding="utf-8") as f:
            for student in students.values():
                f.write(f"{student['name']},{student['score']}\n")
        print("已保存学生信息到文件")
    elif choice=="0":
        print("退出系统")
        break
    else:
        print("无效的选择，请重新输入！")

    

            

