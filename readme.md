# 训练自定义Haar Cascade分类器

Haar算法实际上是运用了boosting算法中的Adaboost算法。Haar分类器利用Adaboost算法构建一个强分类器进行级联，而在底层特征抽取上采用的是高效的矩形特征以及积分图方法。

Haar分类器=类Haar特征+积分图法+Adaboost算法+级联。

Haar分类器主要步骤如下：

* 提取类Haar特征
* 利用积分图法对类Haar特征提取进行加速
* 使用Adaboost算法训练强分类器
* 使用筛选式级联把强的分类器级联在一起，从而提高检测准确度

## 准备数据

标定数据集，将Positive数据整理到p文件夹，Negative数据整理到n文件夹。

为方便测试，可用 `icrawler` 抓取图片。

```py
pip install icrawler
```

## 训练

`Cascade Trainer GUI` 加载数据目录，修改“Negative Image Count”。

按需修改训练参数，“Start”开始训练。

训练完成，生成 `classifier.Cascade.xml` 文件。

## 验证

加载分类器验证。

```py
python .\validate.py
```

## 参考链接

* [make Custom Haar Cascade Classifier](https://medium.com/@vipulgote4/guide-to-make-custom-haar-cascade-xml-file-for-object-detection-with-opencv-6932e22c3f0e)
* [Haar级联分类器简介](https://zhuanlan.zhihu.com/p/100217697)
* [Cascade Trainer GUI](https://amin-ahmadi.com/cascade-trainer-gui/)
* [icrawler：强大简单的图片爬虫库](https://blog.csdn.net/zaf0516/article/details/115374438)
