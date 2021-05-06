import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib import style

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

outer_name = ['Iron', 'Bronze', 'Silver','Gold', 'Platinum', 'Diamond', 'Titan', 'Immortal']
outer_size = [4.143, 38.61, 35.617, 13.939, 5.7, 1.283, 0.246, 0.167]

inner_name = ['Iron4', 'Iron3', 'Iron2', 'Iron1', 'Bronze4', 'Bronze3', 'Bronze2', 'Bronze1', 'Silver4', 'Silver3', 'Silver2', 'Silver1', 'Gold4', 'Gold3', 'Gold2', 'Gold1', 'Platinum4', 'Platinum3', 'Platinum2', 'Platinum1', 'Diamond4', 'Diamond3', 'Diamond2', 'Diamond1', 'Titan1', 'Immortal1']
inner_size = [0.028, 0.093, 0.639, 3.383, 9.235, 8.911, 9.398, 11.066, 10.241, 10.065, 8.420, 6.891, 5.403, 3.624, 2.600, 2.312, 2.224,1.696, 0.978, 0.802, 0.686, 0.375, 0.297, 0.222, 0.246, 0.167]


width_num = 0.4

fig, ax = plt.subplots()

ax.axis('equal')

pie_outside, _ = ax.pie(outer_size, radius = 1.3, labels = outer_name, labeldistance = 0.8)

plt.setp(pie_outside, width = width_num, edgecolor = 'white')

pie_inside, plt_labels, junk = \
ax.pie(inner_size, radius=(1.3 - width_num), labels=inner_name, labeldistance=0.75, autopct='%1.1f%%')

plt.setp(pie_inside, width=width_num, edgecolor='white')

plt.title('블랙서바이벌 영원회귀의 티어 분포표', fontsize=30)

plt.show()

