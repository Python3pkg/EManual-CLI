EManual-CLI
-----------

Command Line Interface for EManual

install
-------
```shell
pip install emanual
```

Usage
-----

1. 创建`info.json` & 把中文文件名变为拼音
```shell
cd path/to/md-xxx
emanual create
// `./dist/markdown`就是生成的内容
````

2. 生成lang.zip
```shell
emanual dist {lang} //lang为指定的语言，小写
```


Development
-----------

```shell
//create you virtual python envirment
virtualenv env
source env/bin/activate

//exit
activate
```

License
-------

MIT
