#logical operators..
#1.WAQTD NAMES OF THE EMPLOYEES WHO HAVE CHARACTER 'S' IN THEIR NAMES ? 
'''select * from employee where ename like "%s%";'''
#2.WAQTD NAMES OF THE EMPLOYEE IF THE EMP HAS CHAR 'A' PRESENT AT AT LEAST 2 TIMES ?
'''select * from employee where ename like "%a%a%";'''
#3.WAQTD NAMES OF THE EMPLOYEE IF THE EMP NAME STARTS WITH 'A' AND ENDS WITH 'A' ?
'''select * from employee where ename like "a%a";'''
#4.WAQTD NAMES OF THE EMPLOYEE IF THE EMP'S SALARY'S LAST 2 DIGIT IS 50 RUPEES ?
'''select * from employee where mod(sal,100)=50;'''
#5.AQTD NAMES OF THE EMPLOYEES HIRED IN NOVEMBER . ?
'''select * from employee where extract(month from hiredate)=11 ;'''
#6. LIST ALL THE EMPLOYEES WHO DON’T HAVE A REPORTING MANAGER ?
'''select * from employee where mgr is null ;'''
#7.LIST ALL THE EMPLOYEES WHO ARE HAVING REPORTING MANAGERS IN DEPT 10 ALONG WITH 10% HIKE IN SALARY'?
'''select * from employee where deptno=10 and mgr in ( select empno from employee)'''
#8.DISPLAY ALL THE EMPLOYEE WHO ARE ‘SALESMAN’S HAVING ‘E’ AS THE LAST BUT ONE CHARACTER IN ENAME BUT SALARY HAVING 
# EXACTLY 4 CHARACTER ?
'''select * from employee where job='salesman and ename like '%e_' and length(sal)=4; '''
#9.LIST THE EMPLOYEES WHO ARE NOT WORKING AS MANAGERS AND CLERKS IN DEPT 10 AND 20 WITH A SALARY IN THE RANGE OF 1k TO 3k? 
'''select * from employee where job not in ('clerk' and 'manager') and deptno in (10,20 ) and sal between 1000 and 3000; '''
#10.WAQTD NUMBER OF EMPLOYEES EARING MORE THAN 1500 IN DEPT 20?
'''select count(*) as nofemp's from employee where sal>1500 and deptno=20; ''' 
#11.WAQTD NUMBER OF DEPARTMENTS PRESENT IN EMPLOYEE TABLE ?
'''select count(distrint job ) as no of departments from employee;'''

