1. SELECT * FROM data;

   <font color="red">data</font>

2. SELECT * FROM data LIMIT 10;

   <font color="red">data.head(10)</font>

3. SELECT id FROM data;  //id 是 data 表的特定一列

   <font color="red">data['id']</font>

4. SELECT COUNT(id) FROM data;

   <font color="red">data['id'].count()</font>

5. SELECT * FROM data WHERE id<1000 AND age>30;

   <font color="red">data[(data['id']<1000) & (data['age']>30)]</font>

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

   <font color="red">table1.groupby('id').agg({'order_id':pd.Series.nunique})</font>

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

   <font color="red">pd.merge(table1, table2, on='id')</font>

8. SELECT * FROM table1 UNION SELECT * FROM table2;

   <font color="red">pd.concat([table1, table2]).drop_duplicates()</font>

9. DELETE FROM table1 WHERE id=10;

   <font color="red">table1 = table1.loc[table1['id']!=10]</font>

10. ALTER TABLE table1 DROP COLUMN column_name;

    <font color="red">del table1['column_name']</font>

