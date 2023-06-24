# Hadoop vs Python
This project aims to compare the performance and scalability of Word Count MapReduce programs implemented in Hadoop and Python, focusing on various data sizes. By analyzing the execution time and resource utilization of both implementations, we seek to understand how these technologies handle different data volumes.

Made by SBD 01 Group 3:
- Cecilia Inez Reva Manurung - 2106636994
- Gemilang Bagas Ramadhani - 2006535205
- Laode Alif Ma'sum Sidrajat Raja Ika - 2106731213
- Zalfy Putra Rezky - 2106731453

#### Text files for testing
- `100 KB` personae.txt
- `1 MB` melville.txt
- `10 MB` shakespeare.txt
- `100 MB` [enwik8.txt](https://mattmahoney.net/dc/enwik8.zip)
- `1 GB` [enwik9.txt](https://mattmahoney.net/dc/enwik9.zip)

## Install Hadoop on Ubuntu 20.04

### Step 1: Install Java and other dependencies
Update system
```
sudo apt update
```
Install  Java 1.8.0_132
```
sudo apt install openjdk-8-jdk -y
```

### Step 2: Install OpenSSH
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

### Step 3: Install Hadoop
Download Hadoop 3.3.2
```
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.2/hadoop-3.3.2.tar.gz
```
Extract the downloaded file.
```
tar -xvzf hadoop-3.3.2.tar.gz
```

### Step 4: Configure Hadoop
A Hadoop environment is configured by editing a set of configuration files:<br>
```
bashrc, hadoop-env.sh, core-site.xml, hdfs-site.xml, mapred-site-xml and yarn-site.xml
```
For more information, see the [article](https://medium.com/@festusmorumbasi/installing-hadoop-on-ubuntu-20-04-4610b6e0391e)

### Step 5: Start Hadoop
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

### Step 6: Access Hadoop UI from Browser
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
This program is used to count the frequency of each word in a given set of documents, in this case a given set of TXT files.

#### Hadoop
This is an example of using the Hadoop MapReduce JAR program on a 100 KB file
```
hdfs dfs -mkdir /100kb
hdfs dfs -put /home/hadoop/Downloads/wordcount/personae.txt /100kb
time hadoop jar /home/hadoop/hadoop-3.3.2/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.2.jar wordcount /100kb /output-100kb
hdfs dfs -get /output-100kb/part-r-00000 /home/hadoop/Downloads/wordcount/output-100kb.txt
```

#### Python
Open the integrated terminal of the directory
```
python wordcount.py filename.txt
```
For python 3, change python to `python3`

## Implementation
#### Device Specification (VirtualBox)

| Specification | Description       |
|---------------|-------------------|
| Prosesor      | AMD Ryzen 7 5800H |
| Core          | 8-core            |
| RAM           | 28 GB             |
| Storage       | 64 GB             |
| OS            | Ubuntu 20.04      |

#### Test Results
![Table](https://raw.githubusercontent.com/zalfyputra/hadoop-vs-python/main/img/table.png)

#### Graph
![Plot](https://raw.githubusercontent.com/zalfyputra/hadoop-vs-python/main/img/plot.png)

#### Analysis
Jika membandingkan waktu eksekusi wordcount dengan python dan menggunakan Hadoop, maka wordcount python lebih cepat karena data yang dihitung disimpan dan dilakukan pada satu mesin atau server tunggal. Sehingga, hanya terjadi sedikit overhead terkait pengaturan dan komunikasi antar node dalam cluster seperti pada Hadoop. Dan untuk ukuran file yang relatif kecil (100 kb, 1 mb, 10 mb) maka wordcount dengan python dapat menyelesaikan tugas lebih cepat karena tidak melibatkan kompleksitas yang signifikan.

Sedangkan, hadoop dirancang untuk memproses dan menganalisis data dalam skala besar dengan membagi tugas pemrosesan ke beberapa node dalam cluster sehingga dapat terjadi overhead yang signifikan walaupun penggunaan hadoop sangat efektif, khususnya pada platform terdistribusi dan data dalam ukuran besar. 

Kinerja hadoop menjadi lebih lambat dibandingkan wordcount normal pada skala kecil karena membutuhkan waktu untuk menghubungkan node-node dalam cluster dan komunikasi antar node.

#### Conclusion
Untuk data yang besar dan membutuhkan pemprosesan dalam skala yang luas, Hadoop menjadi pilihan lebih baik karena lebih optimal. Sedangkan, pada kasus diatas, wordcount normal tidak melibatkan pengaturan dan komunikasi antar node yang kompleks sehingga kinerja lebih cepat dibandingkan menggunakan Hadoop.

#### References
[Install Hadoop on Ubuntu 20.04](https://medium.com/@festusmorumbasi/installing-hadoop-on-ubuntu-20-04-4610b6e0391e)