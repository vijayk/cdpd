###If you modify this file, you need to make sure that it's proper by executing the following command.

```
cat hdp-base.json |python -mjson.tool
```
###Example

```
  "accumulo":{
      "repo-url":"git://git.apache.org/incubator-tez.git",
      "internal-repo-name":"mrx"
      "branch":"branch-3.4",
      "version":"0.4.0",
      "enable-merge":false,
      "enable-sync":false,
      "depends-on":[ "hadoop", "zookeeper" ]
      "no-partner": [ "monarch" ]
    },  
```


Element| Explanataion |Notes|
------------- | -------------|----------|
repo_url | Apache Repo URL | This is where where we are inheriting the opensource component from.
internal-repo-name| internal-name | If different from external repo name.
branch   | branch in the apache repo  that is basis for this release|
version  | Apache version number or expected apache release version |
enable-merge | Setup auto-merge from apache branch into our release branch.| default:True
enable-sync|Setup references branches into hwx repo from apache/external repos|default:True
depends-on | Other components this componet depends on. | Transient dependenices will be calculated
no-partner | List of partners that do not qualify for a given component | defaul:Null
