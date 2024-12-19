from paddlex import create_pipeline
import os

pipeline = create_pipeline(pipeline="ts_ad")

output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/ts_ad.csv")
for res in output:
    res.print() ## 打印预测的结构化输出
    res.save_to_csv("./output/") ## 保存csv格式结果