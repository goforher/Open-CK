原始数据格式为 CSV 文件，每个文件大小约为 2GB。由于 GitHub 对文件上传的容量限制，无法将 CSV 文件上传至项目中。然而，您可以通过 Google Drive 获取原始文件，下载地址为：<a href="https://drive.google.com/drive/folders/1kd6z_HsaO_YHdOMjFVp59SORWlGwL3Jb?usp=sharing">下载链接</a>。

原始文件的维度为 (T, D)，其中 T 代表时间，D 代表传感器。前两行分别为单位和传感器名称。传感器类型通过命名前缀进行区分，传感器的布置方式为从左到右、从上到下。例如，温度传感器命名为 temperature1、temperature2、……、temperatureN。

我们设置了三种类型的传感器，依次为温度、速度和压强，传感器的分辨率为 300x300。每个工况模拟了 400 秒的时间。

在项目中，我们提供了脚本，将 CSV 文件转换为更易于使用的 NP 文件。我们将初始维度 (400, 3*300*300) 转换为 NP 文件中的维度 (400, 3, 300, 300)。
