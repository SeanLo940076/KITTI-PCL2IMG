# KITTI-PCL2IMG
 A Python tool for converting KITTI dataset point cloud data to 2D images using cylindrical projection, visualizing distance with HSV color mapping.

## 專案概述
本專案旨在將 KITTI 資料集中的點雲資料透過球座標投影轉換為二維影像。該轉換過程使用了柱面投影方法，將點雲數據轉換為二維平面圖像，並通過 HSV 色彩空間顯示點與雷達的距離。

## 主要功能

- **點雲轉換**： 將 `.bin` 格式的點雲數據轉換為二維圖像。
- **距離可視化**： 使用 HSV 色彩映射物體距離。

## 環境需求

- Python 3.x
- OpenCV
- NumPy
- tqdm

## 使用方法

### 1. 設置資料夾路徑

修改 `input_folder` 和 `output_folder` 變數，設定點雲資料夾和輸出影像的儲存路徑。

### 2. 執行腳本

執行以下命令來處理資料夾中的所有點雲文件並生成相應的二維影像：

```bash
python Point2Image.py
python Image2Video.py
```

### 3. **結果**
產生的影像將以 `.png` 格式儲存在指定的輸出資料夾中。

### 參數設定

- **`image_width` 和 `image_height`**：設定影像的寬度和高度，基於 Velodyne HDL-64E 的視野（FOV）決定。
- **`vertical_fov`**：設定垂直視場角度，預設值為 26.8 度。

### 注意事項

- 確保輸入資料夾包含 `.bin` 格式的點雲檔案。
- 根據需求調整 `max_dist` 參數以控制距離標準化。