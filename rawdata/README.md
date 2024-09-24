The raw data format is CSV files, with each file approximately 2GB in size. Due to GitHub's file upload size limitations, it is not possible to upload the CSV files to the project. However, you can obtain the raw files from Google Drive at the following link: <a href="https://drive.google.com/drive/folders/1kd6z_HsaO_YHdOMjFVp59SORWlGwL3Jb?usp=sharing">Download Link</a>.

The dimensions of the raw files are (T, D), where T represents time and D represents sensors. The first two rows are the units and sensor names, respectively. Sensor types are distinguished by naming prefixes, and the arrangement of sensors is from left to right and top to bottom. For example, temperature sensors are named temperature1, temperature2, ..., temperatureN.

We have set up three types of sensors: temperature, velocity, and pressure, with a resolution of 300x300. Each condition simulates a duration of 400 seconds.

In the project, we provide scripts to convert the CSV files into more user-friendly NP arrays. We convert the initial dimensions from (400, 3*300*300) to (400, 3, 300, 300) in the NP arrays.
