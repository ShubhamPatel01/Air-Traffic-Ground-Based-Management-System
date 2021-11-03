from datetime import date
from datetime import time
from datetime import datetime
import sqlite3
connection=sqlite3.connect('database1.db')
cursor=connection.cursor()
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS admin (username	TEXT, password	TEXT NOT NULL,PRIMARY KEY(username))")
    cursor.execute("CREATE TABLE IF Not EXISTS status (s_id	INTEGER,s_detail	TEXT NOT NULL,PRIMARY KEY(s_id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS terminal(t_id INTEGER,t_name	TEXT NOT NULL, PRIMARY KEY(t_id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS parking (p_id	INTEGER,p_name	TEXT NOT NULL,t_id	INTEGER NOT NULL,\
        routepark BLOB NOT NULL,routerun BLOB NOT NULL,pv INTEGER NOT NULL,FOREIGN KEY(t_id) REFERENCES terminal(t_id) ON UPDATE CASCADE ON DELETE CASCADE,PRIMARY KEY(p_id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS flttype (ft_id	INTEGER, ft_det	TEXT NOT NULL, PRIMARY KEY(ft_id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS CREATE TABLE flight (f_id	INTEGER,at	TEXT,dt	TEXT, s_id	INTEGER DEFAULT 0,\
	ft_id	INTEGER NOT NULL,p_id	INTEGER,flt_no	TEXT NOT NULL, flt_name	TEXT NOT NULL, Emg	TEXT NOT NULL, Ac_id	TEXT NOT NULL, Arrfrom	TEXT, Deptto	TEXT,\
	FOREIGN KEY(p_id) REFERENCES parking(p_id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY(s_id) REFERENCES status(s_id) ON UPDATE CASCADE ON DELETE CASCADE,PRIMARY KEY(f_id))")

def data_entry():
    cursor=connection.cursor()
    def convertToBinaryData(filename):
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData
    cursor.execute("INSERT INTO status VALUES (0,'IN AIR'),(1,'LANDED'),(2,'TAXI TOWARDS PARKING AND PARKED'),(3,'TAXI TOWARDS RUNWAY'),(4,'TAKEOFF PERMISSION GIVEN AND TAKEN OFF')")
    cursor.execute("INSERT INTO terminal VALUES (1,'T1'),(2,'T2'),(3,'HANGARS'),(4,'OPEN AREA')")
    for i in range(1,9):
        a=convertToBinaryData(f'P{i}-LN.png')
        b=convertToBinaryData(f'P{i}-TF.png')
        cursor.execute("INSERT INTO parking VALUES (?,?,1,?,?,1)",(i,f'P{i}',a,b))
    for i in range(9,16):
        a=convertToBinaryData(f'P{i}-LN.png')
        b=convertToBinaryData(f'P{i}-TF.png')
        cursor.execute("INSERT INTO parking VALUES (?,?,2,?,?,1)",(i,f'P{i}',a,b))
    for i in range(16,21):
        a=convertToBinaryData(f'P{i}-LN.png')
        b=convertToBinaryData(f'P{i}-TF.png')
        cursor.execute("INSERT INTO parking VALUES (?,?,3,?,?,1)",(i,f'P{i}',a,b))
    for i in range(21,26):
        a=convertToBinaryData(f'P{i}-LN.png')
        b=convertToBinaryData(f'P{i}-TF.png')
        cursor.execute("INSERT INTO parking VALUES (?,?,4,?,?,1)",(i,f'P{i}',a,b))
    cursor.execute("INSERT INTO flttype VALUES (1,'Domestic Commercial'),(2,'International Commercial'),(3,'Cargo'),(4,'Private')")
    connection.commit()
    cursor.close()
    
def verify(i,j):
    entered=(i,j)
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM admin")
    data=cursor.fetchall()
    cursor.close()
    if entered in data:
        return True
    else:
        return False

def addEntry(fno,atime,dtime,fltd,flid,flna,emer,acid,arf,dept):
    if fltd=='Domestic Commercial':
        a=1
    elif fltd=='International Commercial':
        a=2
    elif fltd=='Cargo':
        a=4
    elif fltd=='Private':
        a=3
    cursor.execute("INSERT INTO flight values (?,?,?,0,?,NULL,?,?,?,?,?,?) ",(fno,atime,dtime,a,flid,flna,emer,acid,arf,dept))
    connection.commit()

def t1_status():
    cursor=connection.cursor()
    cursor.execute("SELECT p_name from parking where t_id=1 and pv=0")
    data=cursor.fetchall()
    cursor.close()
    return data
    
def t2_status():
    cursor=connection.cursor()
    cursor.execute("SELECT p_name from parking where t_id=2 and pv=0")
    data=cursor.fetchall()
    cursor.close()
    return data
def op_status():
    cursor=connection.cursor()
    cursor.execute("SELECT p_name from parking where t_id=4 and pv=0")
    data=cursor.fetchall()
    cursor.close()
    return data

def hg_status():
    cursor=connection.cursor()
    cursor.execute("SELECT p_name from parking where t_id=3 and pv=0")
    data=cursor.fetchall()
    cursor.close()
    return data

def rtl():
    cursor=connection.cursor()
    cursor.execute("SELECT F.f_id,F.at,F.dt,F.ac_id,FT.ft_det,F.flt_no,F.flt_name,F.Arrfrom from flight F NATURAL JOIN flttype FT where F.s_id=0 ORDER BY F.at LIMIT 8")
    data=cursor.fetchall()
    cursor.close()
    return data

def ptl(id):
    cursor=connection.cursor()
    cursor.execute("UPDATE flight set s_id=1 where f_id=?",(id,))
    connection.commit()
    cursor.close()

def law():
    cursor=connection.cursor()
    cursor.execute("SELECT F.f_id,F.at,F.dt,F.ac_id,FT.ft_det,F.flt_no,F.flt_name,Arrfrom from flight F NATURAL JOIN flttype FT WHERE F.S_ID=1 and F.p_id IS NULL ORDER BY F.at LIMIT 8")
    data=cursor.fetchall()
    cursor.close()
    return data
    
def pallot(id):
    cursor=connection.cursor()
    cursor.execute("SELECT ft_id from flight where f_id=?",(id,))
    data1=cursor.fetchone()
    j=data1[0]
    if j==1:
        cursor.execute("SELECT p_id FROM parking where t_id=1 and pv=1")
        data=cursor.fetchone()
    elif j==2:
        cursor.execute("SELECT p_id FROM parking where t_id=2 and pv=1")
        data=cursor.fetchone()
    elif j==3:
        cursor.execute("SELECT p_id FROM parking where t_id=3 and pv=1")
        data=cursor.fetchone()
    elif j==4:
        cursor.execute("SELECT p_id FROM parking where t_id=4 and pv=1")
        data=cursor.fetchone()
    if data==None:
        return False
    i=data[0]
    cursor.execute("UPDATE flight set p_id=? where f_id=?",(i,id))
    connection.commit()
    cursor.execute("UPDATE parking set pv=? where p_id=?",(0,i))
    connection.commit()
    return True

def usttp(id):
    cursor=connection.cursor()
    cursor.execute("UPDATE FLIGHT SET S_ID=2 WHERE F_ID=?",(id,))
    connection.commit()
    cursor.close
    
def rttp():
    cursor=connection.cursor()
    cursor.execute("SELECT F.f_id,F.at,F.dt,F.Arrfrom,F.Deptto,FT.ft_det,F.flt_no,P.p_name from flttype FT NATURAL JOIN flight F NATURAL JOIN parking P where F.s_id=2 and F.p_id IS NOT NULL ORDER BY F.dt LIMIT 8")
    data=cursor.fetchall()
    cursor.close()
    return data

def ptttr(id):
    cursor=connection.cursor()
    cursor.execute("SELECT * from flight where f_id=?",(id,))
    data=cursor.fetchone()
    i=data[5]
    cursor.execute("UPDATE flight set s_id=3 where f_id=?",(id,))
    cursor.execute("UPDATE parking set pv=1 where p_id=?",(i,))
    connection.commit()
    cursor.close()

def gtr():
    cursor=connection.cursor()
    cursor.execute("SELECT F.f_id,F.at,F.dt,F.ac_id,FT.ft_det,F.flt_no,F.flt_name,F.Deptto from flight F NATURAL JOIN flttype FT where F.s_id=3 ORDER BY F.dt LIMIT 8")
    data=cursor.fetchall()
    cursor.close()
    return data

def ptt(id):
    cursor=connection.cursor()
    cursor.execute("UPDATE flight set s_id=4 where f_id=?",(id,))
    connection.commit()
    cursor.close()

def rtt():
    cursor=connection.cursor()
    cursor.execute("SELECT F.f_id,F.at,F.dt,F.ac_id,FT.ft_det,F.flt_no,F.flt_name,F.Deptto from flight F NATURAL JOIN flttype FT where F.s_id=4 ORDER BY F.dt LIMIT 8")
    data=cursor.fetchall()
    cursor.close()
    return data

def usto(id):
    cursor=connection.cursor()
    cursor.execute("UPDATE flight set s_id=5 where f_id=?",(id,))
    connection.commit()
    cursor.close()


def his():
    cursor=connection.cursor()
    cursor.execute("SELECT F.f_id,F.at,F.dt,F.ac_id,FT.ft_det,F.flt_no,F.flt_name,P.p_name,F.Arrfrom,F.Deptto from flttype FT NATURAL JOIN flight F NATURAL JOIN parking P where F.s_id=5 ORDER BY F.dt LIMIT 8")
    data1=cursor.fetchall()
    cursor.close()
    return data1

def showroute1(id):
    cursor=connection.cursor()
    cursor.execute("SELECT P.routepark from parking P NATURAL JOIN flight F where f_id=?",(id,))
    data=cursor.fetchone()
    i=data[0]
    cursor.close()
    return i

def showroute2(id):
    cursor=connection.cursor()
    cursor.execute("SELECT P.routerun from parking P NATURAL JOIN flight F where f_id=?",(id,))
    data=cursor.fetchone()
    i=data[0]
    cursor.close()
    return i
