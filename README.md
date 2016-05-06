# zsphere

运维平台

## 架构说明

- 技术栈

        Tornado
        Bootstrap
        MongoDB


## 功能说明

- Ansibe UI

## Install

1. 配置数据库

  * 创建mongodb数据库

        db.createCollection("zsphere")

  * 添加用户

    ```
        db.createUser(
          {
            user: "zsphere",
            pwd: "zsphere",
            roles: [{role: "dbOwner", db: "zsphere"}]
          }
        )
    ```

2. 配置virtualenv环境

        cd /opt
        virtualenv zsphere
        source zsphere/bin/active

3. 下载源码

        git clone https://github.com/devops/zsphere.git

4. 安装依赖库

        cd zsphere
        pip install -r requirements.txt

## Run

- 直接运行

        python runserver.py
