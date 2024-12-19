from paddlex import create_pipeline
import os

def test(device='gpu'):
    pipeline = create_pipeline(pipeline="image_classification")

    output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/general_image_classification_001.jpg", device=device)
    for res in output:
        res.print() ## 打印预测的结构化输出
        res.save_to_img("./output/") ## 保存结果可视化图像
        res.save_to_json("./output/") ## 保存预测的结构化输出


if __name__ == "__main__":
    test()