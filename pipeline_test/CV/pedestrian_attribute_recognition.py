from paddlex import create_pipeline
import os

def test(device='cpu'):
    pipeline = create_pipeline(pipeline="pedestrian_attribute_recognition")

    output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/pedestrian_attribute_002.jpg", device=device)
    for res in output:
        res.print() ## 打印预测的结构化输出
        res.save_to_img("./output/") ## 保存结果可视化图像
        res.save_to_json("./output/") ## 保存预测的结构化输出


if __name__ == "__main__":
    test()