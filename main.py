# coding: utf-8
from PIL import Image
from function import draw_text
import sys

############################ Strat 各変数の宣言

# 引数から文字を受け取る
TARGET_STRING = sys.argv[1]

# otfファイルまでのパス
OTF_FILE_PATH = 'font.otf'

# 出力用ファイルまでのパス
OUTPUT_FILE_PATH = 'tmp/' + 'output.jpg'

# 元画像ファイルまでのパス
FRAME_FILE_PATH  = 'image.jpg'

############################ End 各変数の宣言

# 元画像データを取得
image_data = Image.open(FRAME_FILE_PATH)

# 文字合成
font_size          = 80
draw_start_x       = 60
draw_start_y       = 20
draw_text(image_data, font_size, OTF_FILE_PATH, TARGET_STRING, draw_start_x, draw_start_y)

# 合成した画像の書き出し
image_data.save(OUTPUT_FILE_PATH)
image_data.show();
