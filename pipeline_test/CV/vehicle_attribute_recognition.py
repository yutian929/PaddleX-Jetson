from paddlex import create_pipeline
import os
import gc

def test(settings=None):
    pipeline = create_pipeline(pipeline="vehicle_attribute_recognition", device=settings['device'])

    output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/vehicle_attribute_002.jpg")
    for res in output:
        res.print() ## 打印预测的结构化输出
        res.save_to_img("./output/") ## 保存结果可视化图像
        res.save_to_json("./output/") ## 保存预测的结构化输出


    del pipeline
    gc.collect()

if __name__ == "__main__":
    test()