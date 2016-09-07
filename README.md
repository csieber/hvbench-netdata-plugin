# hvbench-netdata-plugin

A performance monitoring plugin for hvbench based on [netdata](https://github.com/firehol/netdata). It takes the messages send by hvbench to kafka and visualises them.

## INSTALL

  - Copy our custom netdata-plugin into netdata's plugin directory:

```
git clone https://github.com/csieber/hvbench-netdata-plugin.git
cd hvbench-netdata-plugin
sudo cp *.plugin /usr/libexec/netdata/plugins.d/

```
  - Configure netdata so that it only shows the data from our custom netdata plugin. Copy our custom Netdata configuration file to this directory:
```
sudo cp netdata.conf /etc/netdata/
sudo killall netdata
sudo /usr/sbin/netdata
```
Perform step two, in hvbench-api folder (netdata.conf file is placed there.).
We kill all current plugins and then restart the netdata so that it loads our custom Netdata configuration file.

This file significantly reduces the resources consumed by netdata. Reduced resource consumption is achieved by:

    1. Disable External plugins
    2. Disable Internal plugins
    3. Disable Logs (Error log,access log, debug log)
    4. Setting memory mode to RAM
    5. Lower memory by reducing history
    6. Disable gzip compression of responses --- Gzip compression of the web responses is using more CPU that the rest of netdata.
    7. Single threaded web server

Now, you can go to your browser and see your charts here: http://[IP of netdata host]:19999/index.html

If you see that a chart is not displayed, just referesh the tab. This is because we have changed the settings in the conf file to lower the memory requirements (i.e. when we add new charts during execution of the plugin). 

## Notes

1) Netdata is a real-time performance monitoring solution. You can read about it, in detail, here: https://github.com/firehol/netdata/wiki

2) This is the first version of netdata-plugin, to get you started. It can be significantly improved. Feel free to modify it according to your need.
