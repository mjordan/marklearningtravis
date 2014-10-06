import sys
import pytest
sys.path.append("lib")

import MySQLdb
import MySQLdb.cursors
import requests

def test_requests():
    r = requests.get('http://localhost/hello')
    # r = requests.get('http://localhost')
    assert r.status_code == 200

def test_mysql():
    try:
        con = MySQLdb.connect('127.0.0.1', 'root', '', 'pkppln')
        cur = con.cursor()
        cur.execute("SELECT * FROM terms_of_use")
        result = cur.fetchall()
    except MySQLdb.Error, e:
        sys.exit(1)

    assert len(result)
