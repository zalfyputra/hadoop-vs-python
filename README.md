# WordCount Program

This program is used to count the frequency of each word in a given set of documents, in this case a given set of TXT files. The program consists of two main stages: the Map stage and the Reduce stage.

SBD Group 3:
- Cecilia Inez Reva Manurung - 2106636994
- Gemilang Bagas Ramadhani - 2006535205
- Laode Alif Ma'sum Sidrajat Raja Ika - 2106731213
- Zalfy Putra Rezky - 2106731453

#### Download links
- `100 KB` personae.txt
- `1 MB` melville.txt
- `10 MB` shakespeare.txt
- [Text file: 100 MB](https://mattmahoney.net/dc/enwik8.zip)
- [Text file: 1 GB](https://mattmahoney.net/dc/enwik9.zip)

## Install Hadoop on Ubuntu 20.04
By Festus Morumbasi<br>
https://medium.com/@festusmorumbasi/installing-hadoop-on-ubuntu-20-04-4610b6e0391e

#### Step 1: Install Java and other dependencies
Update system
```
sudo apt update
```
Install  Java 1.8
```
sudo apt install openjdk-8-jdk -y
```

#### Step 2: Install OpenSSH
Install the OpenSSH server and client
```
sudo apt install openssh-server openssh-client -y
```
Generate public and private key pairs
```
ssh-keygen -t rsa
```
Add the generated public key from `id_rsa.pub` to `authorized_keys`
```
sudo cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
Change the permissions of the `authorized_keys` file
```
sudo chmod 640 ~/.ssh/authorized_keys
```
Verify if the password-less SSH is functional.
```
ssh localhost
```

#### Step 3: Install Hadoop
Download Hadoop 3.3.2
```
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.2/hadoop-3.3.2.tar.gz
```
Extract the downloaded file.
```
tar -xvzf hadoop-3.3.2.tar.gz
```

#### Step 4: Configure Hadoop
A Hadoop environment is configured by editing a set of configuration files:<br>
```
bashrc, hadoop-env.sh, core-site.xml, hdfs-site.xml, mapred-site-xml and yarn-site.xml
```
For more information, see the [article](https://medium.com/@festusmorumbasi/installing-hadoop-on-ubuntu-20-04-4610b6e0391e)

#### Step 5: Start Hadoop
It is important to format the NameNode before starting Hadoop services for the first time:
```
hdfs namenode -format
```
Start the NameNode and DataNode
```
start-dfs.sh
```
Start the YARN resource and node managers
```
start-yarn.sh
```
Verify all the running components
```
jps
```

#### Step 6: Access Hadoop UI from Browser
Use your preferred browser and navigate to your localhost URL or IP. The default port number `9870` gives you access to the Hadoop NameNode UI
```
http://localhost:9870
```
The default port `9864` is used to access individual DataNodes directly from your browser:
```
http://localhost:9864
```
The YARN Resource Manager is accessible on port `8088`
```
http://localhost:8088
```

## Run MapReduce Program

#### Hadoop
This is an example of using the Hadoop MapReduce JAR program on a 100 KB file
```
hdfs dfs -mkdir /100kb
hdfs dfs -put /home/hadoop/Downloads/wordcount/personae.txt /100kb
time hadoop jar /home/hadoop/hadoop-3.3.2/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.2.jar wordcount /100kb /output-100kb
hdfs dfs -get /output-100kb/part-r-00000 /home/hadoop/Downloads/wordcount/output-100kb.txt
```

#### Python
Open integrated terminal in the directory
```
python wordcount.py filename.txt
```
for python 3 use `python3`

## Implementation

#### Test Results
![Table](https://raw.githubusercontent.com/zalfyputra/hadoop-vs-python/main/img/table.png)

#### Graph
Comparing Hadoop and Python execution times for different file sizes using a plotting library like Matplotlib in Python
![Plot](https://raw.githubusercontent.com/zalfyputra/hadoop-vs-python/main/img/plot.png)

#### Analysis
#### Conclusion