
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


`components.ini`

```[component]  ([accumulo]):
COMMON_BUILD_OPTS : Values defined to be referenced in the below sections. 

Builds Set the version for every project while building. The default versions in the pom will be replaced with the actual build versions. 

setversion_cmd : Used when a single set version command is needed.
    ex: 
      setversion_cmd = ${MVN_CMD} ${MVN_SET_VERSION_CMD} -DnewVersion=${oozie_jar_version}

[[setversion_cmd]] :
    Used when a list of set version commands needs to be declared.
    ex:
      [[setversion_cmd]]
          cmd_1 = ${MVN_CMD} ${MVN_SET_VERSION_CMD} -DnewVersion=${hive_jar_version}
          cmd_2 = ${MVN_CMD} ${MVN_SET_VERSION_CMD} -DnewVersion=${hive_jar_version} , storage-api
          cmd_3 = ${MVN_CMD} ${MVN_SET_VERSION_CMD} -DnewVersion=${hive_jar_version}, standalone-metastore
          cmd_4 = ${MVN_CMD} ${MVN_SET_VERSION_CMD} -DnewVersion=${hive_jar_version}, upgrade-acid
    # 'cmd_*' has no real value, just a identifier.

[[artifacts]] :
    List of artifacts to be archived.
    ex:
      [[artifacts]]
        artifact_1 = build/hue-${hue_jar_version}.tar.gz
        artifact_2 = desktop/desktop.db
    
    # 'artifact_*' has no real value, just a identifier.


[[install_cmd]] : 
    List of build commands in the order of execution.
    ex:
      [[install_cmd]]
        cmd_0 = ${GRADLE4102_CMD}
        cmd_1 = ./gradlew ${BUILD_KAFKA_SETVERSION_OPTS}
        cmd_2 = ./gradlew ${BUILD_KAFKA_INSTALL_OPTS}
        cmd_3 = ./gradlew ${BUILD_KAFKA_DOC_OPTS}

    # 'cmd_*' has no real value, just a identifier.

[[test_cmd]] :
    List of unittest commands

[[test_coverage_cmd]] :
    List of test coverage commands

[[fortify_cmd]] :
    List of fortify commands

[[text-replace]]
    Construct to replace strings in files, my using either regex_replace or key_value
    ex: [[text-replace]]
        REPLACE_1 = 'cdhZookeeperVersion', '"${zookeeper_jar_version}"', gradle/dependencies.gradle , regex_replace
        REPLACE_2 = "${hive_apache_base_maven_version}", ${hive_jar_version}, pom.xml , key_value

[[xml-replace]]
    Construct to replace xmltag values.
    ex: [[xml-replace]]
            REPLACE_1 = 'hadoop-two.version', ${hadoop_jar_version}, pom.xml
            REPLACE_2 = 'hadoop.version', ${hadoop_jar_version}, pom.xml
            REPLACE_3 = 'hbase.version', ${hbase_jar_version}, pom.xml

    # "REPLACE_*" has no real value, just a identifier.

```