#Лабораторная_6. Вариант_3: Из файла data.csv посчитать количество мужчин и количество женщин (отдельно – спасенных и погибших).
#Каждая строчка набора данных содержит следующие поля:
#1. Survived — обозначает, выжил данный пассажир или нет (0 для умерших, 1 для выживших);
#2. Pclass — класс пассажира (1 — высший, 2 — средний, 3 — низший);
#3. Name — имя;
#4. Sex — пол;
#5. Age — возраст;
#6. SibSp — количество братьев, сестер, сводных братьев, сводных сестер, супругов на борту титаника;
#7. Parch — количество родителей, детей (в том числе приемных) на борту титаника;
#8. Ticket — номер билета;
#9. Fare — плата за проезд;
#10. Cabin — каюта;
#11. Embarked — порт посадки (C — Шербур; Q — Квинстаун; S — Саутгемптон).

with open('data.csv','r') as file:
  male_Survived_0 = 0
  male_Survived_1 = 0
  female_Survived_0 = 0
  female_Survived_1 = 0
  for lines in file:
      data = lines.split(',')
      if data[1] == '1' and data[5].strip() == 'male':
          male_Survived_1 += 1
      elif data[1] == '0' and data[5].strip() == 'male':
          male_Survived_0 += 1
      elif data[1] == '1' and data[5].strip() == 'female':
          female_Survived_1 += 1
      elif data[1] == '0' and data[5].strip() == 'female':
          female_Survived_0 += 1

print("Мужчин среди пассажиров всего: ", male_Survived_1+male_Survived_0)
print("             из них спасенных: ", male_Survived_1)
print("              из них погибших: ", male_Survived_0)
print("Женщин среди пассажиров всего: ", female_Survived_1+female_Survived_0)
print("             из них спасенных: ", female_Survived_1)
print("              из них погибших: ", female_Survived_0)