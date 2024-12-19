from paddlex import create_pipeline
import os

pipeline = create_pipeline(pipeline="seal_recognition")

output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/seal_text_det.png")
for res in output:
    res.print() ## 打印预测的结构化输出
    res.save_to_img("./output/") ## 保存可视化结果