from paddlex import create_pipeline
import os

def test(device='cpu'):
    pipeline = create_pipeline(pipeline="multi_label_image_classification", device=device)

    output = pipeline.predict(os.path.dirname(os.path.realpath(__file__)) + "/resources/general_image_classification_001.jpg")
    for res in output:
        res.print() ## 打印预测的结构化输出
        res.save_to_img("./output/") ## 保存结果可视化图像
        res.save_to_json("./output/") ## 保存预测的结构化输出


if __name__ == "__main__":
    test()