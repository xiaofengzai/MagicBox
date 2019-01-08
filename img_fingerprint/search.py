# coding=utf-8
# 导入必要的包
from PIL import Image
import imagehash
import argparse
import shelve

# 构建参数解析，并分析参数
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="照片数据集的路径")
ap.add_argument("-s", "--shelve",required=True,
                help="shelve数据集的输出")
ap.add_argument("-q", "--query", required=True,
                help="搜索图像的路径")
args = vars(ap.parse_args())

# 打开shelf数据集
db = shelve.open(args["shelve"])

# 加载需要查询的图片，计算它的图像差分散列值，并从数据库中抓取类似散列值得图像
query = Image.open(args["query"])
print(args["query"])
h = str(imagehash.dhash(query))
filenames = db[h]
print("Found %d images" % (len(filenames)))

# 在图像内部循环
for filename in filenames:
    image = Image.open(filename)
    image.show()
    
# 关闭数据集
db.close()


#python search.py -d img -s db.shelve -q img/image_0001.jpg