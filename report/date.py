from __future__ import  unicode_literals
import cx_Oracle

# 人员总规模
pp=1512

# 人员学历
zhongzhuan=119
dazhuan=686
benke=583
shuoshi=111
qita=13

# 累计HPV
HPV=18.73
# 出勤人数
# ['冲压', '车身', '油漆', '总装']
# [120, 200, 150, 500]




# 当班累计一次通过率
# ['周一','周二','周三','周四','周五','周六','周日']
onepass=[60, 50, 66, 48, 50, 40, 60]

# 月度实时产量
# [120, 200, 150, 500, 200, 480, 5000, 4000, 20000, 1000, 4777, 1344]
def  current_month():
    tns = cx_Oracle.makedsn('10.110.8.158', 1521, 'zzmapogg')
    db = cx_Oracle.connect('ZZ_IMAP_OWIMAP', 'Pass1q2w##', tns)
    cr = db.cursor()
    currentmonth_r = cr.execute(''' 
           SELECT SUM(T.COUNT)
  FROM TB_VEHICLE_MONTH_SUMMARY T
 WHERE T.PRODUNITNO = 'QA2'
   AND T.ULOCROUTENO = 200
   AND T.YEAR = TO_CHAR(SYSDATE, 'YYYY')
   AND T.MONTH IN (SELECT MAX(a.month)
                     FROM TB_VEHICLE_MONTH_SUMMARY a
                    where a.year = to_char(sysdate, 'YYYY'))
 GROUP BY T.MONTH
 ORDER BY T.MONTH

                ''').fetchall()
    currentmonth = []
    for field in currentmonth_r:
        currentmonth.append(field[0])
    db.close()
    return  currentmonth[0]

def month_m():
    tns = cx_Oracle.makedsn('10.110.8.158', 1521, 'zzmapogg')
    db = cx_Oracle.connect('ZZ_IMAP_OWIMAP', 'Pass1q2w##', tns)
    cr = db.cursor()
    month_r = cr.execute(''' 
           SELECT DISTINCT T.MONTH FROM TB_VEHICLE_MONTH_SUMMARY T ORDER BY T.MONTH
                ''').fetchall()
    month1 = []
    for field in month_r:
        month1.append(field[0])
    db.close()
    return  month1


# 月度产量
def month_out():
    tns = cx_Oracle.makedsn('10.110.8.158', 1521, 'zzmapogg')
    db = cx_Oracle.connect('ZZ_IMAP_OWIMAP', 'Pass1q2w##', tns)
    cr = db.cursor()
    month = cr.execute(''' 
           SELECT SUM(T.COUNT)
 FROM TB_VEHICLE_MONTH_SUMMARY T
WHERE T.PRODUNITNO = 'QA2'
  AND T.ULOCROUTENO = 200
  AND T.YEAR = TO_CHAR(SYSDATE, 'YYYY')
  AND T.MONTH IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
GROUP BY T.MONTH
ORDER BY T.MONTH
                ''').fetchall()
    monthout = []
    for field in month:
        monthout.append(field[0])
    db.close()
    return  monthout


# 合理化建议
# [120, 200, 150, 500,200,480,500,400,200,100,77,134]
suggest=[1833,1567,1725,1550,1300,1589,1525,1547]

# 当班实时产量
def shift_out():
    tns = cx_Oracle.makedsn('10.110.8.158', 1521, 'zzmapogg')
    db = cx_Oracle.connect('ZZ_IMAP_OWIMAP', 'Pass1q2w##', tns)
    cr = db.cursor()
    shiftout = cr.execute(''' 
          SELECT SUM(T.COUNT)
  FROM TB_VEHICLE_SUMMARY T
 WHERE T.WORKDATE =
       TO_DATE(TO_CHAR(SYSDATE, 'yyyy-mm-dd'), 'yyyy-mm-dd')
   AND T.PRODUNITNO = '1C3'
   AND T.SHIFTNO = 1
   AND T.ULOCROUTENO = 200
                ''').fetchall()
    shift = []
    for field in shiftout:
        shift.append(field[0])
    db.close()
    return  shift[0]



# 绿十字当前日
def day():
        tns = cx_Oracle.makedsn('10.110.8.158', 1521, 'zzmapogg')
        db = cx_Oracle.connect('ZZ_IMAP_OWIMAP', 'Pass1q2w##', tns)
        cr = db.cursor()
        day_r = cr.execute(''' 
            SELECT TO_CHAR(SYSDATE, 'DD') FROM DUAL
                    ''').fetchall()
        cur_day = []
        for field in day_r:
            cur_day.append(field[0])
        db.close()
        return cur_day[0]

# 绿十字日期列表
list=['','',1,2,3,'','','','',4,5,6,'','',7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,'','',28,29,30,'','','','','.','.','.','','']

#开动率
PR=85.65
BS=86.84
PS=95.38
GA=84.64
#月度产值
month_value=[17.4,10.2,16.4,9.6,11.7,12.4,9.5,12.8]

sumvalue=month_value[0]+month_value[1]+month_value[2]+month_value[3]+month_value[4]+month_value[5]+month_value[6]+month_value[7]