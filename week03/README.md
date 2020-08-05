# 作业

**作业1：**

+ 编写了一个基于多进程模型的主机扫描器
+ 以os、socket完成ping以及扫描端口操作。
+ 运行以命令行形式进行
  + -n：指定并发数量。
  + -f ping：进行 ping 测试
    + 需要成功的ip
  + -f tcp：进行 tcp 端口开放、关闭测试。
    + 1-1024的端口
  + -ip：连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
    + 连续IP地址前三位必须相同，否则报错
  + -w：扫描结果进行保存。
    + 当没有-w时，将终端输出。
    + 有则保存至文件，终端一般不输出具体结果。
+ 示例命令(```pmap.py```同一目录下逐一执行以下命令验证)：
  +  ```python pmap.py -n 4 -f ping -ip 39.107.250.116 ```
  + ``` python pmap.py -n 8 -f ping -ip 39.107.250.116-39.107.250.126``` 
  + ``` python pmap.py -n 8 -f ping -ip 39.107.250.116-39.107.250.126 -w ping_result.txt -v```
  + ```python pmap.py -n 8 -f tcp -ip 39.107.250.116 -v```
  + ```python pmap.py -n 8 -f tcp -ip 39.107.250.116-39.107.250.126 -v -w tcp_result.json```
+ 运行以上命令便可得到work_1中的```ping_result.txt```以及```tcp_result.json```文件。



**作业2：**

+ 截止前没更新就是没做。



**总结查看**[NOTE.md](https://github.com/Bonnenult222RenYu/Python-002/blob/master/week03/NOTE.md)

