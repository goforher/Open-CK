原始数据格式为CSV文件，单个文件大小约为2GB，由于github上传文件具有容量限制，无法将csv文件上传至项目中。但是你可以通过Google Drive获取原始文件，<a href="https://drive.google.com/drive/folders/1kd6z_HsaO_YHdOMjFVp59SORWlGwL3Jb?usp=sharing">下载地址</a>。

原始文件的维度是（T, D），其中T代表时间，D代表传感器，前两行分别为单位和传感器名称。传感器类型通过命名前缀来进行区分，传感器布置方式为由左到右，由上至下。如温度传感器一次命名为temperature1、temperature2、、、、、、temperatureN

我们一共设置了3种类型的传感器，依次为温度、速度、压强，传感器的分辨率为300x300。每个工况模拟了400s的时间。

项目中，我们提供了脚本，将csv文件转换为更易使用的npy文件，我们将初始维度(400,3*300*300)转换为npy文件中的维度(400,3,300,300)