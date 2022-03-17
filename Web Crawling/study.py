import csv

f = open('./covid19_articles.csv', 'r', encoding="euc-kr")

rdr = csv.reader(f)
# 'rdr'의 첫 번째는 건너뜀
next(rdr)

title_num = 0
for row in rdr:
    idx = row[0].strip()
    weather = row[1].strip()
    title = row[2].strip()
    if '[속보]' in title:
        print(title)
        title_num += 1
print(f'속보 기사 개수: {title_num}')

f.close()