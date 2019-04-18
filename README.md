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

`COMPONENT ELEMENTS`

|Element| Explanataion |Value Type | Notes|
|:------- | :--------|:----------| :----------
branch   | branch in the apache repo that is basis for this release| string | Used in enable-sync and enable-merge constructs
build-group | group of components to be built together | list | Used in parallel and CI builds, to bundle components together.
depends-on | Other components this componet depends on. | list | Transient dependenices will be calculated
enable-blackduck-scan | Setup blackduck scan for the component | (bool) default: false |
enable-build | Enable the component build | (bool) default: true
enable-merge | Setup auto-merge from apache branch into our release branch.| (bool) default: false
enable-sync| Setup references branches into hwx repo from apache/external repos| (bool) default: false
image-name | Name of the image created by a component build | string |
internal-merge  | Self repo branch to merge into the component branch | string | It is defined to overwrite the default merge from apache, merges from internal branch instead of merge.
internal-repo-name| internal-name | string | If different from external repo name.
maven-group-id | Maven group id | string | separated by '/' and not ','
no-clone | Do not clone a new workspace using the component name, instead share the workspace of a different component | string | Component name of sharing workspace
no-partner | List of partners that do not qualify for a given component |  (list)  default: null
node-label | Jenkins node label | string | It is used while triggering the jenkins jobs.
platforms | List of platforms applicable to the component | list | Override the list defined at the product level 
poll | Trigger a build if the component changes  | (bool) default: true
repo_url | Apache Repo URL | string | This is where where we are inheriting the opensource component from.
version  | Apache version number or expected apache release version | string | 
