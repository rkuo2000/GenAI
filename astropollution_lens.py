import cv2
import numpy as np

import sys
image_file = sys.argv[1]

def analyze_light_pollution(image_path):
    """
    讀取星空照片並分析光害程度。
    以平均像素亮度作為光害的初步指標。

    參數:
        image_path (str): 星空照片的檔案路徑。

    返回:
        float: 圖片的平均像素亮度值，或 None 如果圖片無法讀取。
    """
    # 1. 讀取影像
    img = cv2.imread(image_path)

    if img is None:
        print(f"錯誤：無法讀取圖片，請檢查路徑：{image_path}")
        return None

    print(f"成功讀取圖片：{image_path}")

    # 2. 轉換為灰階
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. 計算平均亮度
    # 使用 numpy 的 mean 函數計算所有像素的平均值
    average_brightness = np.mean(gray_img)

    print(f"圖片的平均亮度為：{average_brightness:.2f}")

    # 4. 提供評估建議 (基於經驗的簡化判斷)
    print("\n光害程度初步評估（基於平均亮度）：")
    if average_brightness < 30:
        print("  光害非常輕微，天空背景非常暗。這是極佳的觀星地點！")
    elif average_brightness < 60:
        print("  光害輕微，天空背景較暗。適合多數星空攝影。")
    elif average_brightness < 100:
        print("  光害中等，天空背景略亮。可能需要較短的曝光時間或後期處理來減輕光害影響。")
    else:
        print("  光害較為嚴重，天空背景明亮。在這種環境下拍攝深空天體會較困難。")

    return average_brightness

# --- 使用範例 ---
if __name__ == "__main__":

    print("--- 分析星空照片 ---")
    dark_sky_brightness = analyze_light_pollution(image_file)
    print("\n" + "=" * 40 + "\n")
