# marker.py

为图片添加文字水印
可设置文字**大小、颜色、旋转、间隔、透明度**

# usage

需要 PIL 库 `pip install Pillow`

```
usage: marker.py [-h] [-f FILE] [-m MARK] [-o OUT] [-c COLOR] [-s SPACE]
                 [-a ANGEL] [--size SIZE] [--opacity OPACITY]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  image file path or directory
  -m MARK, --mark MARK  watermark content
  -o OUT, --out OUT     image output directory, default is ./output
  -c COLOR, --color COLOR
                        text color like '#000000', default is #8B8B1B
  -s SPACE, --space SPACE
                        space between watermarks, default is 75
  -a ANGEL, --angel ANGEL
                        rotate angel of watermarks, default is 30
  --size SIZE           font size of text, default is 50
  --opacity OPACITY     opacity of watermarks, default is 0.15
  --quality QUALITY     quality of output images, default is 90
```

# 效果

`python marker.py -f ./input/test.png -m 添加水印`

![](https://github.com/2Dou/watermarker/raw/master/output/test.png)

# 修改

套了个壳，本仓库下的版本比原版本增加了配置文件，参数写在同目录下的config.json中。

默认参数：

```javascript
{
    "angle": 30,
    "color": "#8B8B1B",
    "file": "./input",
    "mark": "添加水印",
    "opacity": 0.15,
    "out": "./output",
    "quality": 80,
    "size": 50,
    "space": 75
}
```

`python watermarker.py`
